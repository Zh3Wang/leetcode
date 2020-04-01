'''单链表的实现'''


class Node(object):
    def __init__(self, val, p=0):
        self.data = val
        self.next = p


class LinkList(object):
    def __init__(self):
        self.head = 0

    def init_list(self, data):
        self.head = Node(data[0])
        cur = self.head
        for i in data[1:]:
            node = Node(i)
            cur.next = node
            cur = cur.next

    def get_all_items(self):
        data = []
        cur = self.head
        while True:
            data.append(cur.data)
            if cur.next == 0:
                break
            cur = cur.next
        return data


l = LinkList()
l.init_list([1, 2, 2, 3, 4])
print(l.get_all_items())