import csv

#pathToCsvFile = "D:\\router\\showplatform.csv"    
#pathToTextFile = "D:\\router\\showplatform.txt"    

def OpenTextFile(path):
    with open(path) as text_file:
        text_file = text_file.read().splitlines()
        return text_file

def dictToCsv(results,resultsFile):
    with open(resultsFile, 'w') as csvfile:
        #print(results)
        filewriter = csv.writer(csvfile, delimiter=',',lineterminator='\r')
        count = 0
        filewriter.writerow(["Slot","Type","State","InsertTime","CpldVersion","FirmwareVersion"])
        for item in range(0,len(results["Slot"])):
            filewriter.writerow([results["Slot"][count],results["Type"][count],results["State"][count],results["InsertTime"][count],results["CpldVersion"][count],results["FirmwareVersion"][count]])
            count +=1

def makePatformDict(platfromInput):

   
    platformStatus = {"Slot":[],"Type":[],"State":[],"InsertTime":[],"CpldVersion":[],"FirmwareVersion":[]}
    
    dictOfcpld = {}
    for line in platfromInput:
        if "ok" in line or "N/A" in line:
            if "," in line:
                line = line.replace(", ",",")
            #print(line)
            cleanedList1 = []
            #iterate over ar and clean up then line
            for item in line.split(" "):
                if 1 <= len(item):
                    cleanedList1.append(item)
            platformStatus["Slot"].append(cleanedList1[0])
            platformStatus["Type"].append(cleanedList1[1])
            platformStatus["State"].append(cleanedList1[2])
            platformStatus["InsertTime"].append(cleanedList1[3]) 
        
        #make a dictionary with slot index as key and CpldVersion FirmwareVersion
        phaseLine = " ".join(line.split()).split(" ")
        if len(phaseLine) == 3 and ")" in line:
            if phaseLine[0] in platformStatus["Slot"]:
               dictOfcpld[platformStatus["Slot"].index(phaseLine[0])] = [phaseLine[1], phaseLine[2]]

    #append CpldVersion and FirmwareVersion from dictionary
    for x in range(0, len(platformStatus["Slot"])):
        if x in dictOfcpld:
            platformStatus["CpldVersion"].append(dictOfcpld[x][0])
            platformStatus["FirmwareVersion"].append(dictOfcpld[x][1])
        else:
            platformStatus["CpldVersion"].append("N/A")
            platformStatus["FirmwareVersion"].append("N/A")

    #print(platformStatus)
    return platformStatus


def validateinput(platfromInput):
    if len(platfromInput) < 2:
        return
    for line in platfromInput:
        if "% Incomplete command" in line:
            return 1
        if "Switch#" in line:
            return 1
        if "TLB entries" in line:
            return 1

def printErrToFile(msg,pathToTextFile):
    file = pathToTextFile.replace(".txt", "error.txt")
    with open(file, "w") as text_file:
        text_file.write(msg)



def main(pathToTextFile,pathToCsvFile):
    platfromInput = OpenTextFile(pathToTextFile)

    #Validate input 0 = good 1 = bad
    validationbit = 0
    validationbit = validateinput(platfromInput)
    if validationbit == 1:
        #msg = "Something input file not valid"
        #printErrToFile(msg,pathToTextFile)
        return
        

    #Make a platfrom dictionary
    try:
        platformStatus = makePatformDict(platfromInput)
    except:
        msg = "Something happend with the pharsing of the input"
        printErrToFile(msg,pathToTextFile)
        return

    
    dictToCsv(platformStatus, pathToCsvFile)

if __name__ == "__main__":
    main()