import cfg

cfg.initpos["add"] = 0
cfg.initstate["add"] = "findm"
cfg.initsymbol["add"] = "_"
cfg.machines["add"] = {
#  "tape":"_111_1111" + "_" * (NUM_LEDS - 9),
  "findm_":["_", "R", "findm"],
  "findm1":["2", "R", "skipm"],
  "skipm1":["1", "R", "skipm"],
  "skipm_":["_", "R", "skipn"],
  "skipn1":["1", "R", "skipn"],
  "skipn_":["_", "R", "skipa"],
  "skipa1":["1", "R", "skipa"],
  "skipa_":["1", "L", "backa"],
  "backa1":["1", "L", "backa"],
  "backa_":["_", "L", "backn"],
  "backn1":["1", "L", "backn"],
  "backn2":["2", "R", "findn"],
  "backn_":["_", "L", "backmb"],
  "backmb1":["1", "L", "backm"],
  "backmb2":["2", "R", "findmb"],
  "findmb_":["_", "R", "findn"],
  "findn1":["2", "R", "skipn"],
  "backm1":["1", "L", "backm"],
  "backm2":["2", "R", "findm"],
  "backm_":["_", "R", "endrwm"],
  "findn1":["2", "R", "skipn"],
  "findn_":["_", "L", "endrwn"],
  "endrwn2":["1", "L", "endrwn"],
  "endrwn_":["_", "L", "endrwm"],
  "endrwm2":["1", "L", "endrwm"],
  "endrwm_":["_", "R", "H"]
}

# http://www.mlb.co.jp/linux/science/gturing/BinaryAdd.tur
cfg.initpos["addbin"] = 30
cfg.initstate["addbin"] = "skipb"
cfg.initsymbol["addbin"] = "_"
cfg.machines["addbin"] = {
#  "tape":"_" * 30 + "_101_1110" + "_" * (NUM_LEDS - 39),
  "skipb_":["_", "R", "skipb"],
  "skipb0":["0", "R", "skipm"],
  "skipb1":["1", "R", "skipm"],
  "skipm0":["0", "R", "skipm"],
  "skipm1":["1", "R", "skipm"],
  "skipmx":["x", "R", "skipm"],
  "skipmy":["y", "R", "skipm"],
  "skipm_":["_", "R", "skipn"],
  "skipn0":["0", "R", "skipn"],
  "skipn1":["1", "R", "skipn"],
  "skipn_":["_", "L", "getn"],
  "getn0":["_", "L", "backmzero"],
  "getn1":["_", "L", "backmone"],
  "getn_":["_", "L", "end"],
  "backmzero0":["0", "L", "backmzero"],
  "backmzero1":["1", "L", "backmzero"],
  "backmzero_":["_", "L", "getmzero"],
  "getmzero0":["x", "R", "skipm"],
  "getmzero_":["x", "R", "skipm"],
  "getmzero1":["y", "R", "skipm"],
  "getmzerox":["x", "L", "getmzero"],
  "getmzeroy":["y", "L", "getmzero"],
  "backmone0":["0", "L", "backmone"],
  "backmone1":["1", "L", "backmone"],
  "backmone_":["_", "L", "getmone"],
  "getmone0":["y", "R", "skipm"],
  "getmone_":["y", "R", "skipm"],
  "getmone1":["x", "L", "carry"],
  "getmonex":["x", "L", "getmone"],
  "getmoney":["y", "L", "getmone"],
  "carry0":["1", "R", "skipm"],
  "carry_":["1", "R", "skipm"],
  "carry1":["0", "L", "carry"],
  "endx":["0", "L", "end"],
  "endy":["1", "L", "end"],
  "end0":["0", "L", "H"],
  "end1":["1", "L", "H"],
  "end_":["_", "L", "H"]
}


