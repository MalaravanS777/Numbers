def fact(n):
    if n==0:
        return 1
    elif n==1:
        return n
    else:
        return n*fact(n-1)
n=int(input())
fac = fact(n)
print("Factorial of ",n," is ",fac)
