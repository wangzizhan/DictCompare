import os
import sys
import compare_stargate_master

print('cfg_runtime_zones.list')
os.system('cat cfg_runtime_zones.list')
sync = compare_stargate_master.CheckCfgNsd()
sync.checkCfgNsd()
