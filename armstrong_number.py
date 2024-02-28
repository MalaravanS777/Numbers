n=int(input())
org=n
m=0
order=len(str(n))
while(n>0):
    a=n%10
    m+=a**order
    n=n//10
if m==org:
    print("It is an armstrong number.")
else:
    print("It is not an armstrong number.")
