'''To count digits in a given number'''
count=0
n=int (input("enter a number = "))
while n>0:
    rem=n%10
    count+=1
    n=int(n/10)
print("The number of digits = ",count)    