def totalFlips(number1,nuber2):
    flips=0
    while(number1>0 or number>0):
        t1=(number1 &1)
        t2=(number2&1)
        if(t1!=t2):
            flips+=1
        number1>>=1
        number2>>=1
    return flips
number1=int(input("Enter first number: "))
number2= int(input("Enter second number: "))
print("\n Number of flips needed: ", totalFlips(number1,number2))