'''To calculate sum of cubes of first N 
natural numbers'''
sum=0
n=int(input("Enter a number find sum of cubes natural no = "))
for i in range (1,n+1):
    print(i**3)
    sum =sum+(i**3)
print ("Sum of first natural no = ",sum)