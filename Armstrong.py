# program for find given Number is armstrong or not

No=int(input("Enter Number")) 
Arm=0
Num=No
while No>0: 
    rem=No%10
    Arm=Arm+(rem*rem*rem)
    No=No//10
print(Arm)
if Arm==Num:
    print("Armstrong")
else:
    print("Not Armstrong")


 
