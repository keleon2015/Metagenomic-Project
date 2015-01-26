import os

os.chdir("/home/Shared/IBS574/Programming_Exercises_Data")

fhin=open("Acinetobacter_baumannii_AB5075.fa",'r')
data=fhin.read()
fhin.close()

x=1
gctotal=0
seqtotal=0
previousline=0
while True:
    line=data.split('\n')[x]
    firstchar=(line[0])
    seqcount=line.count('a')
    seqcount+=line.count('t')
    seqcount+=line.count('g')
    seqcount+=line.count('c')
    gccount=line.count('g')
    gccount+=line.count('c')
    x+=1
    gctotal+=gccount
    seqtotal+=seqcount
    if firstchar == '>':
        
        difference=x-previousline
        y=x-difference
        
        line=data.split('\n')[y]
        chromosome=(line [5:11])
        print (str(chromosome)+'\t'+str(gctotal)+'\t'+"1"+'\t'+str(seqtotal))
        x+=1
        previousline=x-2
        gctotal=0
        seqtotal=0
    if firstchar == '':
        break
