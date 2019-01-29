import re

def verifyIPv4( address ):
    """check if given string indeed contains a valid ipv4 address"""
    address.strip()
    result= re.match(r'(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})',address)
    if result == None:
        return False
    for i in range(1,5):
        num= int( result.group( i ))
        if num > 255:
            return False
    return True

def isNotReservedIPv4( address ):
    """ testing if a valid ip address is one that could not be used as target"""
    addr= list( map( int, address.split( '.' )))
    if addr[0]==0 or addr[0]==127 or addr[0]>=224 or (addr[0]==192 and addr[1]==88 and addr[2]==99):
        return False # 0 is self-reference, 127 is loopback, 224-239 is mylticast, 240 and over are reserved,192.88.99 is reserved for ipv6 to ipv4 relay 
    return True


def ping( address ):
    import subprocess                           #this is a linux ping command
    cplProc= subprocess.run( ["ping", address, "-c 4" ], stdout= subprocess.DEVNULL, stderr= subprocess.DEVNULL )
    return cplProc.returncode==0


def checkIP( address ):
    if verifyIPv4( address ):
        print("%s is a valid IPv4 address string"%(address))

        if isNotReservedIPv4( address ):
            print(address,"is not a reserved address")

            if ping( address ):
                print( "{} is reachable through ping".format(address))
                return True
            else:
                print( "{} is not reachable through ping".format(address))
        else:
            print(address,"is a reserved IPv4 address")
    else:
        print("%s is not a valid IPv4 address string"%(address))
    return False

