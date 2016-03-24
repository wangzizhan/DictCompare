class GeneFile(object):
    def geneFile(self):
	f = open("../nsd_runtime_zones.list", 'r')
	result = list()
	for line in f.readlines():
    	    if line.startswith('#'):
		continue
    	    if line.startswith("add"):
		line = line.replace("add ", "")
		result.append(line)
	f.close()
	
	'''	
	f1 = open("nsd_runtime_zones.list", 'r')
	for line in f1.readlines():
    	    if line.startswith("del"):
		for index, record in enumerate(result):
	    	    if line.replace("del ","") == record:
			del result[index]
	f.close()
	'''

	open("compare_file", "w+").write("%s" % "\n".join(result))
