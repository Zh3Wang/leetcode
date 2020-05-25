# 单链表的实现


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

    def is_empty(self):
        if self.get_length() == 0:
            return True
        else:
            return False

    def get_length(self):
        len = 0
        cur = self.head
        while cur != 0:
            len = len + 1
            cur = cur.next
        return len

    def clear(self):
        self.head = 0

    # 尾部添加节点
    def append(self, value):
        data = Node(value)
        if self.head == 0:
            # 头部为0.说明无节点
            self.head = data
        else:
            # 头部节点设为当前节点
            cur = self.head
            while cur.next != 0:
                cur = cur.next
            # 如果下一个节点为0，说明当前节点是最后一个节点，直接将指针指向新节点
            cur.next = data

    # 插入节点
    def insert(self, index, value):
        node = Node(value)
        #如果插入位置为0
        if index == 0:
            node.next = self.head
            self.head = node
        cur = self.head
        j = 1
        while cur.next != 0 and j < index:
            cur = cur.next
            j += 1
        if j == index:
            n = cur.next
            cur.next = node
            node.next = n

    def get_all_items(self):
        data = []
        cur = self.head
        while cur != 0:
            data.append(cur.data)
            cur = cur.next
        return data


List = LinkList()

