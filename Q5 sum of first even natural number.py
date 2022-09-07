'''To calculate sum of first N even
natural numbers'''
sum=0
n=int(input("Enter a number find sum of even natural no= "))
for i in range (2,n*2,2):
     print(i)
     sum=sum+i
print ("Sum of first even natural no = ",sum)