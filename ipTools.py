import re

def verifyIPv4( address ):
    address.strip()
    result=re.match(r'(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})',address)
    if result==None:
        return False
    for i in range(1,5):
        num=int(result.group(i))
        if num>255:
            return False
    return True

def ping( address ):
    import subprocess
    cplProc=subprocess.run(["ping",address,"-c 4"],stdout=subprocess.DEVNULL)
    return cplProc.returncode==0

