
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
def divinumber(a,b):
    if a==0:
        return 0
    else :
        return 1+ divinumber((a-b),b)

print(divinumber(12,2))