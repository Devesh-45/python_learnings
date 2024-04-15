a=int(input("Enter a num1:"))
b=int(input("Enter a num2:"))
c=int(input("Enter a num3:"))
d=max(a,b,c)
for i in range(1,d+1):
    if i%a==0 and i%b==0:
        print(i)
    
    
