import os

os.chdir("/home/Shared/IBS574/Programming_Exercises_Data")

fhin=open("tempDNA.fasta",'r')
data=fhin.read()
fhin.close()

header=(data.split('\n')[0][1:])
sequence=''.join(data.split('\n')[1:])

print("Header is: "+ header)
print("Sequence is: "+sequence)
print("Sequence length is: "+ str(len(sequence)))

gccount=sequence.count('G')
gccount+=sequence.count('C')

print("GC = "+str(float(gccount)))