cfg.initpos["mul"] = 0
cfg.initstate["mul"] = "startb"
cfg.initsymbol["mul"] = "_"
cfg.machines["mul"] = {
#  "tape":"_111_1111" + "_" * (NUM_LEDS - 9),
  "startb_":["_", "R", "startb"],
  "startb1":["2", "R", "findnb"],
  "start_":["_", "L", "end"],
  "start1":["2", "R", "findnb"],
  "start2":["2", "R", "start"],
  "findnb1":["1", "R", "findnb"],
  "findnb_":["_", "R", "findn"],
  "findn_":["_", "L", "resetn"],
  "findn2":["2", "R", "findn"],
  "findn1":["2", "R", "writeab"],
  "writeab_":["_", "R", "writea"],
  "writeab1":["1", "R", "writeab"],
  "writea_":["1", "L", "backnbb"],
  "writea1":["1", "R", "writea"],
  "backnbb_":["_", "L", "bfindn"],
  "backnbb1":["1", "L", "backnbb"],
  "bfindn2":["2", "R", "findn"],
  "bfindn1":["1", "L", "bfindn"],
  "resetn2":["1", "L", "resetn"],
  "resetn_":["_", "L", "bfindst"],
  "bfindst_":["_", "R", "start"],
  "bfindst1":["1", "L", "bfindst"],
  "bfindst2":["2", "L", "bfindst"],
  "end2":["1", "L", "end"],
  "end_":["_", "R", "H"]
}

cfg.initpos["div"] = 0
cfg.initstate["div"] = "iniskipb"
cfg.initsymbol["div"] = "_"
cfg.machines["div"] = {
#  "tape":"_" + "1" * 11 +\
#         "_" + "1" * 4 +\
#         "_" * (NUM_LEDS - 17),
  "iniskipb_":["_", "R", "iniskipb"],
  "iniskipb1":["1", "R", "iniskipm"],
  "iniskipm1":["1", "R", "iniskipm"],
  "iniskipm_":["_", "R", "iniskipn"],
  "iniskipn1":["1", "R", "iniskipn"],
  "iniskipn_":["_", "R", "wrazero"],
  "wrazero_":["3", "L", "bskipnb"],
  "bskipnb_":["_", "L", "bskipn"],
  "bskipn1":["1", "L", "bskipn"],
  "bskipn_":["_", "R", "findn"],
  "findn2":["2", "R", "findn"],
  "findn1":["2", "R", "chknend"],
  "chknend1":["1", "L", "noebackn"],
  "chknend_":["_", "L", "endbackn"],
  "noebackn2":["2", "L", "noebackn"],
  "noebackn_":["_", "L", "noebackm"],
  "noebackm2":["2", "R", "wrmak"],
  "noebackm3":["3", "R", "wrmak"],
  "noebackm_":["_", "R", "wrmak"],
  "noebackm1":["1", "L", "noebackm"],
  "wrmak1":["2", "R", "skipm"],
  "wrmak_":["_", "L", "copyrbfind"],
  "skipm1":["1", "R", "skipm"],
  "skipm_":["_", "R", "findn"],
  "endbackn2":["1", "L", "endbackn"],
  "endbackn_":["_", "L", "endbackm"],
  "endbackm1":["1", "L", "endbackm"],
  "endbackm2":["2", "R", "wrsep"],
  "endbackm3":["3", "R", "wrsep"],
  "endbackm_":["_", "R", "wrsep"],
  "wrsep1":["3", "R", "wraskipm"],
  "wrsep_":["_", "L", "copyrbfind"],
  "wraskipm1":["1", "R", "wraskipm"],
  "wraskipm_":["_", "R", "wraskipn"],
  "wraskipn1":["1", "R", "wraskipn"],
  "wraskipn_":["_", "R", "wraskipa"],
  "wraskipa1":["1", "R", "wraskipa"],
  "wraskipa3":["1", "L", "backskipa"],
  "wraskipa_":["1", "L", "backskipa"],
  "backskipa1":["1", "L", "backskipa"],
  "backskipa_":["_", "L", "backskipn"],
  "backskipn1":["1", "L", "backskipn"],
  "backskipn_":["_", "R", "findn"],
  "copyrbfind2":["2", "L", "copyrbfind"],
  "copyrbfind3":["3", "R", "copyrcopy"],
  "copyrbfind_":["_", "R", "copyrcopy"],
  "copyrcopy2":["3", "R", "copyrskipm"],
  "copyrcopy_":["_", "R", "H"],
  "copyrskipm2":["2", "R", "copyrskipm"],
  "copyrskipm_":["_", "R", "copyrskipn"],
  "copyrskipn1":["1", "R", "copyrskipn"],
  "copyrskipn2":["1", "R", "copyrskipn"],
  "copyrskipn_":["_", "R", "copyrskipa"],
  "copyrskipa1":["1", "R", "copyrskipa"],
  "copyrskipa3":["3", "R", "copyrskipa"],
  "copyrskipa_":["_", "R", "copyrskipr"],
  "copyrskipr1":["1", "R", "copyrskipr"],
  "copyrskipr_":["1", "L", "copyrbskipr"],
  "copyrbskipr1":["1", "L", "copyrbskipr"],
  "copyrbskipr_":["_", "L", "copyrbskipa"],
  "copyrbskipa1":["1", "L", "copyrbskipa"],
  "copyrbskipa3":["3", "L", "copyrbskipa"],
  "copyrbskipa_":["_", "L", "copyrbskipn"],
  "copyrbskipn1":["1", "L", "copyrbskipn"],
  "copyrbskipn2":["2", "L", "copyrbskipn"],
  "copyrbskipn_":["_", "L", "copyrbfind"],
}


