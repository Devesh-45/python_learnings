A=str(input())
B=A[::-1]
if "Python" and "python" in A:
    print(B)
elif "Java" and "java" in A:
    print(A.upper())
else:
    print(A)
