i=2
No =int(input("Enter Number"))
while i<No:
    if No%i==0:
        print("Not prime Number")
        break;
    i+=1
else:
    print("prime number")
