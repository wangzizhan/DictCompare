import os
import sys
from subprocess import Popen
import shlex
import gene_dict
import gene_tmp

class CheckCfgNsd(object):
    def checkCfgNsd(self):
	'''
	generate compare_file
	'''	
        genefile = gene_tmp.GeneFile()
        genefile.geneFile()

	'''
	excute comparison  	
	'''
	checker = None
	geneDict = gene_dict.GeneDict()
	
	'''
	check first time
	'''
	for fieldsCom in geneDict.read_file_data("compare_file"):
    	    dict_fields_com = geneDict.map_fields_dict_schema(fieldsCom)
    	    for fieldsCfg in geneDict.read_file_data("../cfg_runtime_zones.list"):
		dict_fields_cfg = geneDict.map_fields_dict_schema(fieldsCfg)
		if (dict_fields_com["zone"] == dict_fields_cfg["zone"]) and (dict_fields_cfg["group"] in dict_fields_com["group"]):
	    	    checker = True
	    	    break
		else:
	            checker = False
    	    if not checker: 
		#compare_file needs to delete dict_fields_com
		zone = dict_fields_com["zone"]
		zone_name = zone + "zone"
		zone_file = "../zonefile/" + zone_name
		group = dict_fields_com["group"].replace("_master", "")
		serial = 1
		print("nsd_runtime_zones.list needs to delete: %s" % str(zone))
		process = Popen("../del_zone.sh %s %s %s %d" % (str(zone),str(zone_file),str(group),serial), shell = True)
	
	'''
	check again
	'''
	for fieldsCfg in geneDict.read_file_data("../cfg_runtime_zones.list"):
    	    dict_fields_cfg = geneDict.map_fields_dict_schema(fieldsCfg)
    	    for fieldsCom in geneDict.read_file_data("compare_file"):
		dict_fields_com = geneDict.map_fields_dict_schema(fieldsCom)
		if (dict_fields_com["zone"] == dict_fields_cfg["zone"]) and (dict_fields_cfg["group"] in dict_fields_com["group"]):
	    	    checker = True
	    	    break
		else:
	    	    checker = False
    	    if not checker:
	    	#compare_file needs to add dict_fields_cfg
		zone = dict_fields_cfg["zone"]
		zone_name = zone + "zone"
		zone_file = "../zonefile/" + zone_name
		group = dict_fields_cfg["group"]
		serial = 1
		print("nsd_runtime_zones.list needs to add: %s" % str(zone))
		process = Popen("../add_zone.sh %s %s %s %d" % (str(zone),str(zone_file),str(group),serial), shell = True)
