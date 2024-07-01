# coding: utf-8

"""
Definition of triggers
"""

import order as od

from hbt.config.util import Trigger, TriggerLeg

# 2016 triggers from twiki for tau triggers, cclub marked as comments
# and from cclub for single electron and muon triggers
# cclub link: https://gitlab.cern.ch/cclubbtautau/AnalysisCore/-/blob/main/data/HHtriggers_Run2.json


def add_triggers_2016(config: od.Config, era: str) -> None:
    """
    Adds all triggers to a *config*. For the conversion from filter names to trigger bits, see
    https://github.com/cms-sw/cmssw/blob/master/PhysicsTools/NanoAOD/python/triggerObjects_cff.py.

    -> pinning commit to (probably) nanov12:
    https://github.com/cms-sw/cmssw/blob/7648470aa10c1bf28c0898b92ed902f754455d51/PhysicsTools/NanoAOD/python/triggerObjects_cff.py
    and for changes specifically related to year 2016:
    https://github.com/cms-sw/cmssw/blob/7648470aa10c1bf28c0898b92ed902f754455d51/PhysicsTools/NanoAOD/python/triggerObjects_cff.py#L266C1-L294C1

    or in the last version: (19.06.2024)
    https://github.com/cms-sw/cmssw/blob/9030bf6e5bc33e617ca03ac40e8586ea8b86abc2/PhysicsTools/NanoAOD/python/triggerObjects_cff.py#L280C1-L307C2

    Remark: links to this page in https://twiki.cern.ch/twiki/bin/view/CMS/TauTrigger?rev=101
    were meant for https://github.com/cms-sw/cmssw/blob/b5810c920f0f82de8e7a8fd1a7744e6626cb959b/PhysicsTools/NanoAOD/python/triggerObjects_cff.py # noqa
    but the code has obviously been updated, so lines do not match anymore in newer commits.
    """
    config.x.triggers = od.UniqueObjectIndex(Trigger, [
        #
        # e tauh (NO Triggers in and cclub)
        # used the triggers from https://twiki.cern.ch/twiki/bin/view/CMS/TauTrigger?rev=101#Tau_Triggers_in_NanoAOD_2016 # noqa
        Trigger(
            name="HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1",
            id=710,  # TODO
            legs=[
                TriggerLeg(
                    pdg_id=11,
                    min_pt=24.0,
                    # filter names:
                    # hltOverlapFilterSingleIsoEle24WPLooseGsfLooseIsoPFTau20
                    # (OverlapFilter PFTau)
                    trigger_bits=8,  # 3
                ),
                TriggerLeg(
                    pdg_id=15,
                    # no min_pt for TrigObj in twiki
                    # filter names:
                    # hltPFTau20TrackLooseIso
                    # hltOverlapFilterSingleIsoEle24WPLooseGsfLooseIsoPFTau20
                    # (LooseIso, OverlapFilter IsoEle)
                    trigger_bits=1 + 64,  # 0 + 6
                ),
            ],
            applies_to_dataset=(
                lambda dataset_inst: dataset_inst.is_mc or (dataset_inst.x.era <= "E")
            ),
            run_range=(None, 276214),
            tags={"cross_trigger", "cross_e_tau", "channel_e_tau"},
        ),
        Trigger(
            name="HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20",
            id=711,  # TODO
            legs=[
                TriggerLeg(
                    pdg_id=11,
                    min_pt=24.0,
                    # filter names:
                    # hltOverlapFilterSingleIsoEle24WPLooseGsfLooseIsoPFTau20
                    # (OverlapFilter PFTau)
                    trigger_bits=8,  # 3
                ),
                TriggerLeg(
                    pdg_id=15,
                    # no min_pt for TrigObj in twiki
                    # filter names:
                    # hltPFTau20TrackLooseIso
                    # hltOverlapFilterSingleIsoEle24WPLooseGsfLooseIsoPFTau20
                    # (LooseIso, OverlapFilter IsoEle)
                    trigger_bits=1 + 64,  # 0 + 6
                ),
            ],
            applies_to_dataset=(
                lambda dataset_inst: dataset_inst.is_data and dataset_inst.x.era <= "E"
            ),
            run_range=(276215, 278269),
            tags={"cross_trigger", "cross_e_tau", "channel_e_tau"},
        ),
        Trigger(
            name="HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30",
            id=712,  # TODO
            legs=[
                TriggerLeg(
                    pdg_id=11,
                    min_pt=24.0,
                    # filter names:
                    # hltOverlapFilterSingleIsoEle24WPLooseGsfLooseIsoPFTau20
                    # (OverlapFilter PFTau)
                    trigger_bits=8,  # 3
                ),
                TriggerLeg(
                    pdg_id=15,
                    # no min_pt for TrigObj in twiki
                    # filter names:
                    # hltPFTau20TrackLooseIso
                    # hltOverlapFilterSingleIsoEle24WPLooseGsfLooseIsoPFTau20
                    # (LooseIso, OverlapFilter IsoEle)
                    trigger_bits=1 + 64,  # 0 + 6
                ),
            ],
            applies_to_dataset=(
                lambda dataset_inst: dataset_inst.is_data and dataset_inst.x.era >= "E"
            ),
            run_range=(278270, None),
            tags={"cross_trigger", "cross_e_tau", "channel_e_tau"},
        ),

        #
        # mu tauh
        #

        # # not in twiki, but in analysis, values taken from cclub
        # # -> analysis does not give any filter bits
        # Trigger(
        #     name="HLT_IsoMu19_eta2p1_LooseIsoPFTau20",
        #     id=706,  # TODO
        #     legs=[
        #         TriggerLeg(
        #             pdg_id=13,
        #             min_pt=20,
        #             max_eta=2.1 # not used by trigger selection, to add? # TODO
        #             # filter names:
        #             # TODO
        #             trigger_bits=None,
        #         ),
        #         TriggerLeg(
        #             pdg_id=15,
        #             min_pt=25,
        #             max_eta=2.1 # not used by trigger selection, to add? # TODO
        #             # filter names:
        #             # TODO
        #             trigger_bits=None,
        #         ),
        #     ],
        #     tags={"cross_trigger", "cross_mu_tau", "channel_mu_tau"},
        # ),

        # -> analysis does not give any filter bits
        Trigger(
            name="HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1",
            id=707,  # TODO
            legs=[
                TriggerLeg(
                    pdg_id=13,
                    min_pt=19,  # cclub has min_pt=20,
                    # cclub has max_eta=2.1 # to add to trigger selection? # TODO
                    # filter names:
                    # From Tau? 32 = OverlapFilter IsoMu
                    # From Mu would be expected 4 = OverlapFilter PFTau
                    trigger_bits=32,  # 5  # TODO: check if this trigger lets anything through and if 4 is better
                ),
                TriggerLeg(
                    pdg_id=15,
                    # no min_pt for TrigObj in twiki  # cclub has min_pt=25,
                    # cclub has max_eta=2.1 # to add to trigger selection? # TODO
                    # filter names:
                    # hltPFTau20TrackLooseIso
                    # hltOverlapFilterSingleIsoMu19LooseIsoPFTau20
                    # (LooseIso, OverlapFilter IsoMu)
                    trigger_bits=1 + 32,  # 0 + 5
                ),
            ],
            tags={"cross_trigger", "cross_mu_tau", "channel_mu_tau"},
        ),

        #
        # tauh tauh
        #

        # -> analysis does not give any filter bits
        Trigger(
            name="HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg",
            id=708,  # TODO
            legs=[
                TriggerLeg(
                    pdg_id=15,
                    # no min_pt for TrigObj in twiki  # cclub has min_pt=40,
                    # cclub has max_eta=2.1 # to add to trigger selection? # TODO
                    # filter names:
                    # (Medium(Comb)Iso, Dz)
                    trigger_bits=2 + 256,  # 1 + 8
                ),
                TriggerLeg(
                    pdg_id=15,
                    # no min_pt for TrigObj in twiki  # cclub has min_pt=40,
                    # cclub has max_eta=2.1 # to add to trigger selection? # TODO
                    # filter names:
                    # (Medium(Comb)Iso, Dz)
                    trigger_bits=2 + 256,  # 1 + 8
                ),
            ],
            applies_to_dataset=(lambda dataset_inst: dataset_inst.is_mc or
                (dataset_inst.x.era >= "B" and dataset_inst.x.era <= "G")
            ),
            tags={"cross_trigger", "cross_tau_tau", "channel_tau_tau"},
        ),

        # -> analysis does not give any filter bits
        Trigger(
            name="HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg",
            id=709,  # TODO
            legs=[
                TriggerLeg(
                    pdg_id=15,
                    # no min_pt for TrigObj in twiki  # cclub has min_pt=40,
                    # cclub has max_eta=2.1 # to add to trigger selection? # TODO
                    # filter names:
                    # (Medium(Comb)Iso, Dz)
                    trigger_bits=2 + 256,  # 1 + 8
                ),
                TriggerLeg(
                    pdg_id=15,
                    # no min_pt for TrigObj in twiki  # cclub has min_pt=40,
                    # cclub has max_eta=2.1 # to add to trigger selection? # TODO
                    # filter names:
                    # (Medium(Comb)Iso, Dz)
                    trigger_bits=2 + 256,  # 1 + 8
                ),
            ],
            # should not be applied to mc according to twiki, but analysis uses it???
            # twiki says in era G, but only defined for era H according to cmshltinfo and content of samples
            # -> so, apply only to era H
            applies_to_dataset=(lambda dataset_inst: dataset_inst.is_mc or dataset_inst.x.era >= "H"),
            tags={"cross_trigger", "cross_tau_tau", "channel_tau_tau"},
        ),

        #
        # vbf  (NO Triggers)
        #
    ])

    if era == "pre":
        # single electron and muon trigger from cclub instead of twiki
        #
        # single electron
        #
        # analysis has two legs???
        config.x.triggers.add(
            name="HLT_Ele25_eta2p1_WPTight_Gsf",
            id=701,  # TODO
            legs=[
                TriggerLeg(
                    pdg_id=11,
                    min_pt=28,  # TODO
                    # filter names:
                    # TODO
                    trigger_bits=None,  # TODO
                ),
            ],
            tags={"single_trigger", "single_e", "channel_e_tau"},
        )
        #
        # single muon
        #
        config.x.triggers.add(
            name="HLT_IsoMu22",
            id=702,  # TODO
            legs=[
                TriggerLeg(
                    pdg_id=13,
                    min_pt=25,  # TODO
                    # filter names:
                    # TODO
                    trigger_bits=None,  # TODO
                ),
            ],
            tags={"single_trigger", "single_mu", "channel_mu_tau"},
        )
        config.x.triggers.add(
            name="HLT_IsoMu22_eta2p1",
            id=703,  # TODO
            legs=[
                TriggerLeg(
                    pdg_id=13,
                    min_pt=25,  # TODO
                    # filter names:
                    # TODO
                    trigger_bits=None,  # TODO
                ),
            ],
            tags={"single_trigger", "single_mu", "channel_mu_tau"},
        )
        config.x.triggers.add(
            name="HLT_IsoTkMu22",
            id=704,  # TODO
            legs=[
                TriggerLeg(
                    pdg_id=13,
                    min_pt=25,  # TODO
                    # filter names:
                    # TODO
                    trigger_bits=None,  # TODO
                ),
            ],
            tags={"single_trigger", "single_mu", "channel_mu_tau"},
        )
        config.x.triggers.add(
            name="HLT_IsoTkMu22_eta2p1",
            id=705,  # TODO
            legs=[
                TriggerLeg(
                    pdg_id=13,
                    min_pt=25,  # TODO
                    # filter names:
                    # TODO
                    trigger_bits=None,  # TODO
                ),
            ],
            tags={"single_trigger", "single_mu", "channel_mu_tau"},
        )


