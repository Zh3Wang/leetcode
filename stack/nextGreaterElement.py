#下一个更大的数
def nextGreaterElement(nums1,nums2):
    stack = []
    res = {}
    for x in nums2:
        while stack and stack[-1] < x:
            res[stack[-1]] = x
            del stack[-1]
        stack.append(x)
    
    for x in stack:
        res[x] = -1
    return [res[x] for x in nums1]
    

print(nextGreaterElement([4,5,6],[1,5,4,6]))
        