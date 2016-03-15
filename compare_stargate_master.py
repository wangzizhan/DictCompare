import os
import sys
from subprocess import Popen
import shlex
import gene_dict
import generate

class CheckCfgNsd(object):
    def checkCfgNsd(self):
	'''
	generate compare_file
	'''	
        genefile = generate.GeneFile()
        genefile.geneFile()

	'''
	excute comparison  	
	'''
	checker = None
	geneDict = gene_dict.GeneDict()
	for fieldsCom in geneDict.read_file_data("compare_file", " "):
    	    dict_fields_com = geneDict.map_fields_dict_schema(fieldsCom)
    	    for fieldsCfg in geneDict.read_file_data("cfg_runtime_zones.list", "\t"):
		dict_fields_cfg = geneDict.map_fields_dict_schema(fieldsCfg)
		if (dict_fields_com["zone"] == dict_fields_cfg["zone"]) and (dict_fields_cfg["group"] in dict_fields_com["group"]):
	    	    checker = True
	    	    break
		else:
	            checker = False
    	    if not checker: 
		#compare_file needs to delete dict_fields_com
		print("need to delete")
		print(dict_fields_com)
		zone = dict_fields_com["zone"]
		zone_name = zone + "zone"
		print(zone_name)
		zone_file = "./zonefile/" + zone_name
		print(zone_file)
		group = dict_fields_com["group"].replace("_master", "")
		print(group)
		serial = 1
		process = Popen("../del_zone.sh %s %s %s %d" % (str(zone_name),str(zone_file),str(group),serial), shell = True)
	
	for fieldsCfg in geneDict.read_file_data("cfg_runtime_zones.list", "\t"):
    	    dict_fields_cfg = geneDict.map_fields_dict_schema(fieldsCfg)
    	    for fieldsCom in geneDict.read_file_data("compare_file", " "):
		dict_fields_com = geneDict.map_fields_dict_schema(fieldsCom)
		if (dict_fields_com["zone"] == dict_fields_cfg["zone"]) and (dict_fields_cfg["group"] in dict_fields_com["group"]):
	    	    checker = True
	    	    break
		else:
	    	    checker = False
    	    if not checker:
	    	#compare_file needs to add dict_fields_cfg
		print("need to add")
		print(dict_fields_cfg)
		zone = dict_fields_cfg["zone"]
		zone_name = zone + "zone"
		print(zone_name)
		zone_file = "./zonefile/" + zone_name
		print(zone_file)
		group = dict_fields_cfg["group"]
		print(group)
		serial = 1
		process = Popen("../add_zone.sh %s %s %s %d" % (str(zone_name),str(zone_file),str(group),serial), shell = True)
