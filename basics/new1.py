#wap to print a fabonacci series upto n terms
#wap to print armstrong number upto n terms
#wap to print the sum of digits of a number.
#wap to sort a list entered by the user without sort function
num = 10
n1,n2 = 0,1
print("Fabonacci Series:",n1,n2, end=" ")
for i in range(2,num):
    n3 = n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")

print()
