import csv

#pathToCsvFile = "D:\\router\\showiproutestat.csv"    
#pathToTextFile = "D:\\router\\showiproutestat.txt"    

#Open textfile
def OpenStaticTextFile(file):
    with open(file) as text_file:
        text_file = text_file.read().splitlines()
        return text_file


#export cdp dictionary to a csv file
def dictToStatic(results,resultsFile):
    with open(resultsFile, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',lineterminator='\r')
        #for result in results:
        #    filewriter.writerow([result["source"],result["destination"],result["IPaddress"],result["status"]])
        count = 0
        filewriter.writerow(["Type","Source", "Destination"])
        for item in range(0,len(results["Type"])):
            filewriter.writerow([results["Type"][count],results["Source"][count],results["Destination"][count]])
            count +=1


#Make a static dictionary
def makeStaticdict(staticOutput):
    #print(StaticOutput)
    staticRoute = {"Type": [], "Source": [], "Destination":[]}
    for line in staticOutput:
        if "S    " in line:
            staticRoute["Type"].append("Static")
            #print(line.replace(" ","").replace("S","").split("[")[0])
            staticRoute["Source"].append(line.replace(" ","").replace("S","").split("[")[0])
            #print(line.split("via ")[-1])
            staticRoute["Destination"].append(line.split("via ")[-1])
        if "S*   " in line:
            staticRoute["Type"].append("Static")
            #print(line.replace(" ","").replace("S*","").split("[")[0])
            staticRoute["Source"].append(line.replace(" ","").replace("S*","").split("[")[0])
            #print(line.split("via ")[-1])
            staticRoute["Destination"].append(line.split("via ")[-1])
    #print(staticRoute)           
    return staticRoute



def validateinput(staticOutput):
    staticCounter = 0
    for line in staticOutput:
        if "S*  " in line:
            staticCounter +=1
        if "S   " in line:
            staticCounter +=1
    if staticCounter == 0:
        return 1

def printErrToFile(msg,pathToCdpTextFile):
    file = pathToCdpTextFile.replace("howiproutestat", "howiprouteerror")
    with open(file, "w") as text_file:
        text_file.write(msg)



def main(pathToTextFile,pathToCsvFile):
    staticOutput = OpenStaticTextFile(pathToTextFile)

    #Validate input 0 = good 1 = bad
    validationbit = 0
    validationbit = validateinput(staticOutput)
    if validationbit == 1:
        #msg = "Something input file not valid"
        #printErrToFile(msg,pathToCdpTextFile)
        return

    try:
        staticRoute = makeStaticdict(staticOutput)
    except:
        msg = "Something happend with the pharsing of the input"
        printErrToFile(msg,pathToTextFile)
        return


    

    dictToStatic(staticRoute,pathToCsvFile)
if __name__ == "__main__":
    main()