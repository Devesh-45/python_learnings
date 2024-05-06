A=str(input())
if len(A)==13 or len(A)==12:
    if A[0:2].isalpha() and A[3:5].isdigit() and (A[6:7] or A[6:8]).isalpha and A[9:13].isdigit():
        print("Valid")
    else:
        print("Not valid")
else:
    print("Not Valid")
