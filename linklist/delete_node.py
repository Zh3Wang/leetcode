from linklist import List


"""删除节点"""


class Solution:
    def __init__(self):
        pass

    """
        删除指定节点
        
    """
    def deleteNode(self, node):
        node.data = node.next.data
        node.next = node.next.next


List.init_list([1, 2, 3, 4, 5])
print(List.get_all_items())
sl = Solution()
sl.deleteNode(List.head.next.next)
print(List.get_all_items())

