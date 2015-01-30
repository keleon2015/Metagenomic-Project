#cgislands

import os
import re

os.chdir("/home/Shared/IBS574/Programming_Exercises_Data")
fileinput=raw_input("Give me a file! ")
n=raw_input("Give me an n! ")
fileout=raw_input("What do you want your file called? ")

fhin=open('%s' %fileinput,'r')
data=fhin.read()
fhin.close

n=int(n)
os.chdir("/home/kleon")
myfile=open('%s' %fileout,'w')
filename=myfile.name

x=0
output=[]
j=2
k=0
sequence=[]
data=data.split('\n')
data=data[1:]
data=''.join(data)
for match in re.finditer(r"CG", data, re.I):
    aftercg=data[(match.end()):(match.end()+2)]
    precg=data[(match.start()-n):(match.start()-1)]
    postcg1=data[(match.end()+1):(match.end()+n)]
    precg=precg.lower()
    postcg1=postcg1.lower()
    while 'cg' in (data[(match.end())+k:(match.end()+j)]):
        j+=2
        k+=2
        postcg=data[(match.end()+j+1):(match.end()+j+1+n)]
        postcg=postcg.lower()
        if 'cg' not in precg:
            if 'cg' not in postcg:
                capmatch=data[(match.start()):(match.end()+j-2)]
                capmatch=capmatch.upper()
                output.append(precg+(capmatch)+postcg)
    j=2
    k=0        
    if 'cg' not in precg:
        if 'cg' not in postcg1:
            capmatch1=(data[(match.start()):(match.end())])
            capmatch1=capmatch1.upper()
            output.append(precg+capmatch1+postcg1)

output='\n'.join(output)
myfile.write(output)
myfile.close()
print ( filename + " created!")
