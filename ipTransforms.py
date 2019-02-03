import random
import ipTools

def IPv4ToInt( address ):
    """create an integer bitmask from an IPv4 address string"""
    if ipTools.verifyIPv4( address ):
        octets=list(map(int,address.split('.')))
        num=octets[0]<<24 | octets[1]<<16 | octets[2]<<8 | octets[3]
        return num
    return 0

def intToIPv4( num ):
    """create an IPv4 address string from an integer bitmask"""
    addr=''
    for i in range(4):
        byte=(num>>(24-i*8))&255
        addr+=str(byte)
        if (i<3):
            addr+='.'
    return addr

def isValidSubnetMask( mask ):
    """the binary form of subnet mask must consist of all ones followed by all zeros"""
    binMask = IPv4ToInt(mask)
    maskInverse= binInverse(binMask)
    if maskInverse>0 and ( maskInverse & (maskInverse+1))==0: #this happens only when a number is (some power of 2) -1
        return True
    return False

def binInverse( num , length=32 ):
    """return the number having inverted bits"""
    return num^( (1<<length)-1) # (1<<32)-1 is a mask of all 32 ones, xor(^) to num to invert digits

def subnetIPv4( address, subnetMask ):
    """given an address and its subnet mask return a string containing the subnet address"""
    adr= IPv4ToInt(address)
    msk= IPv4ToInt(subnetMask)
    return intToIPv4(adr&msk)

def randomMaskedNum( intWildCardMask ) :
    """given a wildcard mask in bitmask integer form, return a random number using the mask's  set bits"""
    reduct=0
    if intWildCardMask&255==255:
        reduct=1
    rnd=random.randint(1,intWildCardMask-reduct) #this is the max number we need, do not generate 25a
    return rnd & intWildCardMask 

def randomSubnetIPv4( subnet, wildcardMask ):
    """given a subnet address and a subnet mask address in string form, return a random address
        for this subnet, not broadcast"""
    net= IPv4ToInt(subnet)
    mask= IPv4ToInt(wildcardMask)

    newaddr= net | ( randomMaskedNum(mask))
    return intToIPv4(newaddr)
