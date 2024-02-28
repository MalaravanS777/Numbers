n=int(input())
org=n
rev=0
while(n>0):
    a=n%10
    rev=(rev*10)+a
    n=n//10
print(rev)
if rev==org:
    print("Palindrome")
else:
    print("not Palindrome")
