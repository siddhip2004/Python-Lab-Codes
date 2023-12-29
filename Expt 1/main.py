a=float(input("Enter the no. "))
n=a**0.5
print("Square Root of "+str(a)+" is "+str(n))


def sumarr(a,n):
    if(n==0):
        return 0
    else :
        return a[n-1] + sumarr(a,n-1)

num = int(input("Enter the no. of elements of the array: "))
arr=[]

print("Enter the elements:")
for i in range(0, num):
    ele = int(input(""))    
    arr.append(ele)
    
#print(arr)

b=sumarr(arr,num)
print("Sum of items in the array is: "+str(b))

num=int(input("Enter the no. upto which you want fibonacci series: "))
a=0
b=1 
c=0
count=0

print(a)
print(b)

while (count<num-2):
    c=a+b 
    print(c)
    a=b 
    b=c
    count = count+1

inp1 = int(input("Enter the value of lower limit: "))
inp2 = int(input("Enter the value of upper limit: "))

print("The prime numbers in range "+str(inp1)+" to "+str(inp2)+" are:")

for num in range (inp1, inp2+1):
    if (num>1):
        for i in range(2, num):
            if(num%i==0):
                break
        else:
            print(num, end=" ")



    
    
    
    