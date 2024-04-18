Txt=input("Enter the sentence:")
Len=len(Txt)
if Len%2==0:
    X=Len//2
else:
    X=Len
Var=0
for i in range(1,X+1):
    Var+=i
print(Var)
