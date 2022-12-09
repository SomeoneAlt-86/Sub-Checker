#/bin/python

import os 

domain = input("Enter domain: ")
cmd1 = "subfinder -d {} -o tempsub.txt".format(domain)
os.system(cmd1)
filename = "tempsub.txt"
with open (filename,'r') as fP:
	for line in fP:
		cmd = "host {}".format(line)
		os.system(cmd)
		print()

os.system("rm tempsub.txt")
print("Finished!")
print("[TIP]- Check for any domains with aliases, check for takeover and get $$")

