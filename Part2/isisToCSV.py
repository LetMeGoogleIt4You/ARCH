import csv

#pathToCsvFile = "D:\\router\\showisisneidet.csv"
#pathToTextFile = "D:\\router\\showisisneidet.txt"


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
        filewriter.writerow(["IsisNeighbor","Type", "Interface", "IPaddress", "CircuitId", "State","Uptime"])
        for item in range(0,len(results["IsisNeighbor"])):
            filewriter.writerow([results["IsisNeighbor"][count],results["Type"][count],results["Interface"][count],results["IPaddress"][count],results["CircuitId"][count],results["State"][count],results["Uptime"][count]])
            count +=1

def makeIsisDict(isisInput):

    isisStatus = {"IsisNeighbor":[],"Type":[],"Interface":[],"IPaddress":[],"CircuitId":[],"State":[],"Uptime":[] }
    
    #iterate over isisInput
    count = 0
    for line in isisInput:
        if "State Changed" in line:
            cleanedList = []
            #iterate over ar and clean up then line
            for item in isisInput[count-3].split(" "):
                if 1 < len(item):
                    cleanedList.append(item)
            isisStatus["IsisNeighbor"].append(cleanedList[0])
            isisStatus["Type"].append(cleanedList[1])
            isisStatus["IPaddress"].append(cleanedList[3])
            isisStatus["State"].append(cleanedList[4])
            isisStatus["CircuitId"].append(" "+cleanedList[5])
            isisStatus["Uptime"].append(line.split("Changed: ")[1])
        if "Interface name" in line:
            isisStatus["Interface"].append(line.split("name: ")[1])
            #print(line.split("name: ")[1])
        count +=1
        
        
    #print(isisStatus)
    return isisStatus

def printErrToFile(msg,pathToCdpTextFile):
    file = pathToCdpTextFile.replace("show", "error")
    with open(file, "w") as text_file:
        text_file.write(msg)

def validateinput(isisInput):
    #print(isisInput)
    if len(isisInput) < 2:
        return 1
    count = 0
    for line in isisInput:
        #print(line)
        if "State Changed" in line:
            #print(line)
            count += 1
    if count == 0:
        return 1


def main(pathToTextFile,pathToCsvFile):
    isisInput = OpenTextFile(pathToTextFile)

    #Validate input 0 = good 1 = bad
    validationbit = 0
    validationbit = validateinput(isisInput)
    if validationbit == 1:
        #uncomment for debug
        #msg = "Something input file not valid"
        #printErrToFile(msg,pathToTextFile)
        return
    
    #Make isis dict
    try:
        isisStatus = makeIsisDict(isisInput)
    except:
        msg = "Something happend with the pharsing of the input"
        printErrToFile(msg,pathToTextFile)
        return

    #make csv file
    dictToCsv(isisStatus, pathToCsvFile)



if __name__ == "__main__":
    main()
    #main(pathToTextFile,pathToCsvFile)
