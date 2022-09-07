'''To print octal equivalent of a given decimal number. (do not
use bin() method)'''

n=int(input("Enter a decimal number to change in Octal="))
l1=list()
while n>0:
    rem=n%8
    l1.append(rem)
    n=n//8
l1.reverse()
for e in l1:
    print(e,end='')
    