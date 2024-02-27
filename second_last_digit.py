n=int(input("Enter a number:"))
i=0
while n>0:
    last_digit=n%10
    n=n//10
    if i==1:
        break
    i+=1
print("\nThe last digit of a number is ",last_digit)
