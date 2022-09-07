'''To calculate factorial of a given number'''
fact=1
i=1
n=int(input("Enter a number = "))
while i<=n:
    fact=fact*i
    i+=1
print (fact)