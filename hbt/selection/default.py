# coding: utf-8

"""
Empty selectors + trigger selection
"""

from operator import and_
from functools import reduce
from collections import defaultdict

from columnflow.selection import Selector, SelectionResult, selector
from columnflow.selection.stats import increment_stats
from columnflow.production.processes import process_ids
from columnflow.production.categories import category_ids

from columnflow.production.cms.mc_weight import mc_weight
from columnflow.production.util import attach_coffea_behavior
from columnflow.util import maybe_import, dev_sandbox
from hbt.selection.trigger import trigger_selection
from hbt.selection.lepton import lepton_selection
from hbt.production.features import cutflow_features

np = maybe_import("numpy")
ak = maybe_import("awkward")


@selector(
    uses={
        process_ids, mc_weight, increment_stats, cutflow_features, trigger_selection,
        lepton_selection,attach_coffea_behavior, category_ids, 
    },
    produces={
        process_ids, mc_weight, cutflow_features, trigger_selection, 
        lepton_selection,category_ids,
    },
    sandbox=dev_sandbox("bash::$HBT_BASE/sandboxes/venv_columnar_tf.sh"),
    exposed=True,
)
def default(
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

    # prepare the selection results that are updated at every step
    results = SelectionResult()

    # trigger selection
    events, trigger_results = self[trigger_selection](events, **kwargs)
    results += trigger_results

    # lepton selection
    # events, lepton_results = self[lepton_selection](events, trigger_results, **kwargs)
    # results += lepton_results

    # get indices and count selected leptons
    # ele_idx = results.objects.Electron.Electron
    # n_ele = ak.num(events.Electron[ele_idx], axis=1)

    # select events with at least four selected leptons
    # results.steps["two_ele"] = (n_ele) >= 2

    # combined event selection after all steps
    event_sel = reduce(and_, results.steps.values())
    results.event = event_sel

    # write out process/category IDs
    events = self[process_ids](events, **kwargs)
    events = self[category_ids](events, **kwargs)

    # increment stats
    weight_map = {
        "num_events": Ellipsis,
        "num_events_selected": Ellipsis,
    }
    if self.dataset_inst.is_mc:
        weight_map["sum_mc_weight"] = events.mc_weight
        weight_map["sum_mc_weight_selected"] = (events.mc_weight, Ellipsis)

        group_map = {
            # per process
            "process": {
                "values": events.process_id,
                "mask_fn": (lambda v: events.process_id == v),
            },
        }
    events, results = self[increment_stats](
        events,
        results,
        stats,
        weight_map=weight_map,
        group_map=group_map,
        **kwargs,
    )

    return events, results
'''
@default.init
def default_init(self: Selector) -> None:
    """
    Initializes the selector by finding the id of the inclusive category if no hard-coded category
    ids are given on class-level.

    :raises ValueError: If the inclusive category cannot be found.
    """
    # do nothing when category ids are set
    if self.category_ids is not None:
        return

    # find the id of the inclusive category
    if self.inclusive_category_name in self.config_inst.categories:
        self.category_ids = [self.config_inst.categories.get(self.inclusive_category_name).id]
    elif 1 in self.config_inst.categories:
        self.category_ids = [1]
    else:
        raise ValueError(f"could not find inclusive category for {self.cls_name} selector")
'''