def subarraySum( arr, target):
        # code here
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]+arr[j]==target:
                    return [i,j]
        return [-1]
arr=[1,22,3,4,5,66,77,8]
target=88
print(subarraySum( arr, target))
