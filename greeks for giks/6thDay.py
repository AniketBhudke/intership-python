def longest(arr, n):
        #Code Here
        mul=1
        for i in range(len(arr)):
            mul=mul*arr[i]
        return mul    
print(longest([1,2,3,4,5],5))