# program to convert binary number to decimal number
# 0111->7 like this

No=int(input("Enter binary Number"))
decimal=0
i=0
while No>0:
    rem=No%10
    decimal=decimal+(rem*pow(2,i))
    No=No//10
    i+=1
else:
    print(decimal)