def add_triggers_2017(config: od.Config) -> None:
    """
    Adds all triggers to a *config*. For the conversion from filter names to trigger bits, see
    https://github.com/cms-sw/cmssw/blob/master/PhysicsTools/NanoAOD/python/triggerObjects_cff.py.

    in the last version (19.06.2024):
    https://github.com/cms-sw/cmssw/blob/9030bf6e5bc33e617ca03ac40e8586ea8b86abc2/PhysicsTools/NanoAOD/python/triggerObjects_cff.py#L309C1-L335C2
    and
    for v12:
    https://github.com/cms-sw/cmssw/blob/7648470aa10c1bf28c0898b92ed902f754455d51/PhysicsTools/NanoAOD/python/triggerObjects_cff.py#L54C9-L78C11
    for electrons
    and
    https://github.com/cms-sw/cmssw/blob/7648470aa10c1bf28c0898b92ed902f754455d51/PhysicsTools/NanoAOD/python/triggerObjects_cff.py#L106C9-L127C11
    for muons
    """
    config.x.triggers = od.UniqueObjectIndex(Trigger, [
        #
        # single electron
        #
        Trigger(
            name="HLT_Ele32_WPTight_Gsf",
            id=201,
            legs=[
                TriggerLeg(
                    pdg_id=11,
                    min_pt=35.0,
                    # filter names:
                    # hltEle32WPTightGsfTrackIsoFilter
                    trigger_bits=2,
                ),
            ],
            applies_to_dataset=(lambda dataset_inst: dataset_inst.is_mc or dataset_inst.x.era >= "D"),
            tags={"single_trigger", "single_e", "channel_e_tau"},
        ),
        Trigger(
            name="HLT_Ele32_WPTight_Gsf_L1DoubleEG",
            id=202,
            legs=[
                TriggerLeg(
                    pdg_id=11,
                    min_pt=35.0,
                    # filter names:
                    # hltEle32L1DoubleEGWPTightGsfTrackIsoFilter
                    # hltEGL1SingleEGOrFilter
                    trigger_bits=2 + 1024,
                ),
            ],
            tags={"single_trigger", "single_e", "channel_e_tau"},
        ),
        Trigger(
            name="HLT_Ele35_WPTight_Gsf",
            id=203,
            legs=[
                TriggerLeg(
                    pdg_id=11,
                    min_pt=38.0,
                    # filter names:
                    # hltEle35noerWPTightGsfTrackIsoFilter
                    trigger_bits=2,
                ),
            ],
            tags={"single_trigger", "single_e", "channel_e_tau"},
        ),

        #
        # single muon
        #
        Trigger(
            name="HLT_IsoMu24",
            id=101,
            legs=[
                TriggerLeg(
                    pdg_id=13,
                    min_pt=26.0,
                    # filter names:
                    # hltL3crIsoL1sSingleMu22L1f0L2f10QL3f24QL3trkIsoFiltered0p07
                    trigger_bits=2,
                ),
            ],
            tags={"single_trigger", "single_mu", "channel_mu_tau"},
        ),
        Trigger(
            name="HLT_IsoMu27",
            id=102,
            legs=[
                TriggerLeg(
                    pdg_id=13,
                    min_pt=29.0,
                    # filter names:
                    # hltL3crIsoL1sMu22Or25L1f0L2f10QL3f27QL3trkIsoFiltered0p07
                    trigger_bits=2,
                ),
            ],
            tags={"single_trigger", "single_mu", "channel_mu_tau"},
        ),

        #
        # e tauh
        #
        Trigger(
            name="HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
            id=401,
            legs=[
                TriggerLeg(
                    pdg_id=11,
                    min_pt=27.0,
                    # filter names:
                    # hltEle24erWPTightGsfTrackIsoFilterForTau
                    # hltOverlapFilterIsoEle24WPTightGsfLooseIsoPFTau30
                    trigger_bits=2 + 64,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=35.0,
                    # filter names:
                    # hltSelectedPFTau30LooseChargedIsolationL1HLTMatched
                    # hltOverlapFilterIsoEle24WPTightGsfLooseIsoPFTau30
                    trigger_bits=1024 + 256,
                ),
            ],
            tags={"cross_trigger", "cross_e_tau", "channel_e_tau"},
        ),

        #
        # mu tauh
        #
        Trigger(
            name="HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
            id=301,
            legs=[
                TriggerLeg(
                    pdg_id=13,
                    min_pt=22.0,
                    # filter names:
                    # hltL3crIsoL1sMu18erTau24erIorMu20erTau24erL1f0L2f10QL3f20QL3trkIsoFiltered0p07
                    # hltOverlapFilterIsoMu20LooseChargedIsoPFTau27L1Seeded
                    trigger_bits=2 + 64,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=32.0,
                    # filter names:
                    # hltSelectedPFTau27LooseChargedIsolationAgainstMuonL1HLTMatched or
                    # hltOverlapFilterIsoMu20LooseChargedIsoPFTau27L1Seeded
                    trigger_bits=1024 + 512,
                ),
            ],
            tags={"cross_trigger", "cross_mu_tau", "channel_mu_tau"},
        ),

        #
        # tauh tauh
        #
        Trigger(
            name="HLT_DoubleMediumChargedIsoPFTau35_Trk1_eta2p1_Reg",
            id=501,
            legs=[
                TriggerLeg(
                    pdg_id=15,
                    min_pt=40.0,
                    # filter names:
                    # hltDoublePFTau35TrackPt1MediumChargedIsolationAndTightOOSCPhotonsDz02Reg
                    trigger_bits=64,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=40.0,
                    # filter names:
                    # hltDoublePFTau35TrackPt1MediumChargedIsolationAndTightOOSCPhotonsDz02Reg
                    trigger_bits=64,
                ),
            ],
            tags={"cross_trigger", "cross_tau_tau", "channel_tau_tau"},
        ),
        Trigger(
            name="HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
            id=502,
            legs=[
                TriggerLeg(
                    pdg_id=15,
                    min_pt=40.0,
                    # filter names:
                    # hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg
                    trigger_bits=64,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=40.0,
                    # filter names:
                    # hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg
                    trigger_bits=64,
                ),
            ],
            applies_to_dataset=(lambda dataset_inst: dataset_inst.is_data),
            tags={"cross_trigger", "cross_tau_tau", "channel_tau_tau"},
        ),
        Trigger(
            name="HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
            id=503,
            legs=[
                TriggerLeg(
                    pdg_id=15,
                    min_pt=45.0,
                    # filter names:
                    # hltDoublePFTau40TrackPt1MediumChargedIsolationAndTightOOSCPhotonsDz02Reg
                    trigger_bits=64,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=45.0,
                    # filter names:
                    # hltDoublePFTau40TrackPt1MediumChargedIsolationAndTightOOSCPhotonsDz02Reg
                    trigger_bits=64,
                ),
            ],
            applies_to_dataset=(lambda dataset_inst: dataset_inst.is_data),
            tags={"cross_trigger", "cross_tau_tau", "channel_tau_tau"},
        ),
        Trigger(
            name="HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
            id=504,
            legs=[
                TriggerLeg(
                    pdg_id=15,
                    min_pt=45.0,
                    # filter names:
                    # hltDoublePFTau40TrackPt1TightChargedIsolationDz02Reg
                    trigger_bits=64,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=45.0,
                    # filter names:
                    # hltDoublePFTau40TrackPt1TightChargedIsolationDz02Reg
                    trigger_bits=64,
                ),
            ],
            applies_to_dataset=(lambda dataset_inst: dataset_inst.is_data),
            tags={"cross_trigger", "cross_tau_tau", "channel_tau_tau"},
        ),

        #
        # vbf
        #
        Trigger(
            name="HLT_VBF_DoubleLooseChargedIsoPFTau20_Trk1_eta2p1_Reg",
            id=601,
            legs=[
                TriggerLeg(
                    pdg_id=15,
                    min_pt=25.0,
                    # filter names:
                    # hltDoublePFTau20TrackPt1LooseChargedIsolation
                    trigger_bits=2048,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=25.0,
                    # filter names:
                    # hltDoublePFTau20TrackPt1LooseChargedIsolation
                    trigger_bits=2048,
                ),
                # additional leg infos for vbf jets
                TriggerLeg(
                    min_pt=115.0,
                    # filter names:
                    # hltMatchedVBFOnePFJet2CrossCleanedFromDoubleLooseChargedIsoPFTau20
                    trigger_bits=1,
                ),
                TriggerLeg(
                    min_pt=40.0,
                    # filter names:
                    # hltMatchedVBFTwoPFJets2CrossCleanedFromDoubleLooseChargedIsoPFTau20
                    trigger_bits=1,
                ),
            ],
            applies_to_dataset=(lambda dataset_inst: dataset_inst.is_mc or dataset_inst.x.era >= "D"),
            tags={"cross_trigger", "cross_tau_tau_vbf", "channel_tau_tau"},
        ),
    ])


