import csv
import re


#pathToCsvFile = "D:\\router\\showipbgpneighbors.csv"    
#pathToTextFile = "D:\\router\\showipbgpneighbors.txt"    



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
        filewriter.writerow(["BgpNeighbor","RemoteAS", "Link", "BgpVersion", "RemoteRouterID", "BgpState", "Up"])
        for item in range(0,len(results["BgpNeighbor"])):
            filewriter.writerow([results["BgpNeighbor"][count],results["RemoteAS"][count],results["Link"][count],results["BgpVersion"][count],results["RemoteRouterID"][count],results["BgpState"][count],results["Up"][count]])
            count +=1


def makeBgpDict(showBgp):

   
    BgpStatus = {"BgpNeighbor":[],"RemoteAS":[],"Link":[],"BgpVersion":[],"RemoteRouterID":[],"BgpState":[],"Up":[] }
    count = 0

    #iterate over all lines in the showInterface list
    #print(showInterface)
    for line in showBgp:
        #print(line)
        if "BGP neighbor is" in line:
            BgpStatus["BgpNeighbor"].append(line.split('is ')[1].split(",")[0])
            BgpStatus["RemoteAS"].append(line.split('is ')[1].split(", ")[1])
            BgpStatus["Link"].append(line.split('is ')[1].split(", ")[2])
            if "Member of" in showBgp[count+1]:
                count = count+1
            BgpStatus["BgpVersion"].append(showBgp[count+1].split("BGP ")[1].split(",")[0])
            BgpStatus["RemoteRouterID"].append(showBgp[count+1].split("remote router ID ")[1])
            BgpStatus["BgpState"].append(showBgp[count+2].split("= ")[1].split(",")[0])
            BgpStatus["Up"].append(showBgp[count+2].split(" ")[-1])
            #print(showBgp[count+2].split(" ")[-1])
        count +=1
    #print(BgpStatus)
    return BgpStatus


def validateinput(showBgp):
    for line in showBgp:
        if "% Invalid input detected" in line:
            return 1
        if "% BGP not active" in line:
            return 1


def printErrToFile(msg,pathToCdpTextFile):
    file = pathToCdpTextFile.replace("showipbgpneighbors", "showipbgperror")
    with open(file, "w") as text_file:
        text_file.write(msg)



def main(pathToTextFile,pathToCsvFile):
    showBgp = OpenTextFile(pathToTextFile)

    #Validate input 0 = good 1 = bad
    validationbit = 0
    validationbit = validateinput(showBgp)
    if validationbit == 1:
        #msg = "Something input file not valid"
        #printErrToFile(msg,pathToCdpTextFile)
        return


    try:
        BgpStatus = makeBgpDict(showBgp)
    except:
        msg = "Something happend with the pharsing of the input"
        printErrToFile(msg,pathToTextFile)
        return



    dictToCsv(BgpStatus, pathToCsvFile)

if __name__ == "__main__":
    main()