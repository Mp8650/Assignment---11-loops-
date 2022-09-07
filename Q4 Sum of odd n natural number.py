'''To calculate sum of first N odd
natural numbers'''
sum=0
n=int(input("Enter a number find sum of odd natural no = "))
for i in range (1,n*2,2):
     print(i)
     sum=sum+i
print ("Sum of first odd natural no = ",sum)