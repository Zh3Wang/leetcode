""""""
"""
    删除排序数组中的重复项
    
    【示例】
    给定 nums = [0,0,1,1,1,2,2,3,3,4],

    函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
    
    你不需要考虑数组中超出新长度后面的元素。
"""


class Solution:

    def __init__(self):
        pass

    """
        数组是有序的，说明只需要比较相邻元素之间的大小
    """
    @staticmethod
    def remove_duplicates(nums):
        j = 0
        for i in list(range(1, len(nums))):
            if nums[j] != nums[i]:
                j = j + 1
                nums[j] = nums[i]
        return nums


s = Solution()
print(s.remove_duplicates([0, 0, 1, 1, 1, 2]))
