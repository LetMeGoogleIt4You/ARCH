import csv



#pathToInterfaceCsvFile = "D:\\router\\showinventory.csv"    
#pathToInterfaceTextFile = "D:\\router\\showinventory.txt"    


def OpenTextFile(path):
    with open(path) as text_file:
        text_file = text_file.read().splitlines()
        return text_file


def dictToCsv(results,resultsFile):
    with open(resultsFile, 'w') as csvfile:
        #print(results)
        filewriter = csv.writer(csvfile, delimiter=',',lineterminator='\r')
        #for result in results:
        #    filewriter.writerow([result["source"],result["destination"],result["IPaddress"],result["status"]])
        count = 0
        filewriter.writerow(["Part-name","PID", "S/N"])
        for item in range(0,len(results["Part-name:"])):
            filewriter.writerow([results["Part-name:"][count],results["PID:"][count],results["S/N:"][count]])
            count +=1


def makeInventoryDict(showInventory):
    inventoryStatus = {"Part-name:": [], "PID:": [], "S/N:": []}

    count = 0
    for line in showInventory:
        count +=1
        if "NAME" in line:
            #print(line.split('"')[1])
            inventoryStatus["Part-name:"].append(line.split('"')[1])
            #print(text_file[count].split("PID: ")[1].split()[0])
            inventoryStatus["PID:"].append(showInventory[count].split("PID: ")[1].split()[0])

            if "           " not in showInventory[count].split("SN: ")[1]:
                inventoryStatus["S/N:"].append(showInventory[count].split("SN: ")[1].replace(" ",""))
                #print(text_file[count].split("SN: ")[1])
            if "           " in showInventory[count].split("SN: ")[1]:
                inventoryStatus["S/N:"].append("N/A")
                #print("N/A")
    #print(inventoryStatus)
    return inventoryStatus



def main(pathToInterfaceTextFile,pathToInterfaceCsvFile):
    showInventory = OpenTextFile(pathToInterfaceTextFile)
    #print(showInventory)
    inventoryStatus = makeInventoryDict(showInventory)
    #print(inventoryStatus)
    dictToCsv(inventoryStatus, pathToInterfaceCsvFile)


if __name__ == "__main__":
    main()
