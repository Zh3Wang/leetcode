from linklist import List


'''返回倒数第K个节点'''


class Solution:
    def __init__(self):
        pass

    # 迭代
    @staticmethod
    def kth_to_last_wz( head, k):
        if k <= 0:
            return False
        cur = head
        l = []
        while cur:
            l.append(cur.data)
            cur = cur.next
        let = len(l) - k
        return l[let:let + 1][0]

    # 递归解法
    i = 1

    def ktu_to_last_digui(self, head, k):
        if k <= 0:
            return False
        if not head or not head.next:
            return head.data
        p = self.ktu_to_last_digui(head.next, k)
        if self.i >= k:
            self.i += 1
            return p
        else:
            self.i += 1
            return head.data

    # 双指针解法
    @staticmethod
    def kth_to_last_point(head, k):
        """
            设置两个指针，分别为快慢指针 left_point,right_point
            快指针从头节点开始遍历到结束，每次遍历后K-1，当K=0时，慢指针启动，当快指针遍历完成后，慢指针刚好指在倒数第K个节点上，返回当前值即可
        """
        left_point, right_point = head, head
        while right_point:
            right_point = right_point.next
            if k > 0:
                k -= 1
            else:
                left_point = left_point.next
        return left_point.data


List.init_list([1, 2, 3, 4])
List.append(5)
print(List.get_all_items())
sl = Solution()
print(sl.kth_to_last_point(List.head, 4))


