#!/usr/bin/python3

import sys
sys.path.insert(0,'..')

import fileTools
import ipTools
import sshConnect
import threadTools

def aristaCom(userFile,hostFile,cmdFile,cycles,delay,showfeedback,sshfeedbackAction,loopEndAction,finalAction):
    """3 file names, number of cycles to perform, 0 is infinite, delay between cycles
        feedback/silent, action to send to ssh connection thread function, action to perform
        after cycles have been performed."""

    credentials=[]
    hosts=[]
    commands=[]

    if userFile=='':
        userFile = input('Which file contains user credentials?')
    if hostFile=='':
        hostFile = input('Host IP address file:')
    if cmdFile=='':
        cmdFile = input('Arista switch commands file:')

    if not (fileTools.readByLines(userFile,credentials) and 
       fileTools.readByLines(hostFile,hosts) and
       fileTools.readByLines(cmdFile,commands)):
        print('Failed to read config files, exiting...')
        return False

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

    if cycles==0:
        step=0
    else:
        step=1
        cycles-=1
    try:
        while cycles>=0:
            threads=threadTools.startThreads(sshConnect.sshConnect,hosts,[credentials,commands,showfeedback,sshfeedbackAction])
            threadTools.waitThreads(threads)
            if loopEndAction!=None:
                loopEndAction()
            cycles-=step

    except KeyboardInterrupt:
        print('Excecution aborted by the user...')

    if finalAction!=None:
        finalAction()
    print('Done')


def execModule():
    aristaCom('','','',1,0,True,None,None,None)

if __name__=="__main__":
    execModule()

