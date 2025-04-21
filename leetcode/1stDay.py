def firstOccurance( haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if needle in haystack:
        return haystack.index(needle)
    return -1  
haystack="sadbutsad"  
needle="sad"
print(firstOccurance(haystack,needle))