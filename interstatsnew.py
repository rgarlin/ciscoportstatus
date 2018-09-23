#!/usr/bin/python 

import paramiko
import sys
import os
import subprocess
import socket
import datetime
import re
import time
now = datetime.datetime.now().date()
today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
count = 0
path = '/home/rgarlin/Documents/python-script/connected/'


##fname = raw_input("What is the name of the building:  ")
os.chdir(path)
with open('horms.txt') as f:
    for device in f:
        device = device.strip()
        dssh = paramiko.SSHClient()
        dssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
		dssh.connect(line, username='user', password='pass')
        	stdin, stdout, stderr = dssh.exec_command('sh interface status | in connected')
		mystring =  stdout.readlines()
		##print (mystring)
		for line1 in mystring:
			newline1 = line1[:10] + ',' + line1[10:29] + ',' + line1[29:42]  + ',' + line1[42:53]  + ',' + line1[53:60] + ',' + line1[60:67]  + ',' + line1[67:90]
			line2 = newline1.split(',')
			try:
				os.chdir(path)
				fname = open(line, 'r')
				for linefname in fname:
					line3 = linefname.split(',')
					try:
						if line3[2] == line2[0]:break
					except IndexError:continue
				else:	
					f = open(line, 'a+')
       					f.write(line + ',' +str(now) + ',' + newline1)
					f.close()
					count = count +1
			except IOError:
				for line4 in mystring:
					newline = line4[:10] + ',' + line4[10:29] + ',' + line4[29:42]  + ',' + line4[42:53]  + ',' + line4[53:60] + ',' + line4[60:67]  + ',' + line4[67:90]  
					##print newline
					os.chdir(path)
					f = open(line, 'a+')
                                	f.write(line + ',' + str(now) + ',' + newline)
                                	f.close()
	except paramiko.AuthenticationException:
        	j = open('error.txt', 'a')
		j.write(line + '=== Bad credentials \n')
   		j.close()
	except paramiko.SSHException:
		j = open('error.txt', 'a+')		
		j.write(line + '=== Issues with ssh service \n')
		j.close()
	except socket.error:
		j = open('error.txt', 'a+')		
		j.write(line + '=== Device unreachable\n')
		j.close()       
dssh.close()

endtime = datetime.datetime.now().strftime("%H:%M:%S")

os.chdir(path)
summary = open('dormssummary.txt', 'a+')
summary.write(str(count) + ',' + str(today) + ' , ' + str(endtime) + '\n') 
summary.close() 
