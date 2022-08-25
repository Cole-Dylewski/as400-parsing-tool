import pandas as pd
import numpy as np
import random
import csv
import tkinter.filedialog as fd
import os
from csv import writer
from os import listdir
from os.path import isfile
from tkinter import *
from tkinter import ttk
import openpyxl as op

sourceFile = fd.askopenfilename()
#sourceFile = r'C:/Users/dylewskc/OneDrive - Automatic Data Processing Inc/Documents/Project Work/Conversions/TSG/Data/Employee Level/GGF Initial Data p1.txt'
print(sourceFile)

lines = []
with open(sourceFile, 'r') as f:
    lines = f.readlines()

lineCounter = 0
readToggle = True
recordDict={}
output = []
for i in range(15, 150):
    line = lines[i].strip()

    #lets build a list, of dictionarys
    #for each record, add a new dictionary item, and then add the complete dictionary to the list
    #create a dataframe from the list of dictionaries


    if(True):
        #build the dict
        if line[0:1] not in ['*','=',' '] and readToggle:
            #print(i,line, readToggle)
            if lineCounter == 0:
                    recordDict['employeeId'] = line[1:8].strip()
                    print("Employee ID: ", recordDict['employeeId'])
                    recordDict['employeeName'] = line[8:33].strip()
                    print("Employee Name: ", recordDict['employeeName'])
                    recordDict['maritalStatus'] = line[34:40].strip()
                    #print("Marital Status: ", recordDict['maritalStatus'])
                    recordDict['birthday'] = line[41:49]
                    #print("Birthday: ", recordDict['birthday'])
                    recordDict['fedEx'] = line[50:56].strip()
                    #print("Fed Ex: ", fedEx)
                    fitX = line[57:63]
                    #print("FIT-X: ", fitX)
                    dept = line[64:68]
                    #print("Department: ", dept)
                    union = line[69:74]
                    #print("Union Code: ", union)
                    jobCode = line[75:83]
                    #print("Job Code: ", jobCode)
                    autoIncome = line[84:86]
                    #print("Automatic Income: ", autoIncome)
            if lineCounter == 1:
                recordDict['timNo'] = line[0:7]
                #print("TIM No: ", timNo)
                add1 = line[7:33]
                #print("Address 1: ", add1)
                sex = line[33:40]
                #print("Sex: ", sex)
                hireDate = line[40:49]
                #print("Hire Date: ", hireDate)
                fdAdd = line[49:56]
                #print("FD Add: ", fdAdd)
                sitX = line[56:63]
                #print("SIT-X: ", sitX)
                specSenRate = line[63:83]
                #print("Spec Sen Rate: ", specSenRate)
                freqCode = line[83:85]
                #print("Frequency Code: ", freqCode)
                freqBaltoRec = line[86:109]
                #print("Frequency Balance to Recieve: ", freqBaltoRec)
            if lineCounter == 2:
                    tbd = line[0:36]
                    #print("Unknown data/TBD: ", tbd)
            if lineCounter == 3:
                    cityStateZip = line[1:27]
                    #print("City, State, Zip: ", cityStateZip)
                    pens = line[27:33]
                    #print("Pens: ", pens)
                    termCode = line[33:48]
                    #print("Term Code: ", termCode)
            if lineCounter == 4:
                    ssn = line[0:11]
                    #print("SSN: ", ssn)
                    i9 = line[26:27]
                    #print("I9: ", i9)
                    termDate = line[33:41]
                    #print("Term Date: ", termDate)
                    sdiX = line[49:50]
                    #print("SDI-X: ", sdiX)
            if lineCounter == 5:
                    phoneNbr = line[0:12]
                    #print("Phone Number: ", phoneNbr)
                    otherData = line[61:77]
                    #print("Other Data: ", otherData)
                # tempDf = [employeeId,employeeName,maritalStatus,birthday,fedEx,fitX,dept,union,jobCode,autoIncome,timNo,add1,sex,hireDate,fdAdd,sitX,specSenRate,freqCode,freqBaltoRec,tbd,cityStateZip,pens,termCode,ssn,i9,termDate,sdiX,phoneNbr,otherData]
                # print(tempDf)
                # want to build the employee record here...but it into a list and then append it to the previous list of employees so that we build the employee list with each interation through the loop

            lineCounter += 1
        #logic if we get to the end of a record
        if line[0:1].strip() == '*' and readToggle:
            #print("-------------------------------")
            output.append(recordDict)
            recordDict={}
            lineCounter = 0


        if line[0:1].strip() == '':
            #print("IS THIS EVEN HAPPENING?")
            readToggle = False

        if line[0:1] == '-' and not readToggle:
            readToggle = True

print(output)
outputDF= pd.DataFrame(data=output)
print(outputDF.to_string())