#!/usr/bin/python

import os
import sys
from subprocess import Popen
import read_file
import get_master_serial
import get_remote_serial

masterSerial = get_master_serial.GetMasterSerial()
geneDict = read_file.GeneDict()
remoteSerial = get_remote_serial.GetRemoteSerial()

for fieldsCfg in geneDict.read_file_data("../cfg_runtime_zones.list"):
    cfg_zone_name = fieldsCfg[0]
    cfg_group_name = fieldsCfg[1]
    zonepath = "../zonefile/" + cfg_zone_name + "zone"
    serial = masterSerial.getMasterSerial(zonepath)
    for fieldsNs in geneDict.read_file_data("../ns.list"):
	ns_group_name = fieldsNs[0]
	ns_role = fieldsNs[1]
	ns_ip = fieldsNs[2]

	'''
	compare with master
	'''
	if ns_role == "master":
	    serial_master = remoteSerial.getRemoteSerial(cfg_zone_name, ns_ip)
	    if int(serial_master) == 0:
		print("MASTER: master hasn't this zone record, so add this zone.")
		print("MASTER: Zone name is %s." % str(cfg_zone_name))
		process = Popen("../add_zone.sh %s %s %s %s" % (str(cfg_zone_name), str(zonepath), \
			str(cfg_group_name), str(serial)), shell = True)
	    
	    if int(serial) < int(serial_master):
		print("MASTER: master serial is greater than the serial stargate gives, so delete zone, then add it.")
		print("MASTER: Zone name is %s." % str(cfg_zone_name))
		process = Popen("../del_zone.sh %s %s %s %s" % (str(cfg_zone_name), str(zonepath), \
			str(cfg_group_name), str(serial)), shell = True)
		process = Popen("../add_zone.sh %s %s %s %s" % (str(cfg_zone_name), str(zonepath), \
			str(cfg_group_name), str(serial)), shell = True)
	   
	    if int(serial) == int(serial_master):
		print("MASTER: master serial is equal to the serial stargate gives, so this is ok.")
		continue
	 
	    if int(serial) > int(serial_master):
		print("MASTER: master serial is less than the serial stargate gives, so reloads the zone.")
		print("MASTER: Zone name is %s." % str(cfg_zone_name))
		process = Popen("../reload_zone.sh %s %s %s %s" % (str(cfg_zone_name), str(zonepath), \
			str(cfg_group_name), str(serial)), shell = True)
		
	
	'''
	compare with slave
	'''
	if ns_role == "slave":
	    serial_slave = remoteSerial.getRemoteSerial(cfg_zone_name, ns_ip)
	    if int(serial_slave) == 0:
		print("SLAVE: master hasn't this zone record, so add this zone.")
		print("SLAVE: Zone name is %s." % str(cfg_zone_name))
		process = Popen("../add_remote_zone.sh %s %s %s %s %s %d" % (str(cfg_zone_name), str(zonepath), \
			str(cfg_group_name), str(serial), str(ns_ip), 8952), shell = True)
	  
	    if int(serial) < int(serial_slave):
		print("SLAVE: master serial is greater than the serial stargate gives, so delete zone, then add it.")
		print("SLAVE: Zone name is %s." % str(cfg_zone_name))
		process = Popen("../del_remote_zone.sh %s %s %s %s %s %d" % (str(cfg_zone_name), str(zonepath), \
			str(cfg_group_name), str(serial), str(ns_ip), 8952), shell = True)
		process = Popen("../add_remote_zone.sh %s %s %s %s %s %d" % (str(cfg_zone_name), str(zonepath), \
			str(cfg_group_name), str(serial), str(ns_ip), 8952), shell = True)
	    
	    if int(serial) == int(serial_slave):
		print("SLAVE: master serial is equal to the serial stargate gives, so this is ok.")
		continue
	    
	    if int(serial) > int(serial_slave):
		print("SLAVE: master serial is less than the serial stargate gives, so reloads the zone.")
		print("SLAVE: Zone name is %s." % str(cfg_zone_name))
		process = Popen("../reload_zone.sh %s %s %s %s" % (str(cfg_zone_name), str(zonepath), \
			str(cfg_group_name), str(serial)), shell = True)
