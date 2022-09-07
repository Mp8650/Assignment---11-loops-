'''To print binary equivalent of a given decimal number. (do not
use bin() method)'''

print ("Enter a decimal number")
n=int(input())
l1=list()
while n>0:
    rem=n%2
    l1.append(rem)
    n=n//2
l1.reverse()
for e in l1:
    print(e,end='')







    