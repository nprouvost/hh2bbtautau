# coding: utf-8

"""
Wrappers for some default sets of producers.
"""

from columnflow.production import Producer, producer
from columnflow.production.normalization import normalization_weights
from columnflow.production.categories import category_ids
from columnflow.util import maybe_import
from hbt.production.hh_mass import hh_mass
from hbt.production.btag import normalized_btag_weights
# from columnflow.production.cms.electron import electron_weights
# from columnflow.production.cms.muon import muon_weights
# from hbt.production.features import features
# from hbt.production.weights import normalized_pu_weight, normalized_pdf_weight, normalized_murmuf_weight
# from hbt.production.tau import tau_weights, trigger_weights

ak = maybe_import("awkward")


@producer(
    uses={
        category_ids, hh_mass,
    },
    produces={
        category_ids, hh_mass,
    },
)
def empty(
    self: Producer,
    events: ak.Array,
    **kwargs,
) -> ak.Array:
    # category ids
    events = self[category_ids](events, **kwargs)

    # mc-only weights
    if self.dataset_inst.is_mc:
        # normalization weights
        events = self[normalization_weights](events, **kwargs)

        # btag weights
        # events = self[normalized_btag_weights](events, **kwargs)
    # di-higgs mass
    # from IPython import embed; embed()
    events = self[hh_mass](events, **kwargs)

    return events
