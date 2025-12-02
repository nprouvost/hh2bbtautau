# coding: utf-8

import os

import hist

from columnflow.inference import InferenceModel, ParameterType, FlowStrategy  # , ParameterTransformations
from columnflow.inference.cms.datacard import DatacardWriter


class QCDModel(InferenceModel):

    def init_func(self):
        self.add_category(
            "single_category",
            data_from_processes=["tt", "qcd"],  # make up fake data from tt + qcd
            mc_stats=10,  # bb/bb-lite threshold
            empty_bin_value=0.0,  # disables empty bin filling
            flow_strategy=FlowStrategy.warn,  # warn if under/overflow bins have non-zero content
        )

        self.add_process(name="ggHH_kl_1_kt_1_13p6TeV_hbbhtt", is_signal=True)
        self.add_process(name="ggHH_kl_2p45_kt_1_13p6TeV_hbbhtt", is_signal=True)
        self.add_process(name="ggHH_kl_5_kt_1_13p6TeV_hbbhtt", is_signal=True)
        self.add_process(name="tt", is_signal=False)
        self.add_process(name="qcd", is_signal=False)
        self.add_process(name="full_qcd", is_signal=False)

        self.add_parameter("BR_hbb", type=ParameterType.rate_gauss, process=["*_13p6TeV_hbbhtt"], effect=(0.9874, 1.0124))  # noqa: E501
        self.add_parameter("pdf_gg", type=ParameterType.rate_gauss, process="tt", effect=1.042)
        # self.add_parameter("scale_gg", type=ParameterType.shape, process="ggHH_kl_1_kt_1_13p6TeV_hbbhtt", effect=1.06, transformations=ParameterTransformations(["effect_from_rate"]))  # noqa: E501
        self.add_parameter("scale_gg", type=ParameterType.shape, process="ggHH_kl_1_kt_1_13p6TeV_hbbhtt")  # noqa: E501


def create_hist(values, variances, flow=False):
    assert len(values) > (2 if flow else 0)
    assert len(values) == len(variances)
    h = hist.Hist.new.Reg(len(values) - (2 if flow else 0), 0.0, 1.0, name="x").Weight()
    h.view(flow=flow).value[...] = values
    h.view(flow=flow).variance[...] = variances
    return h


# dummy histograms, 2 bins
h_hh = create_hist([0.5, 0.5], [0.1, 0.1])
h_hh_up = create_hist([0.51, 0.55], [0.1, 0.1])
h_hh_down = create_hist([0.45, 0.49], [0.1, 0.1])
h_tt = create_hist([10.0, 0.25], [1.0, 0.1])
h_qcd = create_hist([5.1, 0.0], [0.5, 0.0])
h_full_qcd = create_hist([5.1, 0.25], [0.5, 0.0])

# histogram structure expected by the datacard writer
# category -> process -> config -> shift -> hist
datacard_hists = {
    "single_category": {
        "ggHH_kl_1_kt_1_13p6TeV_hbbhtt": {"22pre_v14": {"nominal": h_hh, ("scale_gg", "up"): h_hh_up, ("scale_gg", "down"): h_hh_down}},  # noqa: E501
        "ggHH_kl_2p45_kt_1_13p6TeV_hbbhtt": {"22pre_v14": {"nominal": h_hh}},
        "ggHH_kl_5_kt_1_13p6TeV_hbbhtt": {"22pre_v14": {"nominal": h_hh}},
        "tt": {"22pre_v14": {"nominal": h_tt}},
        "qcd": {"22pre_v14": {"nominal": h_qcd}},
        "full_qcd": {"22pre_v14": {"nominal": h_full_qcd}},
    },
}

# write it
qcd_model = QCDModel()
writer = DatacardWriter(qcd_model, datacard_hists)
this_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Writing datacard to {this_dir}/datacard.txt")
writer.write(
    os.path.join(this_dir, "datacard.txt"),
    os.path.join(this_dir, "shapes.root"),
    shapes_path_ref="shapes.root",
)
