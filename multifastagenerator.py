#bed fasta generator

import os
import re

os.chdir("/home/Shared/IBS574/Programming_Exercises_Data")

fhin=open("mm10_chr5_exons.bed",'r')
data=fhin.read()
fhin.close

os.chdir("/home/kleon")

data1=[]
data=data.split('\t')
for s in data:
    data1.append(str(s))
    
x=1
y=4

print data1[x:y]
plus=set('+')
for s in data1:
    if plus & set(s):
        x+=5
        y+=5
        print data[x:y]
