def getSecondLargest(arr):
        # Code Here
        maxv=max(arr)
        arr.sort(reverse=True)
        sval=arr.count(maxv)
        if len(arr)!=sval:
            return arr[sval]
        return -1    
arr=[1,11,2,3,4,5,66,6,6,7,7,66,66]
print(getSecondLargest(arr))