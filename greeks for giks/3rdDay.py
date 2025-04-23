def missingNum(arr):
        # code here
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return total_sum - actual_sum
print(missingNum([1,3,4,6,5]))            