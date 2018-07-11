import os
import platform

def check_ping(hostname):
	response = os.system("ping " +("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ")+ hostname)
	print response
	# and then check the response...

	if response == 0:
		pingstatus = "[+] Network Active"
	else:
		pingstatus = "[-] Network Error"

	return pingstatus

def main():
	ipFile = open('ip.txt')
	for line in ipFile.readlines():
		pingstatus = check_ping(line)
		print pingstatus

if __name__ == "__main__":
	main()
