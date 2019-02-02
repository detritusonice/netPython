#!/usr/bin/python3

import sys
import fileTools
import ipTools
import sshConnect
import threadTools

credentials=[]
hosts=[]
commands=[]

userFile = input('Which file contains user credentials?')
hostFile = input('Host IP address file:')
cmdFile = input('Arista switch commands file:')

if not (fileTools.readByLines(userFile,credentials) and 
   fileTools.readByLines(hostFile,hosts) and
   fileTools.readByLines(cmdFile,commands)):
    print('Failed to read config files, exiting...')
    sys.exit()

#print(credentials)
#print(hosts)
#print(commands)

unreachable=[]

for h in hosts:
    print('Trying to reach',h,'...')
    if not ipTools.ping(h):
        unreachable.append(h)
        print('Node %s did not respond.'%(h))
    else:
        print('Node %s reached.'%(h))

for h in unreachable:
    print('removing unreachable host {} from host list'.format(h))
    hosts.remove(h)

print('Starting ssh connection...')
threads=threadTools.startThreads(sshConnect.sshConnect,hosts,[credentials,commands])
threadTools.waitThreads(threads)
print('Done')

