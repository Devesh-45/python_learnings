'''a=input()
if a==a[::-1]:
    print("palindrome")
else:
    print("not a plaindrome")'''

a=int(input())
if a%2==0 or a%3==0 and a%5==0:
    print("prime")
else:
    print("not a prime")
