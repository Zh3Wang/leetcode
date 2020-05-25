from linklist import List


'''反转链表'''

# 递归
def reverse_list(head):
    # head: 头结点
    if not head or not head.next:
        return head
    new_head = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return new_head

# 迭代
def reverse_list2(head):
    pre = None
    cur = head
    while cur:
        if not cur.next:
            cur.next = pre
            break
        p = cur.next
        cur.next = pre
        pre = cur
        cur = p
    return cur


List.init_list([1, 2, 3, 4])
List.append(5)
print(List.get_all_items())
old_head = List.head
new_head = reverse_list2(old_head)

new_l = []
while new_head:
    new_l.append(new_head.data)
    new_head = new_head.next

print(new_l)