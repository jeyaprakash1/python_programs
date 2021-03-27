# program for find factorial of given number

n=int(input("Enter Number"))
factorial=1
while n>0:
    factorial=factorial*n
    n-=1
print(factorial)
