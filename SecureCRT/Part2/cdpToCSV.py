import csv

#pathToCdpCsvFile = "D:\\router\\showcdpneidetail.csv"    
#pathToCdpTextFile = "D:\\router\\showcdpneidetail.txt"    



#Open textfile
def OpenTextFile(pathToCdpTextFile):
    with open(pathToCdpTextFile) as text_file:
        text_file = text_file.read().splitlines()
        return text_file


#export cdp dictionary to a csv file
def dictToCsv(results,resultsFile):
    with open(resultsFile, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',lineterminator='\r')
        #for result in results:
        #    filewriter.writerow([result["source"],result["destination"],result["IPaddress"],result["status"]])
        count = 0
        filewriter.writerow(["CdpNeighbor","Remote-ip", "Remote-platfrom", "Local-interface", "Remote-interface"])
        for item in range(0,len(results["neighbor"])):
            filewriter.writerow([results["neighbor"][count],results["remote-ip"][count],results["remote-platfrom"][count],results["local-interface"][count],results["remote-interface"][count]])
            count +=1

            


#Make a cdp dictionary
def makeCdpdict(cdpOutput):
    #print(cdpOutput)
    cdpNeighbor = {"neighbor":[],"remote-ip":[],"remote-platfrom":[],"local-interface":[],"remote-interface":[] }
    count = 0
    for line in cdpOutput:
        if "Device ID:" in line:
            #print(line.split("Device ID: ")[1].split(".")[0])
            cdpNeighbor["neighbor"].append(line.split("Device ID: ")[1].split(".")[0])
            if "IP address:" in cdpOutput[count+2]:
                #print(cdpOutput[count+2].split(" ")[-1])
                cdpNeighbor["remote-ip"].append(cdpOutput[count+2].split(" ")[-1])
            if "IP address:" not in cdpOutput[count+2]:
                #print("IP address not found")
                cdpNeighbor["remote-ip"].append("IP address not found")
            if "Platform" in cdpOutput[count+2]:
                #print(cdpOutput[count+3].split(": ")[1].split(",")[0])
                cdpNeighbor["remote-platfrom"].append(cdpOutput[count+2].split(": ")[1].split(",")[0])
            if "Platform" in cdpOutput[count+3]:
                #print(cdpOutput[count+3].split(": ")[1].split(",")[0])
                cdpNeighbor["remote-platfrom"].append(cdpOutput[count+3].split(": ")[1].split(",")[0])
            if "Platform" in cdpOutput[count+4]:
                #print(cdpOutput[count+4].split(": ")[1].split(",")[0])
                cdpNeighbor["remote-platfrom"].append(cdpOutput[count+4].split(": ")[1].split(",")[0])
            if "Platform" not in cdpOutput[count+2] and "Platform" not in cdpOutput[count+3] and "Platform" not in cdpOutput[count+4]:
                    #print("Platfrom not found")
                    cdpNeighbor["remote-platfrom"].append("Platfrom not found")

            if "Interface" in cdpOutput[count+3]:
                #print(cdpOutput[count+4].split(": ")[1].split(",")[0])
                cdpNeighbor["local-interface"].append(cdpOutput[count+3].split(": ")[1].split(",")[0])
                #print(cdpOutput[count+4].split(": ")[2])
                cdpNeighbor["remote-interface"].append(cdpOutput[count+3].split(": ")[2])
            if "Interface" in cdpOutput[count+4]:
                #print(cdpOutput[count+4].split(": ")[1].split(",")[0])
                cdpNeighbor["local-interface"].append(cdpOutput[count+4].split(": ")[1].split(",")[0])
                #print(cdpOutput[count+4].split(": ")[2])
                cdpNeighbor["remote-interface"].append(cdpOutput[count+4].split(": ")[2])
            if "Interface" in cdpOutput[count+5]:
                #print(cdpOutput[count+5].split(": ")[1].split(",")[0])
                cdpNeighbor["local-interface"].append(cdpOutput[count+5].split(": ")[1].split(",")[0])
                #print(cdpOutput[count+5].split(": ")[2])
                cdpNeighbor["remote-interface"].append(cdpOutput[count+5].split(": ")[2])
            if "Interface" not in cdpOutput[count+3] and"Interface" not in cdpOutput[count+4] and "Interface" not in cdpOutput[count+5]:
                    #print("local-interface")
                    #print("remote-interface")
                    cdpNeighbor["local-interface"].append("interface not found")
                    cdpNeighbor["remote-interface"].append("interface not found")        
        count +=1
    return cdpNeighbor

def validateinput(cdpInput):
    for line in cdpInput:
        if "% CDP is not enabled" in line:
            return 1
        if "displayed : 0" in line:
            return 1


def printErrToFile(msg,pathToCdpTextFile):
    file = pathToCdpTextFile.replace("showcdpneidetail", "showcdperror")
    with open(file, "w") as text_file:
        text_file.write(msg)


def main(pathToCdpTextFile,pathToCdpCsvFile):
    
    #Open textfile
    cdpInput = OpenTextFile(pathToCdpTextFile)

    #Validate input 0 = good 1 = bad
    validationbit = 0
    validationbit = validateinput(cdpInput)
    if validationbit == 1:
        #msg = "Something input file not valid"
        #printErrToFile(msg,pathToCdpTextFile)
        return
        
    #Make a cdp dictionary
    try:
        cdpNeighbor = makeCdpdict(cdpInput)
    except:
        msg = "Something happend with the pharsing of the input"
        printErrToFile(msg,pathToCdpTextFile)
        return

    #export cdp dictionary to a csv file
    dictToCsv(cdpNeighbor,pathToCdpCsvFile)


if __name__ == "__main__":
    #main(pathToCdpTextFile,pathToCdpCsvFile)
    main()


