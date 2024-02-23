# coding: utf-8


from columnflow.production import Producer, producer
from columnflow.util import maybe_import
from columnflow.columnar_util import set_ak_column

np = maybe_import("numpy")
ak = maybe_import("awkward")


@producer(
    uses={"Jet.pt"},
    produces={"HT"},
)
def HT_feature(self: Producer, events: ak.Array, **kwargs) -> ak.Array:
    # reconstruct HT and write in the events
    events = set_ak_column(events, "HT", ak.sum(events.Jet.pt, axis=1))

    return events


@producer(
    uses={HT_feature},
    produces={HT_feature, "Jet.pt_squared"},
)
def all_features(self: Producer, events: ak.Array, **kwargs) -> ak.Array:
    # use other producer to create HT column
    events = self[HT_feature](events, **kwargs)

    # create for all jets a column containing the square of the transverse momentum
    events = set_ak_column(events, "Jet.pt_squared", events.Jet.pt * events.Jet.pt)

    return events
