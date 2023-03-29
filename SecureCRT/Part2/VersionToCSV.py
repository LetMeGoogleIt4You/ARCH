import csv

#pathToCsvFile = "D:\\router\\1showversion.csv"
#pathToTextFile = "D:\\router\\1showversion.txt"


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
        filewriter.writerow(["Hostname","Model", "Version", "Uptime", "SystemImage", "ConfigurationRegister"])
        for item in range(0,len(results["Hostname"])):
            filewriter.writerow([results["Hostname"][count],results["Model"][count],results["Version"][count],results["Uptime"][count],results["SystemImage"][count],results["ConfigurationRegister"][count]])
            count +=1


def makeVersionDict(showVersion):

    VersionStatus = {"Hostname":[],"Model":[],"Version":[],"Uptime":[],"SystemImage":[],"ConfigurationRegister":[] }
    count = 0

    #iterate over all lines in the showInterface list
    #print(showInterface)
    for line in showVersion:
        #print(line)
        #Get version
        if "), Version"  in line:
            #print(line.split(', Version')[1].split(",")[0])
            VersionStatus["Version"].append(line.split(', Version')[1].split(",")[0])
        #Get hostname and uptime
        if "uptime is" in line:
            #print(line.split(" ")[0])
            VersionStatus["Hostname"].append(line.split(" ")[0])
        #Get uptime
        if " uptime " in line:
            VersionStatus["Uptime"].append(line.split("uptime is ")[-1])
        #Get system image
        if "System image" in line:
            VersionStatus["SystemImage"].append(line.split('is "')[1].replace('"',''))
            #print(line.split('is "')[1].replace('"',''))
        #Get model
        if "Processor board ID " in line:
            VersionStatus["Model"].append(showVersion[count-1].split(" ")[1])
            #print(showVersion[count-1].split(" ")[1])
        if "Configuration register" in line:
            VersionStatus["ConfigurationRegister"].append(line.split("register is ")[-1])
            #print(line.split("register is ")[-1])
        count +=1
    #print(VersionStatus)
    return VersionStatus

def main(pathToTextFile,pathToCsvFile):
    showVersion = OpenTextFile(pathToTextFile)

    VersionStatus = makeVersionDict(showVersion)

    dictToCsv(VersionStatus, pathToCsvFile)

if __name__ == "__main__":
    main()
    #main(pathToTextFile,pathToCsvFile)