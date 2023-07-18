#! /usr/bin/env python
#
#

import os
import sys

from lmtoy import runs

project="2023-S1-US-17"

on = {}

on["NGC6232"] =  [ 108853, 108854, 108855, 108857, 108858, 108859,]    # 25 apr

on["VIIZw800"] = [ 107356, 107357, 107358, 107361, 107362, 107363,]    # 23/24 mar

pars1 = {}
pars1["NGC6232"]  = "badcb=3/3"
pars1["VIIZw800"] = "speczoom=104,3 badcb=3/3"

pars2 = {}
pars2["NGC6232"]  = "srdp=1 admit=0"
pars2["VIIZw800"] = "srdp=1 admit=0"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2)
