# fibbonacci series without third variable 

f,s=-1,1
count=int(input("Enter count"))
while count>0:
    print(f+s,end=" ")
    s=f+s
    f=s-f
    count-=1   
    
    
     
