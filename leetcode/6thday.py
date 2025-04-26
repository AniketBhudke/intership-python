
def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            if nums.count(i)==1:
                return i
print(singleNumber([1,23,4,5,23,4,5]))      