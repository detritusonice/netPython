import time
import paramiko
import re

def sendCommand( terminalSession, cmdString ,sleepPeriod=1):
    terminalSession.send(cmdString.strip()+'\n')
    time.sleep(sleepPeriod)

def sshConnect( hostaddr, credentials, commands, showFeedback, feedbackAction ):
    """perform an ssh connection to hostaddr, using provided credentials and passing given commands"""
    #prepare strings if not already
    hostaddr.strip()
    for i in range(len(credentials)):
        credentials[i]=credentials[i].strip()
    for i in range(len(commands)):
        commands[i]=commands[i].strip()

    #perform basic sanity checks
    if len(credentials[0])==0:
        print( 'No username given')
        return False
    if len(commands)==0:
        print('Command list is empty, no point in establishing a secure connection')
        return True
    #setup the ssh connection
    try:
        session= paramiko.SSHClient()
        
        session.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())#WarningPolicy()) #warn if unknown keys are encountered

        session.connect( hostaddr, username=credentials[0], password=credentials[1])

        term= session.invoke_shell()

        sendCommand(term,"enable")  #enter su mode
        sendCommand(term,"terminal length 0") #disable output pagination
        sendCommand(term,"configure terminal")
        
        for cmd in commands:
            sendCommand(term,cmd,2)

        feedback= term.recv(65535).decode("utf-8")

        if re.search("invalid input", feedback):
            print("IOS Syntax errors in command file for device {}:\n\n".format(hostaddr))
        elif showFeedback:
            print("All done. No erros. Feedback from device {} was:\n\n".format(hostaddr))

        if feedbackAction!=None:
            feedbackAction(feedback)
        if showFeedback:
            print(feedback+'\n\n')

        term.close()
        session.close()

    except paramiko.AuthenticationException as e:
        print("exception raised by authentication or network subsystem\n"+e.text)
        return False
    return True
