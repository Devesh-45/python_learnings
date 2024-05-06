N=input()
X=0
for i in N:
    X+=int(i)**3
if int(N)==X:
    print(X,"is a armstrong number.")
else:
    print("Not valid")
