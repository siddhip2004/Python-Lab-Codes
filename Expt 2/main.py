lst=[1,2,3,4,5]
lst2=["a","b","c","d","e"]
lst3=[[1,2],[3,4],[5,7]]

#SQUARING THE ELEMENTS OF ORIGINAL LIST using for loop

# new_lst=[]
# for i in lst:
#     new_lst.append(i*i)
# print("Original list is "+str(lst))
# print("List after squaring numbers in original list is "+str(new_lst))


#SQUARING THE ELEMENTS OF ORIGINAL LIST using List comprehension

# new_lst1=[i*i for i in lst]
# print("List after squaring original list is "+str(new_lst1))

# new_lst2=[i for i in range(50) if i%10 == 0]
# print("List after finding multiples of 10 from 0 to 50 is "+str(new_lst2))

# new_lst3=[i for i in range(80) if i%10 == 0 and i%7 == 0]
# print("List after finding multiples of 10 and 7 from 0 to 80 is "+str(new_lst3))

# new_lst4=[i for i in "siddhi"]
# print("List containing letters of string are "+str(new_lst4))


# new_lst41=[(i,j )for i in lst for j in lst2]
# new_lst4 = [[(i,j) for j in lst2] for i in lst]
# print(new_lst4)
# print(new_lst41)

# new_lst5=[[j[i] for j in lst3]for i in range(len(lst3[0]))]
# print(new_lst5)

# new_lst6 = list(map(lambda i: i*10, [i for i in lst]))
# print(new_lst6)

# import time 

# new_lst7=[]
# new_lst8=[]

# def for_loop(n):
#     for i in range(n): new_lst7.append(i*10)
#     #print(new_lst7)

# def List_comprehension(n):
#     new_lst8 = [i*10 for i in range(n)] 
#     #print(new_lst8)
    
# begin = time.time()
# for_loop(10**7)
# end = time.time()

# print("Time taken by the for loop is: ", round(end-begin , 2))

# begin = time.time()
# List_comprehension(10**7)
# end = time.time()

#print("Time taken by list comprehension is: ",  round(end-begin , 2))

lst4 = [31,24,55,66]
def sum(n):
    summ=0
    for i in str(n):
        summ = summ + int(i) 
    return summ
    
new_lst9 = [sum(i) for i in lst4 if (i & 1)]

print(new_lst9)
    


