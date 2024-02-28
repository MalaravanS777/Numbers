n=int(input())
count=1
for i in range(2,n+1):
    if n%i==0:
        print(i,end=" ")
        count+=1
print("\n")
print(count)      
