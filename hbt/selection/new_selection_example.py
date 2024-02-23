# coding: utf-8

"""
Selection methods.
"""

from operator import and_
from functools import reduce
from collections import defaultdict, OrderedDict

from columnflow.selection import Selector, SelectionResult, selector
from columnflow.production.processes import process_ids
from columnflow.production.cms.mc_weight import mc_weight
from columnflow.production.cms.pileup import pu_weight
from columnflow.production.cms.pdf import pdf_weights
from columnflow.production.cms.scale import murmuf_weights
from columnflow.production.cms.btag import btag_weights
from columnflow.production.util import attach_coffea_behavior
from columnflow.util import maybe_import, dev_sandbox

from hbt.selection.selection_example_not_exposed import selection_example_not_exposed
from hbt.production.features import cutflow_features
from IPython import embed

np = maybe_import("numpy")
ak = maybe_import("awkward")


@selector(
    uses={
        selection_example_not_exposed, mc_weight, pdf_weights, murmuf_weights, pu_weight, btag_weights,
        process_ids, attach_coffea_behavior, cutflow_features,
    },
    produces={
        selection_example_not_exposed, mc_weight, pdf_weights, murmuf_weights, pu_weight, btag_weights, 
        process_ids, attach_coffea_behavior, cutflow_features,
    },
    sandbox=dev_sandbox("bash::$HBT_BASE/sandboxes/venv_columnar_tf.sh"),
    exposed=True,
)
def new_selection_example(
    self: Selector,
    events: ak.Array,
    stats: defaultdict,
    **kwargs,
) -> tuple[ak.Array, SelectionResult]:
    results = SelectionResult()
    if self.dataset_inst.is_mc:
        events = self[mc_weight](events, **kwargs)
    events = self[attach_coffea_behavior](events, **kwargs)
    print("uses", self.uses)
    print("fields", events.fields)
    #embed()
    events, selection_example_not_exposed_results = self[selection_example_not_exposed](events, **kwargs)
    results += selection_example_not_exposed_results

    if self.dataset_inst.is_mc:
        # pdf weights
        events = self[pdf_weights](events, **kwargs)

        # renormalization/factorization scale weights
        events = self[murmuf_weights](events, **kwargs)

        # pileup weights
        events = self[pu_weight](events, **kwargs)

        # btag weights
        #embed()
        events = self[btag_weights](events, results.x.jet_mask, **kwargs)

    event_sel = reduce(and_, results.steps.values())
    results.main["event"] = event_sel
    results.steps.all_but_bjet = reduce(
        and_,
        [mask for step_name, mask in results.steps.items() if step_name != "bjet"],
    )
    stats["n_events"] += len(events)
    stats["n_events_selected"] += ak.sum(event_sel, axis=0)
    #stats["sum_mc_weight"]=10
    #stats["sum_mc_weight_selected"] = 10*stats["n_events_selected"]/stats["n_events"]
    event_mask = results.main.event
    event_mask_no_bjet = results.steps.all_but_bjet

    # create process ids
    events = self[process_ids](events, **kwargs)
    unique_process_ids = np.unique(events.process_id)


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

        # btag weights
        for name in sorted(self[btag_weights].produces):
            if not name.startswith("btag_weight"):
                continue

            # weights for all events
            weight_map[name] = (events[name], Ellipsis)

            # weights for selected events
            weight_map[f"{name}_selected"] = (events[name], event_mask)

            # weights for selected events, excluding the bjet selection
            weight_map[f"{name}_selected_no_bjet"] = (events[name], event_mask_no_bjet)

            # mc weight times btag weight for selected events, excluding the bjet selection
            weight_map[f"mc_weight_{name}_selected_no_bjet"] = (events.mc_weight * events[name], event_mask_no_bjet)

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
            # for n in unique_n_jets:
            #     stats[f"sum_{name}_per_process_and_njet"][int(p)][int(n)] += ak.sum(
            #         weights[
            #             (events.process_id == p) &
            #             (results.x.n_central_jets == n) &
            #             joinable_mask
            #         ],
            #     )
    embed()

    # combined event seleciton after all but the bjet step
    # results.steps.all_but_bjet = reduce(
    #     and_,
    #     [mask for step_name, mask in results.steps.items() if step_name != "bjet"],
    # )
    events = self[cutflow_features](events, **kwargs)
    return events, results

# @new_selection_example.init
# def new_selection_example_init(self: Selector) -> None:
#     if not getattr(self, "dataset_inst", None) or self.dataset_inst.is_data:
#         return

#     # mc only selectors
#     selectors = {mc_weight, pdf_weights, murmuf_weights, pu_weight, btag_weights}
#     self.uses |= selectors
#     self.produces |= selectors
