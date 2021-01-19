import csv
from collections import OrderedDict



def importCSV(csvFile):

    with open(csvFile, 'rU') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')


        FileInAList = []
        for row in reader:
            FileInAList.append(row)
        headers = FileInAList[0] 
        body = FileInAList[1:]
        
        my_dictionary=OrderedDict()
        for header in headers:
            my_dictionary[header] = ()
    #for line in body:
    #    counter = 0
    #    
    #    for item in line:
    #        result[headers[counter]].append(item)
    #        counter +=1
    return my_dictionary

file = "C:\\Users\\MrRight\\Desktop\\csr1000v\\showinterfaces.csv"


dict1 =importCSV(file)
#crt.Dialog.MessageBox(str(dict1))
crt.Dialog.MessageBox(str(dict(dict1)))


#from collections import OrderedDict
#my_dictionary=OrderedDict()
#my_dictionary['foo']=3
#my_dictionary['aol']=1
#crt.Dialog.MessageBox(str(dict(my_dictionary)))
