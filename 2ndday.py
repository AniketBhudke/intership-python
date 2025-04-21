#factorial program
# def factorial(n):
#    if n==0 or n==1:
#       return 1
#    elif n<0:
#         return "no factorial"
#    else:
#       return n*factorial(n-1)
# print(factorial(99))
#
#number=5
# def number(n):
#     if n==0:
#         return 0
#     else:
#         return n+number(n-1)
# print(number(-5))



#addition of two number
# def add(a,b):
#     if a==0:
#         return b
#     elif b==0:
#         return a
#     else:
#         return a-1 + b+1
# print(add(0,0))

#substractio of two number
# def sub(a,b):
#     if a==0:
#         return b
#     elif b==0:
#         return a
#     else:
#         return a-1 - b+1
# print(sub(5,8))    

#len of lst
# def length(lst):
#     if len(lst)==0:
#         return 0
#     elif len(lst)==1:
#         return 1
#     else:
#         return length(lst[::])
# lst=[11,22,33,45,6,7,89]
# print(length(lst))

#count array element

#maximum and minimium lst
def maxminvalue(lst,low,high):
    if low==high:
        return lst[low],lst[high]
    elif high==low+1:
        if lst[low]>lst[high]:
            return lst[high],lst[low]
        else:
            return lst[low],lst[high]
    else:
        mid=(low+high)//2
        min1,max1=maxminvalue(lst,low,mid)
        min2, max2 = maxminvalue(lst,mid+1,high)
        original_min=minimum(min1,min2)
        original_max=maximum(max1,max2)
        return original_min,original_max

def minimum(a,b):
    if (a<b):
        return a
    else:
        return b
def maximum(c,d):
    if (c>d):
        return c
    else:
        return d

lst=[1,2,3,44,5,66,78889,786,67]
low=0
high=len(lst)-1
print(maxminvalue(lst,low,high))
#

# Print numbers from 1 to N using recursion
# def printhnum(n):
#     if n==0:
#         return 0
#     else:
#         n=printhnum(n - n - 1)
#         return n
# print(printhnum(6))



#sum of all element
#print 1 to n