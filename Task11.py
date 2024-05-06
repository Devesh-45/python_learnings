num = list(map(int,input().split()))
n1=0
n2=1
for i in range(2, 11):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
a=((((n3+2)-3)*6)/7)
print(round(a,2))


