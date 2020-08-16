import cfg

cfg.initpos["busybeaver22"] = int(cfg.NUM_LEDS / 2)
cfg.initstate["busybeaver22"] = "A"
cfg.initsymbol["busybeaver22"] = "0"
cfg.machines["busybeaver22"] = {
  "A0":["1", "R", "B"],
  "A1":["1", "L", "B"],
  "B0":["1", "L", "A"], 
  "B1":["1", "R", "H"],
  "dummy":["0", "R", "H"]
}

cfg.initpos["busybeaver32"] = int(cfg.NUM_LEDS / 2)
cfg.initstate["busybeaver32"] = "A"
cfg.initsymbol["busybeaver32"] = "0"
cfg.machines["busybeaver32"] = {
  "A0":["1", "R", "B"],
  "A1":["1", "R", "H"],
  "B0":["1", "L", "B"], 
  "B1":["0", "R", "C"],
  "C0":["1", "L", "C"], 
  "C1":["1", "L", "A"]
}

cfg.initpos["busybeaver42"] = int(cfg.NUM_LEDS / 2)
cfg.initstate["busybeaver42"] = "A"
cfg.initsymbol["busybeaver42"] = "0"
cfg.machines["busybeaver42"] = {
  "A0":["1", "R", "B"],
  "A1":["1", "L", "B"],
  "B0":["1", "L", "A"], 
  "B1":["0", "L", "C"],
  "C0":["1", "R", "H"], 
  "C1":["1", "L", "D"],
  "D0":["1", "R", "D"], 
  "D1":["0", "R", "A"]
}

cfg.initpos["busybeaver23"] = int(cfg.NUM_LEDS / 2)
cfg.initstate["busybeaver23"] = "A"
cfg.initsymbol["busybeaver23"] = "0"
cfg.machines["busybeaver23"] = {
  "A0":["1", "R", "B"],
  "A1":["2", "L", "B"],
  "A2":["1", "R", "H"], 
  "B0":["2", "L", "A"], 
  "B1":["2", "R", "B"],
  "B2":["1", "L", "B"],
  "dummy":["0", "R", "H"]
}
