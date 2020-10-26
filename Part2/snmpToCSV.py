import csv

#pathToCsvFile = "D:\\router\\showsnmp.csv"
#pathToTextFile = "D:\\router\\showsnmp.txt"


def OpenTextFile(path):
    with open(path) as text_file:
        text_file = text_file.read().splitlines()
        return text_file


def dictToCsv(results,resultsFile):
    with open(resultsFile, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',lineterminator='\r')

        
        count = 0
        filewriter.writerow(["Contact","Location", "Servers", "Port"])
        
        for item in range(0,len(results["Contact"])):
            filewriter.writerow([results["Contact"][count],results["Location"][count],results["Servers"][count],results["Port"][count]])
            count +=1


def makeSnmpDict(showSnmp):

    snmpStatus = {"Contact":[],"Location":[],"Servers":[],"Port":[] }
    
    serverCounter = 0
    contactCounter = 0
    locationCounter = 0
    
    for line in showSnmp:
        #print(line)
        if "Contact" in line:
            snmpStatus["Contact"].append(line.split("Contact: ")[1])
            contactCounter +=1
            #print(line.split(": ")[1])        
        if "Location" in line:
            snmpStatus["Location"].append(line.split("Location: ")[1])
            locationCounter +=1
            #print(line.split(": ")[1])
        if "Logging to " in line:
            ipAddressAndPort = line.split(" to ")[1].split(", ")[0]
            last_char_index = ipAddressAndPort.rfind(".")
            ipAddress = ipAddressAndPort[:last_char_index]
            port = ipAddressAndPort[last_char_index+1:]
            
            snmpStatus["Servers"].append(ipAddress)
            snmpStatus["Port"].append(port)
            #print(ipAddress)
            #print(port)
            serverCounter +=1
            if serverCounter > 1:
                #print("N/A")
                snmpStatus["Contact"].append("N/A")
                snmpStatus["Location"].append("N/A")
                
    if contactCounter == 0:
        snmpStatus["Contact"].append("N/A")
    if locationCounter == 0:
        snmpStatus["Location"].append("N/A")
    
    #print(snmpStatus)
    return snmpStatus


def validateinput(showSnmp):
    if len(showSnmp) < 2:
        return 1
    for line in showSnmp:
        if "%SNMP agent not enabled" in line:
            return 1



def printErrToFile(msg,pathToTextFile):
    file = pathToTextFile.replace("showvrf", "showvrferror")
    with open(file, "w") as text_file:
        text_file.write(msg)


def main(pathToTextFile,pathToCsvFile):
    showSnmp = OpenTextFile(pathToTextFile)

    #Validate input 0 = good 1 = bad
    validationbit = 0
    validationbit = validateinput(showSnmp)
    if validationbit == 1:
        #msg = "Something input file not valid"
        #printErrToFile(msg,pathToTextFile)
        return
            
    #Make a snmp dictionary
    try:
        snmpStatus = makeSnmpDict(showSnmp)
    except:
        msg = "Something happend with the pharsing of the input"
        printErrToFile(msg,pathToTextFile)
        return


    dictToCsv(snmpStatus, pathToCsvFile)


if __name__ == "__main__":
    main()
    #main(pathToTextFile,pathToCsvFile)