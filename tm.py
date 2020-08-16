import sys

import cfg
#global cfg.machines, cfg.initpos, cfg.initstate
import tm_busybeavers
import tm_calc

def tm(machine, tape, headpos, currentstate):
  numsteps = 0
  while True:
    print("step ", numsteps, ":", sep = "")
    for i in range(len(tape)):
      print(tape[i], end = "")
    print()
    for i in range(headpos):
      print(" ", end = "")
    print("^", end = "")
    if currentstate == "H":
      break
    nextsym, nextdir, nextstate = machine[currentstate + tape[headpos]]
    print(currentstate, "=>", nextsym, "/", nextdir, "/", nextstate, sep = "")
    tape = tape[:headpos] + nextsym + tape[headpos + 1:]
    if nextdir == "L":
      headpos = headpos - 1
      if headpos < 0:
        print("head < 0, halt")
        nextstate = "H"
    else:
      headpos = headpos + 1
      if len(tape) <= headpos:
        print(len(tape), "< head, halt")
        nextstate = "H"
    currentstate = nextstate
    numsteps = numsteps + 1
  
  print()
  print("end")
  return


def tmc(tmname):
  if (not tmname in cfg.machines.keys()):
    print(tmname, " not in machines", sep = "")
    exit(199)
  machine = cfg.machines[tmname]
  initsym = cfg.initsymbol[tmname]
  initpos = cfg.initpos[tmname]
  initstate = cfg.initstate[tmname]
  states = []
  symbols = []
  for v in machine.values():
    if not v[0] in symbols:
      symbols.append(v[0])
    if not v[2] in states:
      states.append(v[2])
  symbols.sort()
  if "H" in states:
    states.remove("H")
  else:
    print("warning: H not in states")
  if initstate in states:
    states.remove(initstate)
    states = [initstate] + states
  else:
    print("error: init state ", initstate, " not in states")
    exit(199)

  if initsym in symbols:
    symbols.remove(initsym)
    symbols = [initsym] + symbols
  else:
    print("error: init symbol ", initsym, " not in symbols")
    exit(199)

  print("// machine ", tmname, sep = "")
  print("// symbols: ", symbols, sep = "")
  print("nsymbols = ", len(symbols), sep = "")
  print("// states: ", states, sep = "")
  print("nstates = ", len(states), sep = "")

  stnos = {}
  stno = 0
  for st in states:
    stnos[st] = stno
    stno = stno + 1
  symnos = {}
  symno = 0
  for sym in symbols:
    symnos[sym] = symno
    symno = symno + 1
  ptm = []
  for st in states:
    for sym in symbols:
      if st + sym in machine.keys():
         nextsym, nextdir, nextst = machine[st + sym]
         if not nextsym in symbols or \
            (nextdir != "R" and nextdir != "L") or \
            (not nextst in states and nextst != "H"):
           print("error: machine", st + sym, "=>", machine[st + sym])
           exit(199)
         if nextdir == "R":
           nextdirno = 1
         else:
           nextdirno = -1
         if nextst == "H":
           nextstno = -1
         else:
           nextstno = stnos[nextst]
         ptm.append([stnos[st], symnos[sym],
                    symnos[nextsym], nextdirno, nextstno])
  print("tms_t tm[] =[")
  for p in ptm:
    st, sym, nextsym, nextdir, nextst = p
    print("  {", st, ", ", sym, ", ",
           nextsym, ", ", nextdir, ", ", nextst, "},", sep = "")
  print("  {-1, -1, -1, 0, -1}")
  print("];")

  return


if len(sys.argv) < 2:
  print("usage: tm MACHINE")
  sys.exit(1)

if sys.argv[1] == "-c":
  if len(sys.argv) != 3:
    print("tm -c MACHINENAME|ALL")
    sys.exit(1)
  tmc(sys.argv[2])
  exit(0)

tmname = sys.argv[1]
tape = cfg.initsymbol[tmname] * cfg.NUM_LEDS

if tmname == "busybeaver22" or \
   tmname == "busybeaver32" or \
   tmname == "busybeaver42" or \
   tmname == "busybeaver23":
  if len(sys.argv) != 2:
    print(tmname, ": no args", sep = "")
    sys.exit(2)
 
elif tmname == "mul" or \
     tmname == "div" or \
     tmname == "add" or \
     tmname == "addbin" or \
     tmname == "eucrid":
  if len(sys.argv) != 4:
    print(tmname, ": need 2 args", sep = "")
    sys.exit(2)
  if tmname == "addbin":
    arg1 = bin(int(sys.argv[2]))[2:]
    arg2 = bin(int(sys.argv[3]))[2:]
  else:
    if cfg.NUM_LEDS + 2 <= int(sys.argv[2]) + int(sys.argv[3]):
      print(tmname, ": too long args")
      sys.exit(2)
    arg1 = "1" * int(sys.argv[2])
    arg2 = "1" * int(sys.argv[3])
  pos = cfg.initpos[tmname]
  tape = tape[:1 + pos] + arg1 + \
         tape[1 + pos + len(arg1):1 + pos + len(arg1) + 1] + \
         arg2 + tape[1 + pos + len(arg1) + 1 + len(arg2):]
else:
  print("I don't know machine named", tmname, sep = "")
  sys.exit(1)

tm(cfg.machines[tmname], tape, cfg.initpos[tmname], cfg.initstate[tmname])
sys.exit(0)


