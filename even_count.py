n=int(input("Enter a number:"))
count=0
for i in range(n):
    if(i%2==0):
        print(i,end=" ")
        count+=1
print("\n",count)


