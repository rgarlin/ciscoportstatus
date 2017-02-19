#!/usr/bin/python 

import paramiko
import sys
import os
import subprocess
import socket
import datetime
import re

count = 0
now = datetime.datetime.now()

##fname = raw_input("What is the name of the building:  ")
with open('fetch.txt') as f:
    for line in f:
        line = line.strip()
        dssh = paramiko.SSHClient()
        dssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
		dssh.connect(line, username='rancid', password='D@rkM@yo')
        	stdin, stdout, stderr = dssh.exec_command('sh arp | Vlan10')
		mystring =  stdout.readlines()
		##print (mystring)
		for line1 in mystring:
			line2 = line1.split()
			f = open('dormsconnected.txt',  'a+')
       			f.write(line + ' ' +line2[0] + " " +line2[1] + '\n')
			f.close()
	except paramiko.AuthenticationException:
        	j = open('error.txt', 'a')
		j.write(line + '=== Bad credentials')
   		j.close()
	except paramiko.SSHException:
		j = open('error.txt', 'a+')		
		j.write(line + '=== Issues with ssh service')
		j.close()
	except socket.error:
		j = open('error.txt', 'a+')		
		j.write(line + '=== Device unreachable')
		j.close()       
dssh.close()

print "Finished" 






