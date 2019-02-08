#!/usr/bin/python3

import aristaCom
import re
import matplotlib.pyplot as pyplot

vals=[]
infile=None

def findLoad( feedback ):
    """accepting the (decoded to utf-8) returned feedback from the top function of an arista switch
        isolate and return the cpu usage percentage"""
    matchres=re.search(r'load average:(\s)*?(\d{1,3}\.\d{1,3})(\s)*,',feedback)
    if matchres==None:
        print('No match found.')
        return 0.
    print(matchres.groups())
    fl= open('ariUsage.dat','a')
    fl.write(matchres.group(2)+'\n')# as a string value 
    fl.close()
    return float(matchres.group(2))

def updateUsage():
    k=infile.read() #read from where we left
    if len(k)>1:
        vals.append(float(k.strip())) #add to values
    plotValues()

def plotValues():
    subplot.clear()
    subplot.plot(vals) #re-create the plot
    pyplot.draw()       
    pyplot.pause(0.0001)#this is needed to obtain interactivity.

infile = open('ariUsage.dat','w')#start file from scratch
infile.close()
infile = open('ariUsage.dat','r')

figure=pyplot.figure()
subplot = figure.add_subplot(1,1,1)#axes will auto-adjust
pyplot.show( block=False )          #the plot will be shown after the first draw()
aristaCom.aristaCom('userfile.txt','addressfile.txt','usagecommands.txt',0,10,False,findLoad,updateUsage,None);
