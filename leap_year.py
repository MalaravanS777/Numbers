a=int(input())
if a%400==0 and a%100==0:
    print("a leap year")
elif a%4==0 and a%100!=0:
    print("a leap year")
else:
    print("not a leap year")
