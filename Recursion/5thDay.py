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

def powerNumber(a,b):
    if b==0:
        return a
    else:
        return a * powerNumber(a,b-1)
print(powerNumber(6,2))