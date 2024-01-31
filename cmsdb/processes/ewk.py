# coding: utf-8

"""
EWK-related process definitions.
"""

__all__ = [
    "dy",
    "dy_lep",
    "dy_lep_m50", "dy_lep_m50_1j", "dy_lep_m50_2j", "dy_lep_m50_3j", "dy_lep_m50_4j",
    "dy_lep_0j", "dy_lep_1j", "dy_lep_2j",
    "dy_lep_m50_ht70to100", "dy_lep_m50_ht100to200", "dy_lep_m50_ht200to400",
    "dy_lep_m50_ht400to600", "dy_lep_m50_ht600to800", "dy_lep_m50_ht800to1200",
    "dy_lep_m50_ht1200to2500", "dy_lep_m50_ht2500",
    "dy_lep_pt0To50", "dy_lep_pt50To100", "dy_lep_pt100To250", "dy_lep_pt250To400",
    "dy_lep_pt400To650", "dy_lep_pt650",
    "w",
    "w_lnu",
    "w_lnu_ht70To100", "w_lnu_ht100To200", "w_lnu_ht200To400", "w_lnu_ht400To600",
    "w_lnu_ht600To800", "w_lnu_ht800To1200", "w_lnu_ht1200To2500", "w_lnu_ht2500",
    "ewk",
    "ewk_wp_lnu_m50", "ewk_wm_lnu_m50", "ewk_z_ll_m50",
    "vv",
    "zz", "zz_qqll_m4", "zz_llnunu", "zz_llll",
    "wz", "wz_lllnu", "wz_qqll_m4",
    "ww", "ww_lnulnu",
    "vvv",
    "zzz", "wzz", "wwz", "www",
]

from order import Process
from scinum import Number

import cmsdb.constants as const


#
# Drell-Yan
#

dy = Process(
    name="dy",
    id=50000,
    label="Drell-Yan",
    xsecs={13: Number(0.1)},  # TODO
)

dy_lep = dy.add_process(
    name="dy_lep",
    id=51000,
    label=rf"{dy.label} ($Z \rightarrow ll$)",
    xsecs={13: Number(0.1)},  # TODO
)

# NNLO cross section, based on:
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeV?rev=27

dy_lep_m50 = dy_lep.add_process(
    name="dy_lep_m50",
    id=51100,
    xsecs={13: const.n_leps * Number(6077.22, {
        "integration": 1.49,
        "scale": 0.02j,
        "pdf": 14.78,
    })},
)

# based on datasets DY{i}JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO)
dy_lep_m50_1j = dy_lep_m50.add_process(
    name="dy_lep_m50_1j",
    id=51111,
    xsecs={13: Number(928.3)},
)

dy_lep_m50_2j = dy_lep_m50.add_process(
    name="dy_lep_m50_2j",
    id=51112,
    xsecs={13: Number(293.6)},
)

dy_lep_m50_3j = dy_lep_m50.add_process(
    name="dy_lep_m50_3j",
    id=51113,
    xsecs={13: Number(86.53)},
)

dy_lep_m50_4j = dy_lep_m50.add_process(
    name="dy_lep_m50_4j",
    id=51114,
    xsecs={13: Number(41.28)},
)

# based on datasets DYJetsToLL_{i}J_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO)
dy_lep_0j = dy_lep.add_process(
    name="dy_lep_0j",
    id=51200,
    xsecs={13: Number(5129.0)},
)

dy_lep_1j = dy_lep.add_process(
    name="dy_lep_1j",
    id=51300,
    xsecs={13: Number(951.5)},
)

dy_lep_2j = dy_lep.add_process(
    name="dy_lep_2j",
    id=51400,
    xsecs={13: Number(361.4)},
)

# based on datasets DYJetsToLL_M-50_HT-{i}to{j}_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8 (Autumn18, LO)
dy_lep_m50_ht70to100 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht70to100",
    id=51121,
    xsecs={13: Number(146.5)},
)

dy_lep_m50_ht100to200 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht100to200",
    id=51122,
    xsecs={13: Number(160.7)},
)

dy_lep_m50_ht200to400 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht200to400",
    id=51123,
    xsecs={13: Number(48.63)},
)

dy_lep_m50_ht400to600 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht400to600",
    id=51124,
    xsecs={13: Number(6.993)},
)

dy_lep_m50_ht600to800 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht600to800",
    id=51125,
    xsecs={13: Number(1.761)},
)

dy_lep_m50_ht800to1200 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht800to1200",
    id=51126,
    xsecs={13: Number(0.8021)},
)

dy_lep_m50_ht1200to2500 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht1200to2500",
    id=51127,
    xsecs={13: Number(0.1937)},
)

dy_lep_m50_ht2500 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht2500",
    id=51128,
    xsecs={13: Number(0.003514)},
)

# based on datasets DYJetsToLL_Pt-{i}To{j}_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO)
dy_lep_pt0To50 = dy_lep.add_process(
    name="dy_lep_pt0To50",
    id=51510,
    xsecs={13: Number(1.0)},  # TODO
)

dy_lep_pt50To100 = dy_lep.add_process(
    name="dy_lep_pt50To100",
    id=51520,
    xsecs={13: Number(398.8)},
)

dy_lep_pt100To250 = dy_lep.add_process(
    name="dy_lep_pt100To250",
    id=51530,
    xsecs={13: Number(93.61)},
)

dy_lep_pt250To400 = dy_lep.add_process(
    name="dy_lep_pt250To400",
    id=51540,
    xsecs={13: Number(3.67)},
)

dy_lep_pt400To650 = dy_lep.add_process(
    name="dy_lep_pt400To650",
    id=51550,
    xsecs={13: Number(0.5)},
)

