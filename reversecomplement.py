#Reverse Complement Generator

seq=raw_input("Give me a sequence!")

y=[]
seq=seq.upper()
seq=list(seq)
revdic={'G':'C','A':'T', 'T':'A','C':'G'}
for list in seq:
    for i in list:
        y.append(revdic[i])
print ''.join(y)