def add_triggers_2018(config: od.Config) -> None:
    config.x.triggers = od.UniqueObjectIndex(Trigger, [
        #
        # single electron
        #
        Trigger(
            name="HLT_Ele32_WPTight_Gsf",
            id=201,
            legs=[
                TriggerLeg(
                    pdg_id=11,
                    min_pt=35.0,
                    # filter names:
                    # hltEle32WPTightGsfTrackIsoFilter
                    trigger_bits=2,
                ),
            ],
            applies_to_dataset=(lambda dataset_inst: dataset_inst.is_mc or dataset_inst.x.era >= "D"),
            tags={"single_trigger", "single_e", "channel_e_tau"},
        ),
        Trigger(
            name="HLT_Ele35_WPTight_Gsf",
            id=203,
            legs=[
                TriggerLeg(
                    pdg_id=11,
                    min_pt=38.0,
                    # filter names:
                    # hltEle35noerWPTightGsfTrackIsoFilter
                    trigger_bits=2,
                ),
            ],
            tags={"single_trigger", "single_e", "channel_e_tau"},
        ),

        #
        # single muon
        #
        Trigger(
            name="HLT_IsoMu24",
            id=101,
            legs=[
                TriggerLeg(
                    pdg_id=13,
                    min_pt=26.0,
                    # filter names:
                    # hltL3crIsoL1sSingleMu22L1f0L2f10QL3f24QL3trkIsoFiltered0p07
                    trigger_bits=2,
                ),
            ],
            tags={"single_trigger", "single_mu", "channel_mu_tau"},
        ),
        Trigger(
            name="HLT_IsoMu27",
            id=102,
            legs=[
                TriggerLeg(
                    pdg_id=13,
                    min_pt=29.0,
                    # filter names:
                    # hltL3crIsoL1sMu22Or25L1f0L2f10QL3f27QL3trkIsoFiltered0p07
                    trigger_bits=2,
                ),
            ],
            tags={"single_trigger", "single_mu", "channel_mu_tau"},
        ),

        #
        # e tauh
        #
        Trigger(
            name="HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
            id=401,
            legs=[
                TriggerLeg(
                    pdg_id=11,
                    min_pt=27.0,
                    # filter names:
                    # hltEle24erWPTightGsfTrackIsoFilterForTau
                    # hltOverlapFilterIsoEle24WPTightGsfLooseIsoPFTau30
                    trigger_bits=2 + 64,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=35.0,
                    # filter names:
                    # hltSelectedPFTau30LooseChargedIsolationL1HLTMatched
                    # hltOverlapFilterIsoEle24WPTightGsfLooseIsoPFTau30
                    trigger_bits=1024 + 256,
                ),
            ],
            # the non-HPS path existed only for data and is fully covered in MC below
            applies_to_dataset=(lambda dataset_inst: dataset_inst.is_data),
            tags={"cross_trigger", "cross_e_tau", "channel_e_tau"},
        ),

        #
        # mu tauh
        #
        Trigger(
            name="HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
            id=301,
            legs=[
                TriggerLeg(
                    pdg_id=13,
                    min_pt=22.0,
                    # filter names:
                    # hltL3crIsoL1sMu18erTau24erIorMu20erTau24erL1f0L2f10QL3f20QL3trkIsoFiltered0p07
                    # hltOverlapFilterIsoMu20LooseChargedIsoPFTau27L1Seeded
                    trigger_bits=2 + 64,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=32.0,
                    # filter names:
                    # hltSelectedPFTau27LooseChargedIsolationAgainstMuonL1HLTMatched or
                    # hltOverlapFilterIsoMu20LooseChargedIsoPFTau27L1Seeded
                    trigger_bits=1024 + 512,
                ),
            ],
            # the non-HPS path existed only for data and is fully covered in MC below
            applies_to_dataset=(lambda dataset_inst: dataset_inst.is_data),
            tags={"cross_trigger", "cross_mu_tau", "channel_mu_tau"},
        ),

        #
        # tauh tauh
        #
        Trigger(
            name="HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
            id=502,
            legs=[
                TriggerLeg(
                    pdg_id=15,
                    min_pt=40.0,
                    # filter names:
                    # hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg
                    trigger_bits=64,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=40.0,
                    # filter names:
                    # hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg
                    trigger_bits=64,
                ),
            ],
            applies_to_dataset=(lambda dataset_inst: dataset_inst.is_data),
            tags={"cross_trigger", "cross_tau_tau", "channel_tau_tau"},
        ),
        Trigger(
            name="HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
            id=503,
            legs=[
                TriggerLeg(
                    pdg_id=15,
                    min_pt=45.0,
                    # filter names:
                    # hltDoublePFTau40TrackPt1MediumChargedIsolationAndTightOOSCPhotonsDz02Reg
                    trigger_bits=64,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=45.0,
                    # filter names:
                    # hltDoublePFTau40TrackPt1MediumChargedIsolationAndTightOOSCPhotonsDz02Reg
                    trigger_bits=64,
                ),
            ],
            applies_to_dataset=(lambda dataset_inst: dataset_inst.is_data),
            tags={"cross_trigger", "cross_tau_tau", "channel_tau_tau"},
        ),
        Trigger(
            name="HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
            id=504,
            legs=[
                TriggerLeg(
                    pdg_id=15,
                    min_pt=45.0,
                    # filter names:
                    # hltDoublePFTau40TrackPt1TightChargedIsolationDz02Reg
                    trigger_bits=64,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=45.0,
                    # filter names:
                    # hltDoublePFTau40TrackPt1TightChargedIsolationDz02Reg
                    trigger_bits=64,
                ),
            ],
            applies_to_dataset=(lambda dataset_inst: dataset_inst.is_data),
            tags={"cross_trigger", "cross_tau_tau", "channel_tau_tau"},
        ),

        #
        # vbf
        #
        Trigger(
            name="HLT_VBF_DoubleLooseChargedIsoPFTau20_Trk1_eta2p1_Reg",
            id=601,
            legs=[
                TriggerLeg(
                    pdg_id=15,
                    min_pt=25.0,
                    # filter names:
                    # hltDoublePFTau20TrackPt1LooseChargedIsolation
                    trigger_bits=2048,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=25.0,
                    # filter names:
                    # hltDoublePFTau20TrackPt1LooseChargedIsolation
                    trigger_bits=2048,
                ),
                # additional leg infos for vbf jets
                TriggerLeg(
                    min_pt=115.0,
                    # filter names:
                    # hltMatchedVBFOnePFJet2CrossCleanedFromDoubleLooseChargedIsoPFTau20
                    trigger_bits=1,
                ),
                TriggerLeg(
                    min_pt=40.0,
                    # filter names:
                    # hltMatchedVBFTwoPFJets2CrossCleanedFromDoubleLooseChargedIsoPFTau20
                    trigger_bits=1,
                ),
            ],
            applies_to_dataset=(lambda dataset_inst: dataset_inst.is_mc or dataset_inst.x.era >= "D"),
            tags={"cross_trigger", "cross_tau_tau_vbf", "channel_tau_tau"},
        ),
    ])


