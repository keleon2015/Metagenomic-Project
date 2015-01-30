#stats magic

number=raw_input("Give me numbers separated by spaces! ")
number=number.split()

#average

length=(len(number))
num1=list(map(int, number))
average=(sum(num1))/(length)
print ("The average is "+str(average))

#min/max
sort=sorted(num1)
print ("The minimum is "+str(sort[0]))
print ("The maximum is "+str(sort[length-1]))

#median
if length%2==0:
    a=((length+1)/2)
    b=((length-1)/2)
    median=((sort[a]+sort[b])/2)
    print ("The median is "+str(median))
if length%2!=0:
    c=(length/2)+1
    medodd=sort[c]
    print ("The median is "+str(medodd))