cfg.initpos["eucrid"] = 0
cfg.initstate["eucrid"] = "iniskipb"
cfg.initsymbol["eucrid"] = "_"
cfg.machines["eucrid"] = {
#  "tape":"_" + "1" * 21 +\
#         "_" + "1" * 15 +\
#         "_" * (NUM_LEDS - 38),
  "iniskipb_":["_", "R", "iniskipb"],
  "iniskipb1":["1", "R", "skipm"],
  "skipm1":["1", "R", "skipm"],
  "skipm_":["_", "R", "findn"],
  "findn2":["2", "R", "findn"],
  "findn1":["2", "R", "chknend"],
  "chknend1":["1", "L", "noebackn"],
  "chknend_":["_", "L", "endbackn"],
  "noebackn2":["2", "L", "noebackn"],
  "noebackn_":["_", "L", "noebackm"],
  "noebackm2":["2", "R", "wrmak"],
  "noebackm3":["3", "R", "wrmak"],
  "noebackm_":["_", "R", "wrmak"],
  "noebackm1":["1", "L", "noebackm"],
  "wrmak1":["2", "R", "skipm"],
  "wrmak_":["_", "L", "copyrbfind"],
  "endbackn2":["1", "L", "endbackn"],
  "endbackn_":["_", "L", "endbackm"],
  "endbackm1":["1", "L", "endbackm"],
  "endbackm2":["2", "R", "wrsep"],
  "endbackm3":["3", "R", "wrsep"],
  "endbackm_":["_", "R", "wrsep"],
  "wrsep1":["3", "R", "chkend"],
  "wrsep_":["_", "L", "copyrbfind"],
  "chkend1":["1", "R", "skipm"],
  "chkend_":["_", "R", "H"],
  "copyrbfind2":["2", "L", "copyrbfind"],
  "copyrbfind3":["3", "R", "copyrcopy"],
  "copyrbfind4":["4", "R", "copyrcopy"],
  "copyrbfind_":["_", "R", "copyrcopy"],
  "copyrcopy2":["4", "R", "copyrskipm"],
  "copyrcopy_":["_", "R", "skipm"],
  "copyrskipm2":["2", "R", "copyrskipm"],
  "copyrskipm_":["_", "R", "copyrskipn"],
  "copyrskipn1":["1", "R", "copyrskipn"],
  "copyrskipn2":["1", "R", "copyrskipn"],
  "copyrskipn_":["_", "R", "copyrskipr"],
  "copyrskipr1":["1", "R", "copyrskipr"],
  "copyrskipr_":["1", "L", "copyrbskipr"],
  "copyrbskipr1":["1", "L", "copyrbskipr"],
  "copyrbskipr_":["_", "L", "copyrbskipn"],
  "copyrbskipn1":["1", "L", "copyrbskipn"],
  "copyrbskipn_":["_", "L", "copyrbfind"],
}