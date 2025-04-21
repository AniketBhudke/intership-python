#recursion example
# #addition of two number
# #logic-1
# # def add(a, b):
# #     if a == 0:
# #         return b
# #     else:
# #         return add(a - 1, b + 1)

# # result = add(2, 3)
# # print("Addition is:", result)

# #logic-2
# # def add(a, b):
# #     if b == 0:
# #         return a
# #     else:
# #         return add(a + 1, b - 1)

# # result = add(2, 3)
# # print("Addition is:", result)

# def multiply(a, b):
#     if b == 0:
#         return 0
#     else:
#         return a + multiply(a, b - 1)

# result = multiply(4, 3)
# print("Multiplication is:", result)


# def divide(a, b):
#     if b == 0:
#         return "Error: Division by zero"
#     if a < b:
#         return 0
#     else:
#         return 1 + divide(a - b, b)
#
# result = divide(10, 2)
# print("Division is:", result)  # Output: 5

# def odd_numnm(lst):
#     ans=0
#     for val  in lst:
#         ans^=val
#         return ans
    
# lst=[1,2,3,4,5,-6,-9]
# res=odd_numnm(lst)
# print(res)


# def minmaxproblem(lst,minv,maxv):
#     if len(lst)==1:
#         maxv=lst[0]
#         minv=lst[0]
#         return minv,maxv
#     elif len(lst)==2:
#         if lst[0]>lst[1]:
#             maxv=lst[0]
#             minv=lst[1]
#             return maxv,minv
#         else:
#             maxv=lst[1]
#             minv=lst[0]
#             return maxv,minv
#     else:
#         mid=
        


# lst=[1,3,5,6,8,2,-2,4,99]
# minmaxproblem(lst)    


# def commonvalue(lst1,lst2):
#     lst1.sort()
#     lst2.sort()
#     dict1={}
#     for i in range(len(lst1)):
#         dict1[lst1[i]]=lst2[i]
#     return dict1
#
# lst1=[1,2,44,5,77,4]
# lst2=[2,1,4,44,7,6]
# res=commonvalue(lst1,lst2)
# print(res)

# def merging(lst1,lst2):
#     i=0
#     j=0
#     ans_list=[]
#     while(i<=len(lst1) or j<=len(lst2)):
#         if i!=len(lst1) or j!=len(lst2):
#             if lst1[i]<lst2[j]:
#                 ans_list.append(lst1[i])
#                 i+=1
#             else:
#                 ans_list.append(lst2[j])
#                 j+=1
#     return ans_list
# lst1=[11,2,3,4,5]
# lst2=[22,33,44,55,66]
# print(merging(lst1,lst2))

# def powerNumber(a,b):
#     if b==0:
#         return a
#     else:
#         return a * powerNumber(a,b-1)
# print(powerNumber(6,2))



#sum of all element
# def sumlistelement(lst):
#     s=0
#     for i in range(len(lst)):
#         s=s+lst[i]
#     return s
#
# lst=[11,2,3,4,5,6,77,8]
# res=sumlistelement(lst)
# print(res)

#print 1 to n
# def number(n):
#     if n==0:
#         return 0
#     else:
#         print(n)
#         number(n-1)
# print(number(10))


#sir jevh aaapn print krt
# def sequential_element(lst,key):
#     for i in range(len(lst)):
#         if lst[i]==key:
#             return True,i
#     return False
#
# lst=[11,22,3,4,5,6,7,8,9]
# key=int(input("Enter the Element which ou want to search:"))
# print(sequential_element(lst,key))

#recursive approach

# def multiplication(a,b):
#     if b==0:
#         return b
#     else:
#         return a+multiplication(a,(b-1))
# print(multiplication(2,3))

#division of number
# def divinumber(a,b):
#     if a==0:
#         return 0
#     else :
#         return 1+ divinumber((a-b),b)

# print(divinumber(12,2))

#
# def chocalte(lst,low,high):
#     while low<high:
#         if lst[low]>lst[high]:
#             low+=1
#         else:
#             high-=1
#     return lst[low]
# lst=[11,2,3,4,5,677]
# low=0
# high=len(lst)-1
# print(chocalte(lst,low,high))

#
# lst1=[11,2,30,33,44,5]
# lst2=[22,66,8,9,99,90]
# lst3=[]

# def merging(lst1,lst2):
#     i=0
#     j=0
#     ans_list=[]
#     while(i<=len(lst1) or j<=len(lst2)):
#         if i!=len(lst1) or j!=len(lst2):
#             if lst1[i]<lst2[j]:
#                 ans_list.append(lst1[i])
#                 i+=1
#             else:
#                 ans_list.append(lst2[j])
#                 j+=1
#     return ans_list
# lst1=[11,2,3,4,5]
# lst2=[22,33,44,55,66]
# print(merging(lst1,lst2))

# def powerNumber(a,b):
#     if b==0:
#         return a
#     else:
#         return a * powerNumber(a,b-1)
# print(powerNumber(6,2))