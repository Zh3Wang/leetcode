# coding=utf-8
'''
@File    :   binary_tree.py
@Time    :   2020/09/24 15:00:04
@Author  :   Wangzz 
@Desc    :   二叉树实现
'''

class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self,data):
        # 如果根节点为空，设置当前值为根节点
        if not self.root:
            self.root = Node(data)
            return
        else:
            queue = [self.root]
            while True:
                cur = queue.pop(0)
                if not cur.left:
                    cur.left = Node(data)
                    return
                elif not cur.right:
                    cur.right = Node(data)
                    return
                else:
                    queue.append(cur.left)
                    queue.append(cur.right)

    # 前序遍历
    def prePrint(self,root):
        if not root:
            return
        print(root.data)
        self.prePrint(root.left)
        self.prePrint(root.right)
    
    # 中序遍历
    def midPrint(self,root):
        if not root:
            return
        self.midPrint(root.left)
        print(root.data)
        self.midPrint(root.right)

    # 后序遍历
    def postPrint(self,root):
        if not root:
            return
        self.postPrint(root.left)
        self.postPrint(root.right)
        print(root.data)
        

Bt = BinaryTree()
Bt.insert('A')
Bt.insert('B')
Bt.insert('C')
Bt.insert('D')
Bt.insert('E')
Bt.insert('F')
Bt.insert('G')
Bt.insert('H')
Bt.insert('I')
Bt.insert('J')
Bt.insert('K')
Bt.insert('L')
Bt.insert('M')
Bt.insert('N')
Bt.insert('O')
# Bt.prePrint(Bt.root)
# Bt.midPrint(Bt.root)
Bt.postPrint(Bt.root)
# print(Bt.root.left.left.data)