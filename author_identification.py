#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import re
from collections import Counter

now = time.time()

#if We want to read from file
#line = open("himu.txt","r",encoding = "utf-16")
#list = line.read().split(' ');

line = "নিমকহারাম দাঁত ও চুল। প্রথমটা গেছে পড়ে, দ্বিতীয়টার কতক গেছে উঠে, আর কতক গেছে পেকে"
list = line.split();

fileName = ["Bankim Chandra Chatterjee.txt","Humayun Ahmed.txt","Kazi Nazrul Islam.txt","Rabindranath Tagore.txt","Saratchandra cattopadhy.txt"]
enc = ["utf-16","utf-8","utf-8","utf-8","utf-16"]

inputString = []
authName = []
dic = {}
dic2 = {}

#spliting and counting word
for i in range(0,len(fileName)):
    file = open(fileName[i],"r",encoding = enc[i])
    inputString.append(Counter(file.read().split(' ')))
    authName.append(fileName[i].split(".")[0])
    dic[authName[i]] = 0
    dic2[authName[i]] = 0
    

#Identifying text and summarize the best result
for token in list: 
    for i in range(0,len(inputString)):
        f = inputString[i][token]
        if ( f > 0):
            dic[authName[i]]=dic[authName[i]]+1;

# Max result prented
print("Found on : {0} and found {1}".format(max(dic,key=dic.get),dic[max(dic,key=dic.get)]))
print("Total Time needed:{0}".format(time.time()-now))
