#Hailstone Sequence

number=input("Give me a number greater than zero!")

if number<=0:
        number=input("READ THE INSTRUCTIONS: Give me a number greater than zero!")
        
while (number!=1):
    if number%2==0:
        number=number/2
    else:
        number=(number*3)+1
    print number
    if number ==0:
        break

    
