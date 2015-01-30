#python lab 1

import os

os.chdir("/home/Shared/IBS574/Programming_Exercises_Data")

fhin=open("python_lab.fastq",'r')
data=fhin.read()
fhin.close

os.chdir("/home/kleon")

myfile=open('python_lab.fasta','w')
filename=myfile.name

x=0
output=[]
data=data.split('\n')
for line in data:
    if line=='':
        break
    firstchar=line[0]
    if firstchar=='@':
        output+=([line]+[data[x+1]])
    x+=1

output='\n'.join(output)
myfile.write(output)
myfile.close()
print ( filename + " created!")



        
            
