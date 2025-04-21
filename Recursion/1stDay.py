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