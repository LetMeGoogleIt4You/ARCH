import os


showCommands = ["show version","show cdp nei detail", "show interfaces","show ip bgp neighbors","show isis nei det", "show ip route stat",  "show vlan", "show vrf det", "show snmp", "show inventory", "show platform","show running-config"]


folder = crt.Dialog.Prompt ("Enter the folder location")


folderLocation = folder.replace('"\"' , '"\\"')


def makeFolder(hostname):
    if not os.path.exists(folderLocation + "\\" + hostname):
        os.makedirs(folderLocation+"\\" +hostname)


def getHostname():
    crt.Screen.Send("terminal length 0"+"\r") #Send command
    prompt = crt.Screen.Get(crt.Screen.CurrentRow, 1, crt.Screen.CurrentRow, 80)
    hostname = prompt.split("#")[0]
    return hostname

def runningCommand(hostname,command):
    
    crt.Screen.Send(command+"\r") #Send command
    crt.Screen.WaitForString(command) #Wait for the command is sent
    strResults = crt.Screen.ReadString(hostname +"#") #Save the output to a variabel    
    return strResults

def makeTxtFile(folderLocation,hostname,showCommands,strResults):
    command = showCommands.replace(" ","")
    text_file = open(folderLocation+ "\\"+ hostname + "\\"+ command + ".txt", "wb")
    text_file.write(strResults)
    text_file.close()    


def main():
    hostname = getHostname()
    makeFolder(hostname)
    count = 0
    for command in showCommands:
        
        strResults = runningCommand(hostname,command)
        makeTxtFile(folderLocation,hostname,command,strResults,)
        

main()    
    