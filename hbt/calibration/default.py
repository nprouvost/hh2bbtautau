# coding: utf-8

"""
Calibration methods.
"""

from columnflow.calibration import Calibrator, calibrator
from columnflow.calibration.cms.met import met_phi
from columnflow.calibration.cms.jets import jec, jer
from columnflow.production.cms.mc_weight import mc_weight
from columnflow.production.cms.seeds import deterministic_seeds
from columnflow.util import maybe_import
from columnflow.columnar_util import set_ak_column
from hbt.calibration.tau import tec


ak = maybe_import("awkward")
np = maybe_import("numpy")

# derive calibrators to add settings
jec_nominal = jec.derive("jec_nominal", cls_dict={"uncertainty_sources": [], "data_only": True})
jec_full = jec.derive("jec_nominal", cls_dict={"mc_only": True})


@calibrator(
    uses={
        mc_weight, jec_nominal, jec_full, jer, tec, deterministic_seeds, met_phi,
    },
    produces={
        mc_weight, jec_nominal, jec_full, jer, tec, deterministic_seeds, met_phi,
    },
)
def default(self: Calibrator, events: ak.Array, **kwargs) -> ak.Array:
    if self.dataset_inst.is_mc:
        events = self[mc_weight](events, **kwargs)

    events = self[deterministic_seeds](events, **kwargs)

    if self.dataset_inst.is_data:
        events = self[jec_nominal](events, **kwargs)
    else:
        events = self[jec_full](events, **kwargs)
        events = self[jer](events, **kwargs)

    events = self[met_phi](events, **kwargs)

    if self.dataset_inst.is_mc:
        events = self[tec](events, **kwargs)

    return events


@calibrator(
    uses={
        mc_weight, jec_nominal, jec_full, jer, tec, deterministic_seeds, met_phi,
    },
    produces={
        mc_weight, jec_nominal, jec_full, jer, tec, deterministic_seeds, met_phi, "HLT_Ele25_eta2p1_WPTight_Gsf",
        "HLT_IsoMu22", "HLT_IsoMu22_eta2p1", "HLT_IsoTkMu22", "HLT_IsoTkMu22_eta2p1",
    },
)
def placeholder(self: Calibrator, events: ak.Array, **kwargs) -> ak.Array:
    if self.dataset_inst.is_mc:
        events = self[mc_weight](events, **kwargs)

    events = self[deterministic_seeds](events, **kwargs)

    if self.dataset_inst.is_data:
        events = self[jec_nominal](events, **kwargs)
    else:
        events = self[jec_full](events, **kwargs)
        events = self[jer](events, **kwargs)

    events = self[met_phi](events, **kwargs)

    if self.dataset_inst.is_mc:
        events = self[tec](events, **kwargs)

    # adding placeholder columns for single triggers
    HLT_Ele25_eta2p1_WPTight_Gsf = np.ones(len(events), dtype=bool)
    HLT_IsoMu22 = np.ones(len(events), dtype=bool)
    HLT_IsoMu22_eta2p1 = np.ones(len(events), dtype=bool)
    HLT_IsoTkMu22 = np.ones(len(events), dtype=bool)
    HLT_IsoTkMu22_eta2p1 = np.ones(len(events), dtype=bool)

    events = set_ak_column(events, "HLT_Ele25_eta2p1_WPTight_Gsf", HLT_Ele25_eta2p1_WPTight_Gsf)
    events = set_ak_column(events, "HLT_IsoMu22", HLT_IsoMu22)
    events = set_ak_column(events, "HLT_IsoMu22_eta2p1", HLT_IsoMu22_eta2p1)
    events = set_ak_column(events, "HLT_IsoTkMu22", HLT_IsoTkMu22)
    events = set_ak_column(events, "HLT_IsoTkMu22_eta2p1", HLT_IsoTkMu22_eta2p1)

    return events


@calibrator(
    uses=set(),
    produces=set(),
)
def empty(self: Calibrator, events: ak.Array, **kwargs) -> ak.Array:
    return events
