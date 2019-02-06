#!/usr/bin/python3

import aristaCom
import re

def findLoad( feedback ):
    """accepting the (decoded to utf-8) returned feedback from the top function of an arista switch
        isolate and return the cpu usage percentage"""
    matchres=re.search(r'load average:(\s)*?(\d{1,3}\.\d{1,3})(\s)*,',feedback)
    if matchres==None:
        print('No match found.')
        return 0.
    print(matchres.groups())
    return float(matchres.group(2))

aristaCom.aristaCom('userfile.txt','addressfile.txt','usagecommands.txt',0,10,False,findLoad,None,None);
