lst=[1,2,3,4,5]
lst1=[1,2,3,4,5]
#using 1 parameter
# def square(n):
#     return (n**2)
    
# new_lst1=list(map(square , lst))
# print(new_lst1)

#using more parameters

# def power(x,y):
#     return(x**y)
# new_lst2=list(map(power, lst, lst1))           #new_lst2 = list(map(pow, lst, lst1))
# print(new_lst2)
    
# lst3=["druhi", "gauri", "richa", "siddhi"]
# new_lst4=list(map(len, lst3))
# print(new_lst4)

from functools import reduce

# def multiply(a,b):
#     x=a*b 
#     return x

# lst2=[1,2,3]
# new_lst5=reduce(multiply,lst2)
# print(f"Multiplication of digits of list is:  {new_lst5}")

# new_lst6=reduce(lambda x,y: x*y, lst2)
# print(f"Multiplication of digits of list is:  {new_lst6}")

# def check_num(num):
#     if(num%2 == 0):
#         return True
#     else:
#         return False 

# even_num = filter(check_num, lst)
# new_lst7 = list(even_num)
# print(f"Even numbers in the list {lst} are: {new_lst7}")

# lst4 = ['a','e','i','o','f','h','k']

# def check_vowel(v):
#     if(v=='a' or v=='e' or v=='i' or v=='o' or v=='u'):
#         return True
#     else:
#         return False
# vowel=filter(check_vowel, lst4)
# new_lst8 = list(vowel)
# print(f"Vowels in our list {lst4} are: {new_lst8}")

# vowel=filter(lambda v:v=='a' or v=='e' or v=='i' or v=='o' or v=='u', lst4)
# new_lst9 = list(vowel)
# print(f"Vowels in our list {lst4} are: {new_lst9}")

lst5 = [1,0,'c',True,False,"siddhi"]
check_none = filter(None, lst5)
new_lst10 = list(check_none)
print(f"After using none function for the list {lst5}, output is: {new_lst10}")