def add_triggers_2022(config: od.Config) -> None:
    """
    Adds all triggers to a *config*. For the conversion from filter names to trigger bits, see
    https://github.com/cms-sw/cmssw/blob/master/PhysicsTools/NanoAOD/python/triggerObjects_cff.py.
    """
    config.x.triggers = od.UniqueObjectIndex(Trigger, [
        #
        # single electron
        #
        Trigger(
            name="HLT_Ele32_WPTight_Gsf",
            id=201,
            legs=[
                TriggerLeg(
                    pdg_id=11,
                    min_pt=33.0,
                    # filter names:
                    # WPTightTrackIso
                    trigger_bits=2,
                ),
            ],
            tags={"single_trigger", "single_e", "channel_e_tau"},
        ),
        Trigger(
            name="HLT_Ele35_WPTight_Gsf",
            id=203,
            legs=[
                TriggerLeg(
                    pdg_id=11,
                    min_pt=36.0,
                    # filter names:
                    # WPTightTrackIso
                    trigger_bits=2,
                ),
            ],
            tags={"single_trigger", "single_e", "channel_e_tau"},
        ),

        #
        # single muon
        #
        Trigger(
            name="HLT_IsoMu24",
            id=101,
            legs=[
                TriggerLeg(
                    pdg_id=13,
                    min_pt=25.0,
                    # filter names:
                    # "Iso", "SingleMuon"
                    trigger_bits=2 + 8,
                ),
            ],
            tags={"single_trigger", "single_mu", "channel_mu_tau"},
        ),
        Trigger(
            name="HLT_IsoMu27",
            id=102,
            legs=[
                TriggerLeg(
                    pdg_id=13,
                    min_pt=28.0,
                    # filter names:
                    # "Iso", "SingleMuon"
                    trigger_bits=2 + 8,
                ),
            ],
            tags={"single_trigger", "single_mu", "channel_mu_tau"},
        ),

        #
        # e tauh
        #
        Trigger(
            name="HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1",
            id=401,
            legs=[
                TriggerLeg(
                    pdg_id=11,
                    min_pt=25.0,
                    # filter names:
                    # OverlapFilterPFTau
                    trigger_bits=8,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=35.0,
                    # filter names:
                    # "DeepTau", "Hps"
                    trigger_bits=8 + 32,
                ),
            ],
            tags={"cross_trigger", "cross_e_tau", "channel_e_tau"},
        ),

        #
        # mu tauh
        #
        Trigger(
            name="HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1",
            id=301,
            legs=[
                TriggerLeg(
                    pdg_id=13,
                    min_pt=21.0,
                    # filter names:
                    # hltL3crIsoL1sMu18erTau24erIorMu20erTau24erL1f0L2f10QL3f20QL3trkIsoFiltered0p07
                    # hltOverlapFilterIsoMu20LooseChargedIsoPFTau27L1Seeded
                    trigger_bits=4,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=32.0,
                    # filter names:
                    # hltSelectedPFTau27LooseChargedIsolationAgainstMuonL1HLTMatched or
                    # hltOverlapFilterIsoMu20LooseChargedIsoPFTau27L1Seeded
                    trigger_bits=8 + 32,
                ),
            ],
            tags={"cross_trigger", "cross_mu_tau", "channel_mu_tau"},
        ),

        #
        # tauh tauh
        #
        Trigger(
            name="HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1",
            id=505,
            legs=[
                TriggerLeg(
                    pdg_id=15,
                    min_pt=40.0,
                    # filter names:
                    # hltDoublePFTau35TrackPt1MediumChargedIsolationAndTightOOSCPhotonsDz02Reg
                    trigger_bits=8 + 32,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=40.0,
                    # filter names:
                    # hltDoublePFTau35TrackPt1MediumChargedIsolationAndTightOOSCPhotonsDz02Reg
                    trigger_bits=8 + 32,
                ),
            ],
            tags={"cross_trigger", "cross_tau_tau", "channel_tau_tau"},
        ),
        Trigger(
            name="HLT_DoubleMediumChargedIsoPFTauHPS40_Trk1_eta2p1",
            id=506,
            legs=[
                TriggerLeg(
                    pdg_id=15,
                    min_pt=45.0,
                    # filter names:
                    # "MediumChargedIso", "Hps", "TightOOSCPhotons"
                    trigger_bits=2 + 32 + 16,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=45.0,
                    # filter names:
                    # "MediumChargedIso", "Hps", "TightOOSCPhotons"
                    trigger_bits=2 + 32 + 16,
                ),
            ],
            applies_to_dataset=(lambda dataset_inst: dataset_inst.is_mc or dataset_inst.x.era >= "E"),
            tags={"cross_trigger", "cross_tau_tau", "channel_tau_tau"},
        ),

        Trigger(
            name="HLT_DoubleMediumChargedIsoDisplacedPFTauHPS32_Trk1_eta2p1",
            id=507,
            legs=[
                TriggerLeg(
                    pdg_id=15,
                    min_pt=45.0,
                    # filter names:
                    # "MediumChargedIso", "Hps", "TightOOSCPhotons"
                    trigger_bits=2 + 32 + 16,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=45.0,
                    # filter names:
                    # "MediumChargedIso", "Hps", "TightOOSCPhotons"
                    trigger_bits=2 + 32 + 16,
                ),
            ],
            applies_to_dataset=(lambda dataset_inst: dataset_inst.is_data and dataset_inst.x.era < "E"),
            tags={"cross_trigger", "cross_tau_tau", "channel_tau_tau"},
        ),

        #
        # vbf
        #
        Trigger(
            name="HLT_VBF_DoubleLooseChargedIsoPFTauHPS20_Trk1_eta2p1",
            id=602,
            legs=[
                TriggerLeg(
                    pdg_id=15,
                    min_pt=25.0,
                    # filter names:
                    # LooseChargedIso", "Hps", "VBFpDoublePFTau_run3"
                    trigger_bits=1 + 32 + 4096,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=25.0,
                    # filter names:
                    # LooseChargedIso", "Hps", "VBFpDoublePFTau_run3"
                    trigger_bits=1 + 32 + 4096,
                ),
                # additional leg infos for vbf jets
                TriggerLeg(  # TODO
                    min_pt=115.0,
                    # filter names:
                    # hltMatchedVBFOnePFJet2CrossCleanedFromDoubleLooseChargedIsoPFTau20
                    trigger_bits=1,
                ),
                TriggerLeg(
                    min_pt=40.0,
                    # filter names:
                    # hltMatchedVBFTwoPFJets2CrossCleanedFromDoubleLooseChargedIsoPFTau20
                    trigger_bits=1,
                ),
            ],
            applies_to_dataset=(lambda dataset_inst: dataset_inst.is_mc and config.has_tag("pre")),
            tags={"cross_trigger", "cross_tau_tau_vbf", "channel_tau_tau"},
        ),

        Trigger(
            name="HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1",
            id=603,
            legs=[
                TriggerLeg(
                    pdg_id=15,
                    min_pt=25.0,
                    # filter names:
                    # LooseChargedIso", "Hps", "VBFpDoublePFTau_run3"
                    trigger_bits=1 + 32 + 4096,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=25.0,
                    # filter names:
                    # LooseChargedIso", "Hps", "VBFpDoublePFTau_run3"
                    trigger_bits=1 + 32 + 4096,
                ),
                # additional leg infos for vbf jets
                TriggerLeg(  # TODO
                    min_pt=115.0,
                    # filter names:
                    # hltMatchedVBFOnePFJet2CrossCleanedFromDoubleLooseChargedIsoPFTau20
                    trigger_bits=1,
                ),
                TriggerLeg(
                    min_pt=40.0,
                    # filter names:
                    # hltMatchedVBFTwoPFJets2CrossCleanedFromDoubleLooseChargedIsoPFTau20
                    trigger_bits=1,
                ),
            ],
            applies_to_dataset=(lambda dataset_inst: dataset_inst.is_data and config.has_tag("pre")),
            tags={"cross_trigger", "cross_tau_tau_vbf", "channel_tau_tau"},
        ),
        #
        # tau tau jet
        #
        Trigger(
            name="HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60",
            id=701,
            legs=[
                TriggerLeg(
                    pdg_id=15,
                    min_pt=35.0,
                    # filter names:
                    # "TightOOSCPhotons", "DiTauAndPFJet"
                    trigger_bits=16 + 16384,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=35.0,
                    # filter names:
                    # "TightOOSCPhotons", "DiTauAndPFJet"
                    trigger_bits=16 + 16384,
                ),
                TriggerLeg(
                    min_pt=65.0,
                    # filter names:
                    # hltMatchedDoubleTau35OnePFJet60CrossCleaned
                    trigger_bits=1,
                ),
            ],
            tags={"cross_trigger", "cross_tau_tau_jet", "channel_tau_tau"},
        ),
        Trigger(
            name="HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75",
            id=702,
            legs=[
                TriggerLeg(
                    pdg_id=15,
                    min_pt=35.0,
                    # filter names:
                    # TightOOSCPhotons", "DiTauAndPFJet
                    trigger_bits=16 + 16384,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=35.0,
                    # filter names:
                    # TightOOSCPhotons", "DiTauAndPFJet
                    trigger_bits=16 + 16384,
                ),
                TriggerLeg(
                    min_pt=80.0,
                    # filter names:
                    # hltMatchedDoubleTau35OnePFJet75CrossCleaned
                    trigger_bits=1,
                ),
            ],
            tags={"cross_trigger", "cross_tau_tau_jet", "channel_tau_tau"},
        ),
    ])