dy_lep_pt650 = dy_lep.add_process(
    name="dy_lep_pt650",
    id=51560,
    xsecs={13: Number(0.04704)},
)


#
# W boson
#

w = Process(
    name="w",
    id=6000,
    label="W + jets",
    xsecs={13: Number(0.1)},  # TODO
)

# NNLO cross section, based on:
# https://twiki.cern.ch/twiki/bin/view/CMS/StandardModelCrossSectionsat13TeV?rev=27

w_lnu = w.add_process(
    name="w_lnu",
    id=6100,
    label=rf"{w.label} ($W \rightarrow l\nu$)",
    xsecs={13: const.n_leps * Number(20508.9, {
        "scale": (165.7, 88.2),
        "pdf": 770.9,
    })},
)

# LO cross sections, scaled to NNLO
# inclusive cross section based on WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO)
# ht bins based on datasets WJetsToLNu_HT-{i}To{j}_TuneCP5_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO)
w_lnu_ht70To100 = w_lnu.add_process(
    name="w_lnu_ht70To100",
    id=6110,
    xsecs={13: w_lnu.get_xsec(13) * 1264.0 / 53870.0},
)

w_lnu_ht100To200 = w_lnu.add_process(
    name="w_lnu_ht100To200",
    id=6120,
    xsecs={13: w_lnu.get_xsec(13) * 1256.0 / 53870.0},
)

w_lnu_ht200To400 = w_lnu.add_process(
    name="w_lnu_ht200To400",
    id=6130,
    xsecs={13: w_lnu.get_xsec(13) * 335.5 / 53870.0},
)

w_lnu_ht400To600 = w_lnu.add_process(
    name="w_lnu_ht400To600",
    id=6140,
    xsecs={13: w_lnu.get_xsec(13) * 45.25 / 53870.0},
)

w_lnu_ht600To800 = w_lnu.add_process(
    name="w_lnu_ht600To800",
    id=6150,
    xsecs={13: w_lnu.get_xsec(13) * 10.97 / 53870.0},
)

w_lnu_ht800To1200 = w_lnu.add_process(
    name="w_lnu_ht800To1200",
    id=6160,
    xsecs={13: w_lnu.get_xsec(13) * 4.933 / 53870.0},
)

w_lnu_ht1200To2500 = w_lnu.add_process(
    name="w_lnu_ht1200To2500",
    id=6170,
    xsecs={13: w_lnu.get_xsec(13) * 1.16 / 53870.0},
)

# NOTE: Summer20UL16 not available in xsdb, Fall17 cross section is used instead
w_lnu_ht2500 = w_lnu.add_process(
    name="w_lnu_ht2500",
    id=6180,
    xsecs={13: w_lnu.get_xsec(13) * 0.008001 / 53870.0},
)


#
# EWK radiations
#

ewk = Process(
    name="ewk",
    id=7000,
    label="EWK",
    xsecs={13: Number(0.1)},  # TODO
)

ewk_wp_lnu_m50 = ewk.add_process(
    name="ewk_wp_lnu_m50",
    id=7100,
    xsecs={13: Number(0.1)},  # TODO
)

ewk_wm_lnu_m50 = ewk.add_process(
    name="ewk_wm_lnu_m50",
    id=7200,
    xsecs={13: Number(0.1)},  # TODO
)

ewk_z_ll_m50 = ewk.add_process(
    name="ewk_z_ll_m50",
    id=7300,
    xsecs={13: Number(0.1)},  # TODO
)


#
# Di-boson
#

vv = Process(
    name="vv",
    id=8000,
    label="Di-Boson",
    xsecs={13: Number(0.1)},  # TODO
)

zz = vv.add_process(
    name="zz",
    id=8100,
    label="ZZ",
    xsecs={
        # https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v3)
        13: Number(12.13),
    },
)

zz_qqll_m4 = zz.add_process(
    name="zz_qqll_m4",
    id=8110,
    xsecs={13: Number(0.1)},  # TODO
)

zz_llnunu = zz.add_process(
    name="zz_llnunu",
    id=8120,
    xsecs={13: Number(0.1)},  # TODO
)

zz_llll = zz.add_process(
    name="zz_llll",
    id=8130,
    xsecs={13: Number(0.1)},  # TODO
)

wz = vv.add_process(
    name="wz",
    id=8200,
    label="WZ",
    xsecs={
        # https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v3)
        13: Number(25.56),
    },
)

wz_lllnu = wz.add_process(
    name="wz_lllnu",
    id=8210,
    xsecs={13: Number(0.1)},  # TODO
)

wz_qqll_m4 = wz.add_process(
    name="wz_qqll_m4",
    id=8220,
    xsecs={13: Number(0.1)},  # TODO
)

ww = vv.add_process(
    name="ww",
    id=8300,
    label="WW",
    xsecs={
        # https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v3)
        13: Number(75.91),
    },
)

ww_lnulnu = ww.add_process(
    name="ww_lnulnu",
    id=8310,
    xsecs={13: Number(0.1)},  # TODO
)


#
# Triple-boson
#

vvv = Process(
    name="vvv",
    id=9000,
    label="Triple-Boson",
    xsecs={13: Number(0.1)},  # TODO
)

zzz = vvv.add_process(
    name="zzz",
    id=9100,
    xsecs={13: Number(0.1)},  # TODO
)

wzz = vvv.add_process(
    name="wzz",
    id=9200,
    xsecs={13: Number(0.1)},  # TODO
)

wwz = vvv.add_process(
    name="wwz",
    id=9300,
    xsecs={13: Number(0.1)},  # TODO
)

www = vvv.add_process(
    name="www",
    id=9400,
    xsecs={13: Number(0.1)},  # TODO
)
