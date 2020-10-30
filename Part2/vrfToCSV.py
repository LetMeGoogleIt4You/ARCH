import csv

#pathToCsvFile = "D:\\router\\showvrf.csv"    
#pathToTextFile = "D:\\router\\showvrfdet.txt"    

def OpenTextFile(path):
    with open(path) as text_file:
        text_file = text_file.read().splitlines()
        return text_file

def dictToCsv(results,resultsFile):
    with open(resultsFile, 'w') as csvfile:
        #print(results)
        filewriter = csv.writer(csvfile, delimiter=',',lineterminator='\r')
        count = 0
        filewriter.writerow(["Name","VRFId","DefaultRD","Interfaces","Protocols","ExportVPN","ImportVPN"])
        for item in range(0,len(results["Name"])):
            filewriter.writerow([results["Name"][count],results["VRFId"][count],results["DefaultRD"][count],results["Interfaces"][count],results["Protocols"][count],results["ExportVPN"][count],results["ImportVPN"][count]])
            count +=1

def makeVrfDict(showVrf):

   
    VrfStatus = {"Name":[],"VRFId":[],"DefaultRD":[],"Interfaces":[],"Protocols":[],"ExportVPN":[],"ImportVPN":[]}
    
    #print(showVrf)
    vrflist = []
    
    count = 0
    vrfCount = 0
    
    
    #iterate over all lines in the showInterface list
    for line in showVrf:
        if "VRF Id" in line:
            VrfStatus["Name"].append(line.split("VRF ")[1].split(" ")[0])
            #print(line.split("VRF ")[1].split(" ")[0])
            VrfStatus["VRFId"].append(line.split("VRF Id = ")[1].split(")")[0])
            #print(line.split("VRF Id = ")[1].split(")")[0])
            VrfStatus["DefaultRD"].append(line.split("default RD ")[1].split(";")[0])
            #print(line.split("defaultRD ")[1].split(";")[0])
            #print(showVrf[count+3])
            #print(line)
            #print(showVrf[count+1])
            if "Interfaces" in showVrf[count+1]:
                    #print(showVrf[count+4].split(" "))
                    interfaceCount = 0
                    vrfInterface = ""
                    for interface in showVrf[count+4].split(" "):
                        if 1 < len(interface):
                            vrfInterface = vrfInterface+interface+" "
                        interfaceCount +=1
                    #print(mylist)
                    #print(vrfInterface)
                    VrfStatus["Interfaces"].append(vrfInterface)
            if "Interfaces" in showVrf[count+3]:
                    #print(showVrf[count+4].split(" "))
                    interfaceCount = 0
                    vrfInterface = ""
                    for interface in showVrf[count+4].split(" "):
                        if 1 < len(interface):
                            vrfInterface = vrfInterface+interface+" "
                        interfaceCount +=1
                    #print(mylist)
                    #print(vrfInterface)
                    VrfStatus["Interfaces"].append(vrfInterface)
            if "No interfaces" in showVrf[count+3] or "No interfaces" in showVrf[count+1]:
                VrfStatus["Interfaces"].append("N/A")
                
                #print("N/A")
        
        if "Address family ipv4 " in line:
            if "Address family ipv4 unicast (" in line:
                VrfStatus["Protocols"].append("IPv4 Unicast")
            if "Address family ipv4 (" in line:
                VrfStatus["Protocols"].append("IPv4 Unicast")
            #print("IPv4 Unicast")
            #print(showVrf[count+2])

            if count + 5 > len(showVrf):
                break
            #print(showVrf[count+2])
            if "  Export VPN" in showVrf[count+1]:
                #print(showVrf[count+3].split(" "))
                #print(line)
                RTExportCount = 0
                vrfRTExport = ""
                for RTExport in showVrf[count+2].split(" "):
                    if 1 < len(RTExport):
                        vrfRTExport = vrfRTExport+RTExport+" "
                    RTExportCount +=1
                VrfStatus["ExportVPN"].append(vrfRTExport)
                #print(vrfRTExport)
            if "  Export VPN" in showVrf[count+2]:
                #print(showVrf[count+3].split(" "))
                #print(line)
                RTExportCount = 0
                vrfRTExport = ""
                for RTExport in showVrf[count+3].split(" "):
                    if 1 < len(RTExport):
                        vrfRTExport = vrfRTExport+RTExport+" "
                    RTExportCount +=1
                VrfStatus["ExportVPN"].append(vrfRTExport)
                #print(vrfRTExport)
            if "No Export VPN" in showVrf[count+2] or "No Export VPN" in showVrf[count+1]:
                VrfStatus["ExportVPN"].append("N/A")
                #print("N/A")
            
            if "  Import VPN" in showVrf[count+3] and "RT" in showVrf[count+4]:
                RTImportCount = 0
                vrfRTImport = ""

                #print(showVrf[count+5].split(" "))
                for RTImport in showVrf[count+4].split(" "):
                    #print(RTImport)
                    if 1 < len(RTImport):
                        #print(RTImport)
                        vrfRTImport = vrfRTImport+RTImport+" "
                    RTImportCount +=1
                VrfStatus["ImportVPN"].append(vrfRTImport)
                #print(vrfRTImport)


            if "  Import VPN" in showVrf[count+4] and "RT" in showVrf[count+5]:
                RTImportCount = 0
                vrfRTImport = ""

                #print(showVrf[count+5].split(" "))
                for RTImport in showVrf[count+5].split(" "):
                    #print(RTImport)
                    if 1 < len(RTImport):
                        #print(RTImport)
                        vrfRTImport = vrfRTImport+RTImport+" "
                    RTImportCount +=1
                VrfStatus["ImportVPN"].append(vrfRTImport)
                #print(vrfRTImport)
            
            
            if "No Import VPN" in showVrf[count+3] or "No Import VPN" in showVrf[count+2]:
                VrfStatus["ImportVPN"].append("N/A")
            
            
        
        count += 1

    #print(VrfStatus["Name"])
    #print(VrfStatus["DefaultRD"])
    #print(VrfStatus["VRFId"])
    #print(VrfStatus["Interfaces"])
    #print(VrfStatus["Protocols"])
    #print(VrfStatus["ExportVPN"])
    #print(VrfStatus["ImportVPN"])
    #print(VrfStatus)
    return VrfStatus


def validateinput(showVrf):
    if len(showVrf) < 5:
        return 1
    for line in showVrf:
        if "% Invalid input detected" in line:
            return 1


def printErrToFile(msg,pathToTextFile):
    file = pathToTextFile.replace("showvrfdet", "showvrferror")
    with open(file, "w") as text_file:
        text_file.write(msg)

def main(pathToTextFile,pathToCsvFile):
    showVrf = OpenTextFile(pathToTextFile)


    #Validate input 0 = good 1 = bad
    validationbit = 0
    validationbit = validateinput(showVrf)
    if validationbit == 1:
        #msg = "Something input file not valid"
        #printErrToFile(msg,pathToTextFile)
        return
        
    

    #Make a vrf dictionary
    try:
        VrfStatus = makeVrfDict(showVrf)
    except:
        msg = "Something happend with the pharsing of the input"
        printErrToFile(msg,pathToTextFile)
        return

    
    dictToCsv(VrfStatus, pathToCsvFile)

if __name__ == "__main__":
    main()
    #main(pathToTextFile,pathToCsvFile)
