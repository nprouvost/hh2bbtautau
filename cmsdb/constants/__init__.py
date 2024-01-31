# coding: utf-8

"""
Scientific constants.
"""

from scinum import Number, Correlation

from cmsdb.util import DotDict


# misc
n_leps = Number(3)

# masses
m_z = Number(91.1876, {"z_mass": 0.0021})

# branching ratios
br_w = DotDict()
br_w["had"] = Number(0.6741, {"br_w_had": 0.0027})
br_w["lep"] = 1 - br_w.had

br_ww = DotDict(
    fh=br_w.had ** 2,
    dl=br_w.lep ** 2,
    sl=2 * ((br_w.had * Correlation(br_w_had=-1)) * br_w.lep),
)

br_z = DotDict(
    qq=Number(0.69911, {"br_z_qq": 0.00056}),
    clep=Number(0.033658, {"br_z_clep": 0.000023}) * n_leps,
)

br_h = DotDict(
    ww=Number(0.2152, {"br_h_ww": (0.0153j, 0.0152j)}),
    zz=Number(0.02641, {"br_h_zz": (0.0153j, 0.0152j)}),
    gg=Number(0.002270, {"br_h_gg": (0.0205j, 0.0209j)}),
    bb=Number(0.5809, {"br_h_bb": (0.0124j, 0.0126j)}),
    tt=Number(0.06256, {"br_h_tt": (0.0165j, 0.0163j)}),
)

br_hh = DotDict(
    bbbb=br_h.bb ** 2,
    bbvv=2 * br_h.bb * (br_h.ww + br_h.zz),
    bbww=2 * br_h.bb * br_h.ww,
    bbzz=2 * br_h.bb * br_h.zz,
    bbtt=2 * br_h.bb * br_h.tt,
    bbgg=2 * br_h.bb * br_h.gg,
    ttww=2 * br_h.tt * br_h.ww,
    ttzz=2 * br_h.tt * br_h.zz,
    tttt=br_h.tt ** 2,
    wwww=br_h.ww ** 2,
    zzzz=br_h.zz ** 2,
    wwzz=2 * br_h.ww * br_h.zz,
    wwgg=2 * br_h.ww * br_h.gg,
)
