A=str(input())
if len(A)==10 or len(A)==9:
    if A[0:2].isalpha() and A[2:4].isdigit() and (A[4:6] or A[4:5]).isalpha and A[6:10].isdigit():
        print("Valid")
    else:
        print("Not valid")
else:
    print("Not Valid")
