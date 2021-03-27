# program for reverse a given Number and check reversed and given Number 
# are equal or not

No=int(input("Enter Number")) 
reverse=0
Num=No
while No>0: 
    rem=No%10
    reverse=reverse*10+(rem)
    No=No//10
print(reverse)
if reverse==Num:
    print("palindrome")
else:
    print("Not palindrome")


 
