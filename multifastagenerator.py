#bed fasta generator

import os
import re

os.chdir("/home/Shared/IBS574/Programming_Exercises_Data")

fhin=open("mm10_chr5_exons.bed",'r')
data=fhin.read()
fhin.close

fhin=open("mm10_chr5.fa",'r')
data2=fhin.read()
fhin.close

os.chdir("/home/kleon")

myfile=open('mm10_ch5_exons.fasta','w')
filename=myfile.name

data1=[]
data=data.split('\t')
for s in data:
    data1.append(str(s))
    
x=1
y=4
start=[]
end=[]
header=[]
start.append(data[x])
end.append(data[x+1])
header.append(data[x+2])
plus=set('+')
for s in data1:
    if plus & set(s):
        x+=5
        y+=5
        start.append(data[x])
        end.append(data[x+1])
        header.append(data[x+2])

data2=data2.split('\n')
data2=''.join(data2)
j=0
sequence=[]
for x in start:
    sequence.append(data2[int(start[j]):int(end[j])])
    j+=1
k=0
output=[]
for x in sequence:
    output.append(">"+header[k])
    output.append(sequence[k])
    k+=1

output='\n'.join(output)
myfile.write(output)
myfile.close()
print ( filename + " created!")

    

