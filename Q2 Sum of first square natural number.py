'''To calculate sum of squares of first N 
natural numbers'''
sum=0
n=int(input("Enter a number find sum of natural no = "))
for i in range (1,n+1):
    print(i**2)
    sum =sum+(i**2)
print ("Sum of first natural no = ",sum)