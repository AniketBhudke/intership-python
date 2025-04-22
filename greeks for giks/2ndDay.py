def subarraySum(arr, n, target):
    start = 0
    curr_sum = 0

    for end in range(n):
        curr_sum += arr[end]

        while curr_sum > target and start < end:
            curr_sum -= arr[start]
            start += 1

        if curr_sum == target:
            return [start + 1, end + 1]  # 1-based indexing

    return [-1]
arr=[11,2,3,4,5,6,7,8]
n=3
target=9
print(subarraySum(arr, n, target)
)