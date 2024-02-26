n=input("Enter the numbers:").split(" ")
for i in range(len(n)-1):
    for j in range(i+1,len(n)):
        if(int(n[i])>int(n[j])):
            num=n[i]
            n[i]=n[j]
            n[j]=num
print(n)
