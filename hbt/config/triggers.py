# coding: utf-8

"""
Definition of triggers
"""

import order as od

from hbt.config.util import Trigger, TriggerLeg

# 2016 triggers as per AN of CMS-HIG-20-010 (AN2018_121_v11-1)

def add_triggers_2016(config: od.Config) -> None:
    """
    Adds all triggers to a *config*. For the conversion from filter names to trigger bits, see
    https://github.com/cms-sw/cmssw/blob/master/PhysicsTools/NanoAOD/python/triggerObjects_cff.py.
    """
    config.x.triggers = od.UniqueObjectIndex(Trigger, [
        #
        # e tauh (NO Triggers in AN)
        # used the triggers from https://twiki.cern.ch/twiki/bin/view/CMS/TauTrigger#Tau_Triggers_in_NanoAOD_2016  
        Trigger(
            name="HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1",
            id=710,  ######## TO DO 
            legs=[
                TriggerLeg(
                    pdg_id=11,
                    min_pt=26.0,  ######## TO DO 
                    # filter names:
                    # 
                    trigger_bits=None,  ######## TO DO 
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=22.0,  ######## TO DO 
                    # filter names:
                    #
                    trigger_bits=None,  ######## TO DO 
                ),
            ],
            tags={"cross_trigger", "cross_e_tau", "channel_e_tau"},
        ),
        Trigger(
            name="HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20",
            id=711,  ######## TO DO 
            legs=[
                TriggerLeg(
                    pdg_id=11,
                    min_pt=26.0,  ######## TO DO 
                    # filter names:
                    # 
                    trigger_bits=None,  ######## TO DO 
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=22.0,  ######## TO DO 
                    # filter names:
                    #
                    trigger_bits=None,  ######## TO DO 
                ),
            ],
            tags={"cross_trigger", "cross_e_tau", "channel_e_tau"},
        ),
        Trigger(
            name="HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30",
            id=712,  ######## TO DO 
            legs=[
                TriggerLeg(
                    pdg_id=11,
                    min_pt=26.0,  ######## TO DO 
                    # filter names:
                    # 
                    trigger_bits=None,  ######## TO DO 
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt=32.0,  ######## TO DO 
                    # filter names:
                    #
                    trigger_bits=None,  ######## TO DO 
                ),
            ],
            tags={"cross_trigger", "cross_e_tau", "channel_e_tau"},
        ),

        #
        # mu tauh
        #
        Trigger(
            name="HLT_IsoMu19_eta2p1_LooseIsoPFTau20",
            id=706, ######## TO DO 
            legs=[
                TriggerLeg(
                    pdg_id=13,
                    min_pt= 22, ######## TO DO 
                    # filter names:
                    ######## TO DO 
                    trigger_bits= None, ######## TO DO 
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt= 23, ######## TO DO 
                    # filter names:
                    ######## TO DO
                    trigger_bits= None, ######## TO DO 
                ),
            ],
            tags={"cross_trigger", "cross_mu_tau", "channel_mu_tau"},
        ),
        Trigger(
            name="HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1",
            id=707, ######## TO DO 
            legs=[
                TriggerLeg(
                    pdg_id=13,
                    min_pt= 22, ######## TO DO 
                    # filter names:
                    ######## TO DO 
                    trigger_bits= None, ######## TO DO 
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt= 23, ######## TO DO 
                    # filter names:
                    ######## TO DO
                    trigger_bits= None, ######## TO DO 
                ),
            ],
            tags={"cross_trigger", "cross_mu_tau", "channel_mu_tau"},
        ),

        #
        # tauh tauh
        #
        Trigger(
            name="HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg",
            id=708, ######## TO DO 
            legs=[
                TriggerLeg(
                    pdg_id=15,
                    min_pt= 38, ######## TO DO 
                    # filter names:
                    ######## TO DO 
                    trigger_bits= None, ######## TO DO 
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt= 38, ######## TO DO 
                    # filter names:
                    ####### TO DO 
                    trigger_bits= None, ######## TO DO 
                ),
            ],
            applies_to_dataset=(lambda dataset_inst: dataset_inst.is_mc or dataset_inst.x.era >= "B" and dataset_inst.x.era <= "G"),
            tags={"cross_trigger", "cross_tau_tau", "channel_tau_tau"},
        ),
        Trigger(
            name="HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg",
            id=709, ######## TO DO 
            legs=[
                TriggerLeg(
                    pdg_id=15,
                    min_pt= 38, ######## TO DO 
                    # filter names:
                    ######## TO DO 
                    trigger_bits= None, ######## TO DO 
                ),
                TriggerLeg(
                    pdg_id=15,
                    min_pt= 38, ######## TO DO 
                    # filter names:
                    ######## TO DO 
                    trigger_bits= None, ######## TO DO 
                ),
            ],
            applies_to_dataset=(lambda dataset_inst: dataset_inst.is_mc or dataset_inst.x.era >= "H"),
            tags={"cross_trigger", "cross_tau_tau", "channel_tau_tau"},
        ),

        #
        # vbf  (NO Triggers)
        #
        ''' commenting out single triggers because they do not exist in the NanoAODs ..... 
        #
        # single electron
        #
        Trigger(
            name="HLT_Ele25_eta2p1_WPTight_Gsf", 
            id= 701, ######## TO DO 
            legs=[
                TriggerLeg(
                    pdg_id=11,
                    min_pt= 28, ######## TO DO 
                    # filter names:
                    ######## TO DO
                    trigger_bits= None, ######## TO DO 
                ),
            ],
            tags={"single_trigger", "single_e", "channel_e_tau"},
        ),
        
        #
        # single muon
        #
        Trigger(
            name="HLT_IsoMu22",
            id= 702, ######## TO DO 
            legs=[
                TriggerLeg(
                    pdg_id=13,
                    min_pt= 25, ######## TO DO 
                    # filter names:
                    ######## TO DO 
                    trigger_bits= None, ######## TO DO 
                ),
            ],
            tags={"single_trigger", "single_mu", "channel_mu_tau"},
        ),
        Trigger(
            name="HLT_IsoMu22_eta2p1",
            id= 703, ######## TO DO 
            legs=[
                TriggerLeg(
                    pdg_id=13,
                    min_pt= 25, ######## TO DO 
                    # filter names:
                    ######## TO DO 
                    trigger_bits= None, ######## TO DO 
                ),
            ],
            tags={"single_trigger", "single_mu", "channel_mu_tau"},
        ),
        Trigger(
            name="HLT_IsoTkMu22",
            id= 704, ######## TO DO 
            legs=[
                TriggerLeg(
                    pdg_id=13,
                    min_pt= 25, ######## TO DO 
                    # filter names:
                    ######## TO DO 
                    trigger_bits= None, ######## TO DO 
                ),
            ],
            tags={"single_trigger", "single_mu", "channel_mu_tau"},
        ),
        Trigger(
            name="HLT_IsoTkMu22_eta2p1",
            id= 705, ######## TO DO 
            legs=[
                TriggerLeg(
                    pdg_id=13,
                    min_pt= 25, ######## TO DO 
                    # filter names:
                    ######## TO DO 
                    trigger_bits= None, ######## TO DO 
                ),
            ],
            tags={"single_trigger", "single_mu", "channel_mu_tau"},
        ),
        '''      
    ])
 
def add_triggers_2017(config: od.Config) -> None:
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
 
def add_triggers_2018(config:od.Config) -> None:
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
