#!/usr/bin/python3 

import sys
import math

sys.path.insert(0,'..') #search in parent folder for modules

import ipTools
import ipTransforms

address=''
while not ipTools.verifyIPv4(address):
    address=input('host address:')

subnetMask=''
while not (ipTools.verifyIPv4(subnetMask) and ipTransforms.isValidSubnetMask(subnetMask)):
    subnetMask=input('Subnet mask:')

subnetAddr=ipTransforms.subnetIPv4(address,subnetMask)
print('\nSubnet address is {}\n'.format(subnetAddr))

maxWild= ipTransforms.binInverse( ipTransforms.IPv4ToInt(subnetMask) )
maxWildStr= ipTransforms.intToIPv4(maxWild)

print('number of mask bits:',32-int(math.log2(maxWild+1)),'\n')
print('max number of subnet addresses is', maxWild-1,'\n')
print('maximum possible wildcard mask is %s\n'%(maxWildStr))

answer='k'
while answer not in 'ynYN':
    answer=input('Would you like to choose another wildcard mask(y/n)?')

if answer=='y':
    userWildStr=''
    userWild=0
    #must be a valid ip address and have a subset of the set bits of max Wildcard
    while not ( ipTools.verifyIPv4(userWildStr) and userWild>0 and (userWild & maxWild)==userWild):
        userWildStr=input('Please insert a valid wildcard mask:')
    userWild=ipTransforms.IPv4ToInt(userWildStr)
else:
    userWild=maxWild
    userWildStr=maxWildStr

print('Wildcard mask is now:',userWildStr)

answer='k'
while answer not in 'nN':
    print('A random IP address in the subnet using the specified wildcard mask:',
           ipTransforms.randomSubnetIPv4(subnetAddr,userWildStr) )
    answer=input('Would you like to generate another address(y/n)?')
        
