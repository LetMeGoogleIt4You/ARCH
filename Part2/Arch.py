import glob
import sys
import os

#import sub files
pathToSubScript = "C:\\Users\\btl\\Documents\\git\\ARCH\\Part2\\"
sys.path.insert(0, pathToSubScript)

import cdpToCSV
import VersionToCSV
import InterfaceToCSV
import BgpToCSV
import isisToCSV
import staticRouteToCSV
import vrfToCSV
import VlanToCSV
import snmpToCSV
import InventoryToCSV
import platformToCSV

#set folder location with SecureCRT or Python
folder = crt.Dialog.Prompt ("Enter the folder location of the txt files")
#folder = input("Enter the folder location of the txt files")

#Format location
location = folder.replace('"\"' , '"\\"')

#Get a list of txt files
listOfFiles = glob.glob(location + "\\"+"*.txt")

#List of show commands
listOfFileNames = ["showcdpneidetail","showversion","showinterfaces","showipbgpneighbors","showisisneidet","showiproutestat","showvrfdet","showvlan","showsnmp","showinventory", "showplatform"]

#loop over list of file names
for listOfFileName in listOfFileNames:
    #Make path files pharsing
    pathToTextFile = location+"\\"+ listOfFileName+".txt" 
    pathToCsvFile = location+"\\"+ listOfFileName+".csv"

    #If files and accepet show showcommands in folder run pharsing
    if pathToTextFile in listOfFiles and listOfFileNames[0] in listOfFileName:
        cdpToCSV.main(pathToTextFile,pathToCsvFile)
    if pathToTextFile in listOfFiles and listOfFileNames[1] in listOfFileName:
        VersionToCSV.main(pathToTextFile,pathToCsvFile)
    if pathToTextFile in listOfFiles and listOfFileNames[2] in listOfFileName:
        InterfaceToCSV.main(pathToTextFile,pathToCsvFile)
    if pathToTextFile in listOfFiles and listOfFileNames[3] in listOfFileName:
        BgpToCSV.main(pathToTextFile,pathToCsvFile)
    if pathToTextFile in listOfFiles and listOfFileNames[4] in listOfFileName:
        isisToCSV.main(pathToTextFile,pathToCsvFile)
    if pathToTextFile in listOfFiles and listOfFileNames[5] in listOfFileName:
        staticRouteToCSV.main(pathToTextFile,pathToCsvFile)
    if pathToTextFile in listOfFiles and listOfFileNames[6] in listOfFileName:
        vrfToCSV.main(pathToTextFile,pathToCsvFile)
    if pathToTextFile in listOfFiles and listOfFileNames[7] in listOfFileName:
        VlanToCSV.main(pathToTextFile,pathToCsvFile)
    if pathToTextFile in listOfFiles and listOfFileNames[8] in listOfFileName:
        snmpToCSV.main(pathToTextFile,pathToCsvFile)
    if pathToTextFile in listOfFiles and listOfFileNames[9] in listOfFileName:
        InventoryToCSV.main(pathToTextFile,pathToCsvFile)
    if pathToTextFile in listOfFiles and listOfFileNames[10] in listOfFileName:
        platformToCSV.main(pathToTextFile,pathToCsvFile)

#Clean up the pyc files
listOfPycFiles = glob.glob(pathToSubScript+"*.pyc")
for pycFile in listOfPycFiles:
    os.remove(pycFile)