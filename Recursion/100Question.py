# Find the Missing Number in an Array
# Input: [1, 2, 4, 5, 6]
# Output: 3

# def missingNumber(lst):
#     for i in range(min(lst),max(lst)):
#         if i not in lst:
#             return i

# lst=[1, 2,3, 5]
# print(missingNumber(lst))         



#find dupliacte number
# Input: [3, 1, 3, 4, 2]
# Output: 3

# def duplicatenumber(lst,lst1):
#     for i in range(len(lst)):
#         if lst.count(lst[i])>=2:
#             lst1.append(lst[i])
#     return set(lst1)
# lst1=[]
# lst=[3, 1, 3, 4, 2]
# print(duplicatenumber(lst,lst1))

# Find the Majority Element (Moore’s Voting Algorithm)
# Example:
# Input: [3, 3, 4, 2, 4, 4, 2, 4, 4]
# Output: 4

# def majorityElement(lst,maxcount,maxnumber):
#     for i in range(len(lst)):
#         if lst.count(lst[i])>maxcount:
#             maxcount=lst.count(lst[i])
#             maxnumber=lst[i]
#     return maxcount,maxnumber
# lst=[3, 3,3,3,3,3,3, 4, 2, 4,5,5,5,5,5,5,5,5,5,5, 4, 2, 4, 4]
# maxcount=0
# maxnumber=0
# print(majorityElement(lst,maxcount,maxnumber))

# Two Sum Problem
# Example:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]

# def twoSumProblem(lst,target):
#     for i in range(len(lst)):
#         for j in range(i+1,len(lst)):
#             if lst[i]+lst[j]==target:
#                 return i,j
# lst= [ 11, 2,15,7]
# target = 9           
# print(twoSumProblem(lst,target))

# Move Zeroes to the End
# 13.Input: [0, 1, 2, 0, 3, 4]
# Output: [1, 2, 3, 4, 0, 0]

def movezeroEnd(lst):
    for i in range(len(lst)):
        if lst[i]==0:
            lst.remove(lst[i])
            lst.append(0)
    print(lst)
print(movezeroEnd( [0, 1, 2, 0, 3, 4]))           