import read_zone

class GetMasterSerial(object):
    def getMasterSerial(self, zonepath):
	geneDict = read_zone.GeneDict()
	for fields in geneDict.read_file_data(zonepath):
	    serial = fields[6]
	return serial

