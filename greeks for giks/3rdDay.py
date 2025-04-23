def missingNum(arr):
        # code here
        arr.sort()
        for i in range(min(arr),max(arr)):
            if i not in arr:
                return i

print(missingNum([1,3,4,6,5]))            