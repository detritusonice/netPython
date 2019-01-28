import os 

def checkFile( filename ):
    filename.strip()        #trim spaces
    if len(filename)>0:     #check that name is nonempty
        if os.path.exists(filename) and os.path.isfile(filename) and os.access(filename,os.R_OK):#check that given name is a file and can be accessed
            return True
    return False

def readByLines( filename ):
    res=[]
    if checkFile(filename): #file exists
        try:
            infile=open(filename,"r") #open file for reading
            infile.seek(0)              #move to start of file (defensive)
            res=list(map(lambda x: x.strip(),infile.readlines()))      #load text lines in resulting list, remove newlines and any spaces
            infile.close()
        except:
            pass    #placeholder
    return res




