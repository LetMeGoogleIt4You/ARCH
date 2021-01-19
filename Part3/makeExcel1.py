import sys, os
import glob
import csv
import re

#pathToXlsxwriter = "F:\\AKR\\Scripts\\"
#sys.path.insert(0, pathToXlsxwriter)

import xlsxwriter


#sort list
def sortCSVFiles(listOfFiles):
    sortList = []
    for file in listOfFiles:
        if "showversion" in file:
            sortedList.append(file)
    for file in listOfFiles:
        if "showcdpneidetail" in file:
            sortedList.append(file)
    for file in listOfFiles:
        if "showinterfaces" in file:
            sortedList.append(file)
    for file in listOfFiles:
        if "showipbgpneighbors" in file:
            sortedList.append(file)      
    for file in listOfFiles:
        if "showisisneidet" in file:
            sortedList.append(file)
    for file in listOfFiles:
        if "showiproutestat" in file:
            sortedList.append(file)
    for file in listOfFiles:
        if "showvrfdet" in file:
            sortedList.append(file)
    for file in listOfFiles:
        if "showvlan" in file:
            sortedList.append(file)
    for file in listOfFiles:
        if "showsnmp.csv" in file:
            sortedList.append(file)
    for file in listOfFiles:
        if "showinventory" in file:
            sortedList.append(file)
    for file in listOfFiles:
        if "showplatform" in file:
            sortedList.append(file)
    return sortedList


#import CSV file and make a dict
    def importCSV(csvFile):
        with open(csvFile, 'rU') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')



            #FileInAList = []
            #for row in reader:
            #    FileInAList.append(row)
            #
            #headers = FileInAList[0] 
            #body = FileInAList[1:]
            #result = {}
            #
            #for header in headers:
            #    result[header] = []
            #
            #for line in body:
            #    counter = 0
            #    for item in line:
            #        result[headers[counter]].append(item)
            #        counter +=1
            #crt.Dialog.MessageBox(str(result))
            return result


#add dict to excelsheet
def makeExcelTabel(dataDict,rowStarter):
    rowTyper = rowStarter
    columnType = 0
    dataDictLenght = 0
    #Header
    for key in dataDict:
        #Write header
        worksheet1.write(rowTyper, columnType, key)
        rowTyper += 1
        #Write column of header
        for value in dataDict[key]:
            worksheet1.write(rowTyper, columnType, value)
            rowTyper += 1
        rowTyper = rowStarter
        columnType += 1
 

#Select to the folders with the CSV files
folder = crt.Dialog.Prompt("Enter the folder location of the CSV files:")

#List out all the CSV files in folder
location = folder.replace('"\"' , '"\\"')
listOfFiles = glob.glob(location + "\\"+"*.csv")

#Sort list
sortedList =  []
sortedList = sortCSVFiles(listOfFiles)

#Set filename
filename ="\\" + sortedList[1].split("\\")[-2]+"-overview.xlsx"

#make a excel file and a sheet
workbook = xlsxwriter.Workbook(location + filename)
worksheet1 = workbook.add_worksheet()


#add tabels to worksheet1 
rowStarter = 0
for csvFile in sortedList:
    dataDict = importCSV(csvFile)
    makeExcelTabel(dataDict,rowStarter)
    
    for key, value in dataDict.items():
        lenght = len(value)
    rowStarter += lenght + 2
    
workbook.close()

#Clean up the pyc fils
#listOfPycFiles = glob.glob(pathToXlsxwriter+"*.pyc")
#for pycFile in listOfPycFiles:
#    os.remove(pycFile)