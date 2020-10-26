import csv

#pathToCsvFile = "D:\\AKR\\router\\showvlan.csv"    
#pathToTextFile = "D:\\AKR\\router\\showvlan.txt"  


#Open textfile
def OpenTextFile(file):
    with open(file) as text_file:
        text_file = text_file.read().splitlines()
        return text_file


def dictToVlan(results,resultsFile):
    with open(resultsFile, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',lineterminator='\r')
        #for result in results:
        #    filewriter.writerow([result["source"],result["destination"],result["IPaddress"],result["status"]])
        count = 0
        filewriter.writerow(["VlanID","Name", "Ports"])
        for item in range(0,len(results["VlanID"])):
            filewriter.writerow([results["VlanID"][count],results["Name"][count],results["Ports"][count]])
            count +=1


#Make a cdp dictionary
def makeVlanDict(VlanOutput):
    #print(VlanOutput)
    vlanDic = {"VlanID": [], "Name": [], "Ports":[]}
    for line in VlanOutput:
        if "active" in line:
            #get vlan ID
            #print(line.split(" ")[0])
            vlanDic["VlanID"].append(line.split(" ")[0])
            
            #Get vlan name
            if len(line.split(" ")[4])>2:
                #print(line.split(" ")[4])
                vlanDic["Name"].append(line.split(" ")[4])
            if len(line.split(" ")[3])>2:
                #print(line.split(" ")[3])
                vlanDic["Name"].append(line.split(" ")[3])
            if len(line.split(" ")[2])>2:
                #print(line.split(" ")[2])
                vlanDic["Name"].append(line.split(" ")[2])
            if len(line.split(" ")[1])>2:
                #print(line.split(" ")[1])
                vlanDic["Name"].append(line.split(" ")[1])
            
            #get ports
            if len(line.split("active    ")[-1]) <1:
                #print("N/A")
                vlanDic["Ports"].append("N/A")
            if len(line.split("active    ")[-1]) > 1:
                #print(line.split("active    ")[-1])
                vlanDic["Ports"].append(line.split("active    ")[-1])
    return vlanDic
    #print(len(vlanDic["VlanID"]))
    #print(len(vlanDic["Name"]))
    #print(len(vlanDic["Ports"]))


def validateinput(vlanOutput):
    if len(vlanOutput) < 5:
        return 1
    for line in vlanOutput:
        if "% Incomplete command" in line:
            return 1
        if "% Ambiguous command" in line:
            return 1

def printErrToFile(msg,pathToTextFile):
    file = pathToTextFile.replace("showvlan", "showvlanerror")
    with open(file, "w") as text_file:
        text_file.write(msg)


def main(pathToTextFile,pathToCsvFile):
    vlanOutput = OpenTextFile(pathToTextFile)


    #Validate input 0 = good 1 = bad
    validationbit = 0
    validationbit = validateinput(vlanOutput)
    if validationbit == 1:
        #msg = "Something input file not valid"
        #printErrToFile(msg,pathToTextFile)
        return

    #Make a vrf dictionary
    try:
        vlanDict = makeVlanDict(vlanOutput)
    except:
        msg = "Something happend with the pharsing of the input"
        printErrToFile(msg,pathToTextFile)
        return

    dictToVlan(vlanDict,pathToCsvFile)


if __name__ == "__main__":
    main()