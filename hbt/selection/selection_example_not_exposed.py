# coding: utf-8

"""
Pt selection methods.
"""

from __future__ import annotations

from columnflow.selection import Selector, SelectionResult, selector
from columnflow.columnar_util import set_ak_column
from columnflow.util import DotDict, maybe_import



np = maybe_import("numpy")
ak = maybe_import("awkward")


@selector(
    uses={
        # nano columns
        "event", "Jet.pt", "Jet.eta", "Jet.phi", "Jet.mass", "Jet.jetId", "Jet.puId"
    },
    # produces={
    #     selection_example_not_exposed
    # },
)
def selection_example_not_exposed(
    self: Selector,
    events: ak.Array,
    **kwargs,
) -> tuple[ak.Array, SelectionResult]:
    """
    Combined lepton selection.
    """
    # get channels from the config
    is_2016 = self.config_inst.campaign.x.year == 2016
    jet_mask=(events.Jet.pt > 200.0)
    sorted_indices = ak.argsort(events.Jet.pt, axis=-1, ascending=False)
    jet_indices = sorted_indices[jet_mask[sorted_indices]]
    jet_sel = (
        (ak.sum(jet_mask, axis=1) >= 1)
    )
    ak4_mask = (
        (events.Jet.jetId == 6) &  # tight plus lepton veto
        ((events.Jet.pt >= 50.0) | (events.Jet.puId == (1 if is_2016 else 4))) #&  # flipped in 2016
        #ak.all(events.Jet.metric_table(lepton_results.x.lepton_pair) > 0.5, axis=2)
    )

    # default jets
    default_mask = (
        ak4_mask &
        (events.Jet.pt > 20.0) &
        (abs(events.Jet.eta) < 2.4)
    )
    # jet_indices = ak.values_astype(ak.fill_none(jet_indices, 0), np.int32)
    return events, SelectionResult(
        steps={
            "selection_example_not_exposed": jet_sel,
        },
        objects={
            "Jet": {
                "Jet": jet_indices,
            },
        },
        aux={
            # save the selected lepton pair for the duration of the selection
            # multiplication of a coffea particle with 1 yields the lorentz vector
            "jet_mask": default_mask
        },
    )
