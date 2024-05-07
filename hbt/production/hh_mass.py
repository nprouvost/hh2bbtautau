import functools
from columnflow.production import Producer, producer
from columnflow.util import maybe_import
from columnflow.columnar_util import EMPTY_FLOAT, set_ak_column
from columnflow.production.util import attach_coffea_behavior
from columnflow.production.categories import category_ids
from columnflow.production.normalization import normalization_weights

np = maybe_import("numpy")
ak = maybe_import("awkward")

set_ak_column_f32 = functools.partial(set_ak_column, value_type=np.float32)


@producer(
    uses=(
        "Tau.*", "Jet.*","HHBJet.*",category_ids,normalization_weights,attach_coffea_behavior,
    ),
    produces={
        "hh_mass",category_ids,normalization_weights,
    },
)
def hh_mass(self: Producer, events: ak.Array, **kwargs) -> ak.Array:
    # category ids
    events = self[category_ids](events, **kwargs)

    events = self[attach_coffea_behavior](
        events,
        collections={"HHBJet": {"type_name": "Jet"}},
        **kwargs,
    )
    # mc-only weights
    if self.dataset_inst.is_mc:
        # normalization weights
        events = self[normalization_weights](events, **kwargs)

        # btag weights
        # events = self[normalized_btag_weights](events, **kwargs)

    # four-vector sum of first two elements of each object collection (possibly fewer)
    diBJet = events.HHBJet.sum(axis=1)
    diTau = events.Tau[:, :2].sum(axis=1)
    hh = diBJet + diTau

    # total number of objects per event
    n_bjets = ak.num(events.HHBJet, axis=1)
    n_taus = ak.num(events.Tau, axis=1)

    # hh mass taking into account only events with at least 2 b-tagged jets and 2 taus
    # (and otherwise substituting a predefined EMPTY_FLOAT value)
    dihiggs_mask = (n_bjets==2) & (n_taus==2)
    dibjets_mask = (n_bjets==2)
    ditau_mask = (n_taus==2)

    # from IPython import embed; embed()
    def save_interesting_properties(
        source: ak.Array,
        target_column: str,
        column_values: ak.Array,
        mask: ak.Array[bool],
    ):
        return set_ak_column_f32(
            source, target_column, 
            ak.where(mask, column_values, EMPTY_FLOAT)
        )
    
    # write out the resulting mass to the `events` array,
    events = save_interesting_properties(events, "hh.mass", hh.mass, dihiggs_mask)
    events = save_interesting_properties(events, "hh.eta", hh.eta, dihiggs_mask)
    events = save_interesting_properties(events, "hh.pt", hh.pt, dihiggs_mask)

    events = save_interesting_properties(events, "diBJet.pt", diBJet.pt, dibjets_mask)
    events = save_interesting_properties(events, "diBJet.eta", diBJet.eta, dibjets_mask)
    events = save_interesting_properties(events, "diBJet.pt", diBJet.pt, dibjets_mask)

    events = save_interesting_properties(events, "diTau.pt", diTau.pt, ditau_mask)
    events = save_interesting_properties(events, "diTau.eta", diTau.eta, ditau_mask)
    events = save_interesting_properties(events, "diTau.pt", diTau.pt, ditau_mask)

    # return the events
    return events