def add_triggers_2023(config: od.Config) -> None:
    """
    Adds all triggers to a *config*. For the conversion from filter names to trigger bits, see
    https://github.com/cms-sw/cmssw/blob/master/PhysicsTools/NanoAOD/python/triggerObjects_cff.py.
    """
    config.x.triggers = od.UniqueObjectIndex(Trigger, [
        #
        # single electron
        #
        Trigger(
            name="HLT_Ele32_WPTight_Gsf",
            id=201,
            legs=[
                TriggerLeg(
                    pdg_id=11,
                    min_pt=33.0,
                    # filter names:
                    # WPTightTrackIso
                    trigger_bits=2,
                ),
            ],
            tags={"single_trigger", "single_e", "channel_e_tau"},
        ),
        Trigger(
            name="HLT_Ele35_WPTight_Gsf",
            id=203,
            legs=[
                TriggerLeg(
                    pdg_id=11,
                    min_pt=36.0,
                    # filter names:
                    # WPTightTrackIso
                    trigger_bits=2,
                ),
            ],
            tags={"single_trigger", "single_e", "channel_e_tau"},
        ),

        #
        # single muon
        #
        Trigger(
            name="HLT_IsoMu24",
            id=101,
            legs=[
                TriggerLeg(
                    pdg_id=13,
                    min_pt=25.0,
                    # filter names:
                    # "Iso", "SingleMuon"
                    trigger_bits=2 + 8,
                ),
            ],
            tags={"single_trigger", "single_mu", "channel_mu_tau"},
        ),
        Trigger(
            name="HLT_IsoMu27",
            id=102,
            legs=[
                TriggerLeg(
                    pdg_id=13,
                    min_pt=28.0,
                    # filter names:
                    # "Iso", "SingleMuon"
                    trigger_bits=2 + 8,
                ),
            ],
            tags={"single_trigger", "single_mu", "channel_mu_tau"},
        ),

        #
        # e tauh
        #
        Trigger(
            name="HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1",
            id=401,
            legs=[
                TriggerLeg(
                    pdg_id=11,
                    min_pt=25.0,
                    # filter names:
                    # OverlapFilterPFTau
                    trigger_bits=8,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=35.0,
                    # filter names:
                    # "DeepTau", "Hps"
                    trigger_bits=8 + 32,
                ),
            ],
            tags={"cross_trigger", "cross_e_tau", "channel_e_tau"},
        ),

        #
        # mu tauh
        #
        Trigger(
            name="HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1",
            id=301,
            legs=[
                TriggerLeg(
                    pdg_id=13,
                    min_pt=21.0,
                    # filter names:
                    # hltL3crIsoL1sMu18erTau24erIorMu20erTau24erL1f0L2f10QL3f20QL3trkIsoFiltered0p07
                    # hltOverlapFilterIsoMu20LooseChargedIsoPFTau27L1Seeded
                    trigger_bits=4,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=32.0,
                    # filter names:
                    # hltSelectedPFTau27LooseChargedIsolationAgainstMuonL1HLTMatched or
                    # hltOverlapFilterIsoMu20LooseChargedIsoPFTau27L1Seeded
                    trigger_bits=8 + 32,
                ),
            ],
            tags={"cross_trigger", "cross_mu_tau", "channel_mu_tau"},
        ),

        #
        # tauh tauh
        #
        Trigger(
            name="HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1",
            id=505,
            legs=[
                TriggerLeg(
                    pdg_id=15,
                    min_pt=40.0,
                    # filter names:
                    # "TightOOSCPhotons", "DiTauAndPFJet"
                    trigger_bits=16 + 16384,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=40.0,
                    # filter names:
                    # "TightOOSCPhotons", "DiTauAndPFJet"
                    trigger_bits=16 + 16384,
                ),
            ],
            tags={"cross_trigger", "cross_tau_tau", "channel_tau_tau"},
        ),

        #
        # tau tau jet
        #
        Trigger(
            name="HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60",
            id=701,
            legs=[
                TriggerLeg(
                    pdg_id=15,
                    min_pt=35.0,
                    # filter names:
                    # "TightOOSCPhotons", "DiTauAndPFJet
                    trigger_bits=16 + 16384,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=35.0,
                    # filter names:
                    # "TightOOSCPhotons", "DiTauAndPFJet
                    trigger_bits=16 + 16384,
                ),
                TriggerLeg(
                    min_pt=65.0,
                    # filter names:
                    # hltMatchedDoubleTau35OnePFJet60CrossCleaned
                    trigger_bits=1,
                ),
            ],
            tags={"cross_trigger", "cross_tau_tau_jet", "channel_tau_tau"},
        ),

        #
        # vbf
        #
        Trigger(
            name="HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1",
            id=602,
            legs=[
                TriggerLeg(
                    pdg_id=15,
                    min_pt=25.0,
                    # filter names:
                    # LooseChargedIso", "Hps", "VBFpDoublePFTau_run3"
                    trigger_bits=1 + 32 + 4096,
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=25.0,
                    # filter names:
                    # LooseChargedIso", "Hps", "VBFpDoublePFTau_run3"
                    trigger_bits=1 + 32 + 4096,
                ),
                # additional leg infos for vbf jets
                TriggerLeg(  # TODO
                    min_pt=115.0,
                    # filter names:
                    # hltMatchedVBFOnePFJet2CrossCleanedFromDoubleLooseChargedIsoPFTau20
                    trigger_bits=1,
                ),
                TriggerLeg(
                    min_pt=40.0,
                    # filter names:
                    # hltMatchedVBFTwoPFJets2CrossCleanedFromDoubleLooseChargedIsoPFTau20
                    trigger_bits=1,
                ),
            ],
            applies_to_dataset=(lambda dataset_inst: dataset_inst.is_mc),
            tags={"cross_trigger", "cross_tau_tau_vbf", "channel_tau_tau"},
        ),
    ])
