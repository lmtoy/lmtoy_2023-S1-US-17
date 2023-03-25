#! /usr/bin/env python
#
#   script generator for project="2021-S1-US-3"
#
#   lmtinfo.py grep US-3 Science Map | awk '{print $2}' | sort


import os
import sys

# in prep of the new lmtoy module
try:
    lmtoy = os.environ['LMTOY']
    sys.path.append(lmtoy)
    from lmtoy import runs
except:
    print("No LMTOY with runs.py")
    sys.exit(0)

project="2023-S1-US-17"

on = {}

on["VIIZw800"] = [ 107356, 107357, 107358, 107361, 107362, 107363,]    # 23/24 mar

pars1 = {}
pars1["VIIZw800"] = "speczoom=104,3"

pars2 = {}
pars2["VIIZw800"] = "srdp=1 admit=0"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2)
