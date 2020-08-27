from linklist import List


'''反转链表'''


class Solution:
    def __init__(self):
        pass
    
    #迭代
    @staticmethod
    def reverse_curcle(head):
        cur, pre = head, None
        while cur:
            if not cur.next:
                cur.next = pre
                break
            p = cur.next
            cur.next = pre
            pre = cur
            cur = p
        return cur
    
    # 递归
    def reverse_digui(self,head):
        if not head or not head.next:
            return head
        new_head = self.reverse_digui(head.next)
        head.next.next = head
        head.next = None
        return new_head
List.init_list([1, 2, 3, 4, 5])
print(List.get_all_items())
sl = Solution()
# new_head = sl.reverse_curcle(List.head)
new_head = sl.reverse_digui(List.head)
new_l = []
while new_head:
    new_l.append(new_head.data)
    new_head = new_head.next

print(new_l)