def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if target in nums:
                if nums[i]==target:
                    return i
            else:
                nums.append(target)
                nums.sort()
                if target in nums:
                    return nums.index(target)
nums=[11,2,3,4,5,66,77,8]
target=9
print(searchInsert(nums, target))