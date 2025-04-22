def majorityElement(lst,maxcount):
    for i in range(len(lst)):
        if lst.count(lst[i])>maxcount:
            maxcount=lst.count(lst[i])
    return maxcount
lst=[3, 3,3,3,3,3,3, 4, 2, 4, 4, 2, 4, 4]
maxcount=0
print(majorityElement(lst,maxcount))

