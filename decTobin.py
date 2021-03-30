# program to convert  decimal number to  binary

no=int(input("Enter a number"))
binary=''
while no>0:
    rem=no%2
    binary=str(rem)+binary
    no=no//2
else:
    print(binary)
    
