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

# def majorityElement(lst,maxcount):
#     for i in range(len(lst)):
#         if lst.count(lst[i])>maxcount:
#             maxcount=lst.count(lst[i])
#     return maxcount
# lst=[3, 3,3,3,3,3,3, 4, 2, 4, 4, 2, 4, 4]
# maxcount=0
# print(majorityElement(lst,maxcount))

