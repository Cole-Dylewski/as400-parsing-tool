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


#sourceFile = fd.askopenfilename()
sourceFile=r'C:/Users/Franczyj/Downloads/GGF Initial Data p1.txt'
print(sourceFile)

lines = []
with open(sourceFile,'r') as f:
    lines = f.readlines()

lineCounter = 0
if lines[0:0] != " ":
    lineCounter = 0
    for i in range(15,50):
        line = lines[i].strip()
        if line[0:1] != "*":
            if line [0:1] != "=":
                if lineCounter == 0:
                    employeeId = line[1:8].strip()
                    print("Employee ID: ",employeeId)
                    employeeName = line[8:33].strip()
                    print("Employee Name: ",employeeName)
                    maritalStatus = line[34:40]
                    print("Marital Status: ", maritalStatus)
                    birthday = line[41:49]
                    print("Birthday: ", birthday)
                    fedEx = line[50:56]
                    print("Fed Ex: ", fedEx)
                    fitX = line[57:63]
                    print("FIT-X: ", fitX)
                    dept = line[64:68]
                    print("Department: ", dept)
                    union = line[69:74]
                    print("Union Code: ", union)
                    jobCode = line[75:83]
                    print("Job Code: ", jobCode)
                    autoIncome = line[84:86]
                    print("Automatic Income: ", autoIncome)
                if lineCounter == 1:
                    timNo = line[0:7]
                    print("TIM No: ", timNo)
                    add1 = line[7:33]
                    print("Address 1: ", add1)
                    sex = line[33:40]
                    print("Sex: ", sex)
                    hireDate = line[40:49]
                    print("Hire Date: ", hireDate)
                    fdAdd = line[49:56]
                    print("FD Add: ", fdAdd)
                    sitX = line[56:63]
                    print("SIT-X: ", sitX)
                    specSenRate = line[63:83]
                    print("Spec Sen Rate: ", specSenRate)
                    freqCode = line[83:85]
                    print("Frequency Code: ", freqCode)
                    freqBaltoRec = line[86:109]
                    print("Frequency Balance to Recieve: ", freqBaltoRec)
                if lineCounter == 2:
                    tbd = line[0:36]
                    print("Unknown data/TBD: ", tbd)
                if lineCounter == 3:
                    cityStateZip = line[1:27]
                    print("City, State, Zip: ", cityStateZip)
                    pens = line[27:33]
                    print("Pens: ", pens)
                    termCode = line[33:48]
                    print("Term Code: ", termCode)
                if lineCounter == 4:
                    ssn = line[0:11]
                    print("SSN: ", ssn)
                    i9 = line[26:27]
                    print("I9: ", i9)
                    termDate = line[33:41]
                    print("Term Date: ", termDate)
                    sdiX = line[49:50]
                    print("SDI-X: ", sdiX)
                if lineCounter == 5:
                    phoneNbr = line[0:12]
                    print("Phone Number: ", phoneNbr)
                    otherData = line[61:77]
                    print("Other Data: ", otherData)
                #tempDf = [employeeId,employeeName,maritalStatus,birthday,fedEx,fitX,dept,union,jobCode,autoIncome,timNo,add1,sex,hireDate,fdAdd,sitX,specSenRate,freqCode,freqBaltoRec,tbd,cityStateZip,pens,termCode,ssn,i9,termDate,sdiX,phoneNbr,otherData]
                #print(tempDf)
                #want to build the employee record here...but it into a list and then append it to the previous list of employees so that we build the employee list with each interation through the loop
                if lineCounter >= 6:
                    lineCounter = -1
                lineCounter += 1