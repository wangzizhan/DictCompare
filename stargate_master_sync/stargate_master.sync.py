#!/usr/bin/python

import os
import sys
import compare_stargate_master

sync = compare_stargate_master.CheckCfgNsd()
sync.checkCfgNsd()
