class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result=""
        carry = 0
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        for i in range(max_len - 1, -1, -1):
            total = carry
            total += int(a[i]) + int(b[i])
            result = str(total % 2) + result
        
            carry = total // 2

    
        if carry:
            result = '1' + result

        return result 