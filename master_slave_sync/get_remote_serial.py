import os
import sys
from subprocess import Popen
import read_zone

class GetRemoteSerial(object):
    def getRemoteSerial(self, zonename, ip):
	process = Popen("./get_remote_serial.sh %s %s" % (str(zonename), str(ip)), shell = True)
	process.wait()
	serial = 0
	getSerial = read_zone.GeneDict()
	for fields in getSerial.read_file_data("/tmp/record.txt"):
   	    serial = fields[6]
	os.system('rm /tmp/record.txt')
	return serial


