n=int(input())
count=0
while(n>0):
    a=n%10
    count+=1
    n=n//10
print("The number of digits in a number:",count)
