import csv
import re
items =('Interface', '123')

#pathToCsvFile = "F:\\router\\showinterfaces.csv"    
#pathToTextFile = "F:\\router\\showinterfaces.txt"    

def OpenTextFile(path):
    with open(path) as text_file:
        text_file = text_file.read().splitlines()
        return text_file


def dictToCsv(results,resultsFile):
    with open(resultsFile, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',lineterminator='\r')
        #for result in results:
        #    filewriter.writerow([result["source"],result["destination"],result["IPaddress"],result["status"]])
        count = 0
        filewriter.writerow(["Interface-name","Status", "Protocol", "Description", "Internet-address", "Duplex", "Speed", "Media-type"])
        for item in range(0,len(results["Interface-name"])):
            filewriter.writerow([results["Interface-name"][count],results["Status"][count],results["Protocol"][count],results["Description"][count],results["Internet-address"][count],results["Duplex"][count],results["Speed"][count],results["Media-type"][count]])
            count +=1

def makeInterfaceDict(showInterface):
    global items
    
    interfaceNames = ["TenGigabitEthernet","GigabitEthernet","Ethernet-Internal","Loopback", "Tunnel","Port-channel","Vlan","Cellular","FastEthernet"]
    InterfaceStatus = {"Interface-name":[],"Status":[],"Protocol":[],"Description":[],"Internet-address":[],"Duplex":[],"Speed":[],"Media-type":[] }
    count = 0

    #iterate over all lines in the showInterface list
    #print(showInterface)
    for line in showInterface:
        #iterate over all lines in the interfaceNames list
        for interfacename in interfaceNames:
            #removes the numbers from <interface*/*/>
            match = re.match(r"([a-z]+)([0-9]+)", line, re.I)
            if match:
                items = match.groups()
                #print(items)
            if interfacename == items[0] and " line " in line:
                #print(line)
                #print(line.split(" is ")[0])
                InterfaceStatus["Interface-name"].append(line.split(" is ")[0])
                #print(line.split(" is ")[1].split(",")[0])
                InterfaceStatus["Status"].append(line.split(" is ")[1].split(",")[0])
                #print(line.split(" is ")[2])
                InterfaceStatus["Protocol"].append(line.split(" is ")[2])
                if "Description" in showInterface[count+2]:
                    #print(showInterface[count+2].split(" Description: ")[1])
                    InterfaceStatus["Description"].append(showInterface[count+2].split(" Description: ")[1])
                if "Description" not in showInterface[count+2]:
                    #print("Description not set")
                    InterfaceStatus["Description"].append("Description not set")
                if "Internet address" in showInterface[count+2]:
                    #print(showInterface[count+2])
                    if "negotiated" in showInterface[count+2]:
                        #print(showInterface[count+2].split(" ")[-1])
                        InterfaceStatus["Internet-address"].append(showInterface[count+2].split(" ")[-1])
                    else:
                        #print(showInterface[count+2].split("  Internet address is ")[1])
                        InterfaceStatus["Internet-address"].append(showInterface[count+2].split("Internet address is ")[1])
                if "Internet address" in showInterface[count+3]:
                    #print(showInterface[count+3])
                    if "negotiated" in showInterface[count+3]:
                        #print(showInterface[count+2].split(" ")[-1])
                        InterfaceStatus["Internet-address"].append(showInterface[count+3].split(" ")[-1])
                    else:
                        #print(showInterface[count+3].split("  Internet address is ")[1])
                        InterfaceStatus["Internet-address"].append(showInterface[count+3].split("Internet address is ")[1])
                if "Internet address" in showInterface[count+4]:
                    #print(showInterface[count+4])
                    if "negotiated" in showInterface[count+4]:
                        #print(showInterface[count+2].split(" ")[-1])
                        InterfaceStatus["Internet-address"].append(showInterface[count+4].split(" ")[-1])
                    else:
                        #print(showInterface[count+4].split("  Internet address is ")[1])
                        InterfaceStatus["Internet-address"].append(showInterface[count+4].split("Internet address is")[1])
                if "Internet address" not in showInterface[count+3] and "Internet address" not in showInterface[count+4] and "Internet address" not in showInterface[count+2]:
                    #print("Internet address not set")
                    InterfaceStatus["Internet-address"].append("Internet address not set")
        if " Keepalive " in showInterface[count]:
            if "uplex" in showInterface[count+1]:
                #print(showInterface[count+1].replace(" ","").split(",")[0])
                InterfaceStatus["Duplex"].append(showInterface[count+1].replace(" ","").split(",")[0])
                #print(showInterface[count+1].split(", ")[1])
                InterfaceStatus["Speed"].append(showInterface[count+1].split(", ")[1])
                #print(showInterface[count+1].split(", ")[3].split("is ")[1])
            if "media" in showInterface[count+1]:
                InterfaceStatus["Media-type"].append(showInterface[count+1].split("media type is ")[1])
            if "uplex"not in showInterface[count+1]:
                #print("Duplex not set")
                InterfaceStatus["Duplex"].append("Duplex not set")
                #print("Speed not set")
                InterfaceStatus["Speed"].append("Speed not set")
            if "media" not in showInterface[count+1]:
                InterfaceStatus["Media-type"].append("Media type not set")      
        count +=1
    #print(InterfaceStatus)
    return InterfaceStatus


def printErrToFile(msg,pathToTextFile):
    file = pathToTextFile.replace("showinterfaces", "showinterfaceserror")
    with open(file, "w") as text_file:
        text_file.write(msg)

def main(pathToTextFile,pathToCsvFile):
    showInterface = OpenTextFile(pathToTextFile)


    ##Make a vrf dictionary
    try:
        InterfaceStatus = makeInterfaceDict(showInterface)
    except:
        msg = "Something happend with the pharsing of the input"
        printErrToFile(msg,pathToTextFile)
        return

    #print(InterfaceStatus)
    dictToCsv(InterfaceStatus, pathToCsvFile)



if __name__ == "__main__":
    main()
