n=input("Enter three numbers:")
a,b,c =n.split(" ")
if a<b:
    if a<c:
        print(a)
    else:
        print(c)
elif b<c:
    print(b)
else:
    print(c)
