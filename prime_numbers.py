n=int(input())
print("The prime numbers between 1 and ",n)
for i in range(1,n):
    count=0
    for j in range(1,n+1):
        if(i%j==0):
            count+=1
    if(count==2):
        print(i,end=" ")
