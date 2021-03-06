import re
class GeneDict(object):
    def read_file_data(self, filepath):
	f = open(filepath, 'r')
	for line in f:
	    try:
       	        line = line[:-1]
		if not line: continue
	    except:
		continue
	    
	    try:
		#fields = line.split(sep)
		fields = re.split(r'(?:\s)\s*', line)
	    except:
		continue
	    yield fields #a generator
	f.close()
	
    def map_fields_dict_schema(self, fields):
	dict_schema = {"zone":0, "group":1}
	pdict = {}
	for fstr, findex in dict_schema.iteritems():
	    pdict[fstr] = str(fields[int(findex)])
	return pdict 
