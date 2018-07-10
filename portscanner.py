import optparse
import socket
from socket import *

def connScan(tgtHost, tgtPort):
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.connect((tgtHost, tgtPort))
		print '[+]%d/tcp open'% tgtPort
		connSkt.close()
	except:
		print '[-]%d/tcp closed'% tgtPort

def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print "[-] Cannot resolve '%s': Unknown host"% tgtHost
		return
	try:
		tgtName = gethostbyaddr(tgtIP)
		print '\n[+] Scan Results for: ' + tgtName[0]
	except:
		print '\n[+] Scan Results for: ' + tgtIP
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		print 'Scanning port ' + tgtPort
		connScan(tgtHost, int(tgtPort))
#		connScan(tgtHost, tgtPort)

		
def main():
	parser = optparse.OptionParser("usage%prog -H <target Host> -p <target port>")
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-p', dest='tgtPort', type='string', help='specify target port[s] separated by comma')
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	print (options.tgtPort)
	tgtPorts = str(options.tgtPort).split(', ')
	print tgtPorts
	if(tgtHost == None) | (tgtPorts[0] == None):
		 print '[-] You must specify a target host and port[s].'
		 exit(0)
	portScan(tgtHost, tgtPorts)
	 

if __name__ == "__main__":
	main()
	
