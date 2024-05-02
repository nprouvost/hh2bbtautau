import functools
from columnflow.production import Producer, producer
from columnflow.util import maybe_import
from columnflow.columnar_util import EMPTY_FLOAT, set_ak_column
from columnflow.production.util import attach_coffea_behavior

np = maybe_import("numpy")
ak = maybe_import("awkward")

set_ak_column_f32 = functools.partial(set_ak_column, value_type=np.float32)


@producer(
    uses=(
        "Tau.pt", "Tau.eta", "Tau.phi", "Tau.mass", "Tau.genPartFlav", "Tau.decayMode", "Jet.*",
    ),
    produces={
        "hh_mass",
    },
)

def hh_mass(self: Producer, events: ak.Array, **kwargs) -> ak.Array:
    # attach coffea behavior for four-vector arithmetic
    events = self[attach_coffea_behavior](
        events,
        collections=[ "Tau", "Jet"],
        **kwargs,
    )

    # four-vector sum of first two elements of each object collection (possibly fewer)
    diJet = events.Jet[:,:2].sum(axis=1)
    diTau = events.Tau[:,:2].sum(axis=1)

    # sum the results to form the di-higgs four-vector
    hh = diJet + diTau

    # total number of objects per event
    n_objects = (ak.num(events.Jet, axis=1) + ak.num(events.Tau, axis=1))

    # hh mass taking into account only events with at least 2 b-tagged jets and 2 taus
    # (and otherwise substituting a predefined EMPTY_FLOAT value)
    hh_mass = ak.where(
        n_objects >= 4,
        hh.mass,
        EMPTY_FLOAT,
    )

   # write out the resulting mass to the `events` array,
    events = set_ak_column_f32(
        events,
        "hh_mass",
        hh_mass,
    )

    # return the events
    return events
