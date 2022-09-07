'''To calculate sum of digits of a
given number'''
sum=0
n=int (input("enter a number"))
while n>0:
    rem=n%10
    sum=sum+rem
    n=int(n/10)
print(sum)
    