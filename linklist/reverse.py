# 链表反转

from linklist import List


# 递归
def reverse_list(head):
    # head: 头结点
    if not head or not head.next:
        return head
    p = reverse_list(head.next)
    p.next = head
    head.next = None
    return head


# 迭代
def reverse_list2():
    pass


List.init_list([1, 2, 3, 4])
List.append(5)
print(List.get_all_items())
old_head = List.head
new_head = reverse_list(old_head)

new_l = []
while new_head:
    new_l.append(new_head.data)
    new_head = new_head.next

print(new_l)