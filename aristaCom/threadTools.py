import threading

def startThreads(function,idparamList, params):
    """given a function, an identifying paramete list and a list of parameters 
        creates thread objects in a list, starts them, then returns the list"""
    threads=[]

    for id in idparamList:
        newThread=threading.Thread(target=function,args=(id,)+tuple(params))
        threads.append(newThread)

    for t in threads:
        t.start()

    return threads

def waitThreads(threads):
   """given a list of started threads, joins and waits for their completion"""
   for t in threads:
       t.join()


