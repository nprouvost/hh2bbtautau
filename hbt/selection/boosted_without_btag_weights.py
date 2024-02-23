from columnflow.selection import Selector, SelectionResult, selector
from columnflow.util import maybe_import, dev_sandbox
from columnflow.production.processes import process_ids
from columnflow.production.cms.mc_weight import mc_weight
from columnflow.production.cms.pileup import pu_weight
from columnflow.production.cms.pdf import pdf_weights
from columnflow.production.cms.scale import murmuf_weights
from columnflow.production.util import attach_coffea_behavior
from hbt.production.features import cutflow_features

from collections import defaultdict, OrderedDict

from operator import and_
from functools import reduce

from hbt.selection.boosted_jet import boosted_jet_selector
from hbt.selection.lepton import lepton_selection
from hbt.selection.trigger import trigger_selection
from IPython import embed

np = maybe_import("numpy")

ak = maybe_import("awkward")

@selector(
    uses={pu_weight},
)
def increment_stats(
    self: Selector,
    events: ak.Array,
    results: SelectionResult,
    stats: dict,
    **kwargs,
) -> ak.Array:
    """
    Unexposed selector that does not actually select objects but instead increments selection
    *stats* in-place based on all input *events* and the final selection *mask*.
    """
    # get event masks
    event_mask = results.main.event
    event_mask_no_bjet = results.steps.all_but_bjet

    # increment plain counts
    stats["n_events"] += len(events)
    stats["n_events_selected"] += ak.sum(event_mask, axis=0)

    # get a list of unique jet multiplicities present in the chunk
    unique_process_ids = np.unique(events.process_id)
    unique_n_jets = []
    if results.has_aux("n_central_jets"):
        unique_n_jets = np.unique(results.x.n_central_jets)

    # create a map of entry names to (weight, mask) pairs that will be written to stats
    weight_map = OrderedDict()
    if self.dataset_inst.is_mc:
        # mc weight for all events
        weight_map["mc_weight"] = (events.mc_weight, Ellipsis)

        # mc weight for selected events
        weight_map["mc_weight_selected"] = (events.mc_weight, event_mask)

        # mc weight times the pileup weight (with variations) without any selection
        for name in sorted(self[pu_weight].produces):
            weight_map[f"mc_weight_{name}"] = (events.mc_weight * events[name], Ellipsis)

        # mc weight for selected events, excluding the bjet selection
        weight_map["mc_weight_selected_no_bjet"] = (events.mc_weight, event_mask_no_bjet)

        # weights that include standard systematic variations
        for postfix in ["", "_up", "_down"]:
            # pdf weight for all events
            weight_map[f"pdf_weight{postfix}"] = (events[f"pdf_weight{postfix}"], Ellipsis)

            # pdf weight for selected events
            weight_map[f"pdf_weight{postfix}_selected"] = (events[f"pdf_weight{postfix}"], event_mask)

            # scale weight for all events
            weight_map[f"murmuf_weight{postfix}"] = (events[f"murmuf_weight{postfix}"], Ellipsis)

            # scale weight for selected events
            weight_map[f"murmuf_weight{postfix}_selected"] = (events[f"murmuf_weight{postfix}"], event_mask)


    # get and store the weights
    for name, (weights, mask) in weight_map.items():
        joinable_mask = True if mask is Ellipsis else mask

        # sum for all processes
        stats[f"sum_{name}"] += ak.sum(weights[mask])

        # sums per process id and again per jet multiplicity
        stats.setdefault(f"sum_{name}_per_process", defaultdict(float))
        stats.setdefault(f"sum_{name}_per_process_and_njet", defaultdict(lambda: defaultdict(float)))
        for p in unique_process_ids:
            stats[f"sum_{name}_per_process"][int(p)] += ak.sum(
                weights[(events.process_id == p) & joinable_mask],
            )
            for n in unique_n_jets:
                stats[f"sum_{name}_per_process_and_njet"][int(p)][int(n)] += ak.sum(
                    weights[
                        (events.process_id == p) &
                        (results.x.n_central_jets == n) &
                        joinable_mask
                    ],
                )

    return events


@selector(
    uses={boosted_jet_selector, lepton_selection, trigger_selection,
        process_ids, increment_stats, attach_coffea_behavior,
        pu_weight, mc_weight, pdf_weights, murmuf_weights,
        cutflow_features,
          },
    produces={
        trigger_selection, lepton_selection, boosted_jet_selector,
        process_ids, increment_stats, attach_coffea_behavior,
        pu_weight, mc_weight, pdf_weights, murmuf_weights,
        cutflow_features,
    },
    sandbox=dev_sandbox("bash::$HBT_BASE/sandboxes/venv_columnar_tf.sh"),
    exposed=True,
)
def boosted(
    self: Selector,
    events: ak.Array,
    stats: defaultdict,
    **kwargs,
) -> tuple[ak.Array, SelectionResult]:

    # ensure coffea behavior
    events = self[attach_coffea_behavior](events, **kwargs)

    # add corrected mc weights
    if self.dataset_inst.is_mc:
        events = self[mc_weight](events, **kwargs)

    results = SelectionResult()
    # trigger selection
    events, trigger_results = self[trigger_selection](events, **kwargs)
    results += trigger_results

    # lepton selection
    events, lepton_results = self[lepton_selection](events, trigger_results, **kwargs)
    results += lepton_results

    # fat jet selections
    events, jet_results = self[boosted_jet_selector](events, trigger_results, lepton_results, **kwargs)
    results += jet_results

    # mc-only functions
    if self.dataset_inst.is_mc:
        # pdf weights
        events = self[pdf_weights](events, **kwargs)

        # renormalization/factorization scale weights
        events = self[murmuf_weights](events, **kwargs)

        # pileup weights
        events = self[pu_weight](events, **kwargs)

    event_sel = reduce(and_, results.steps.values())
    results.main["event"] = event_sel

    results.steps.all_but_bjet = reduce(
        and_,
        [mask for step_name, mask in results.steps.items() if step_name != "bjet"],
    )

    # create process ids
    events = self[process_ids](events, **kwargs)

    # increment stats
    events = self[increment_stats](events, results, stats, **kwargs)

    # some cutflow features
    events = self[cutflow_features](events, **kwargs)

    return events, results
