# -*- coding: utf-8 -*-


import time


class Node(object):
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None


# 广度优先遍历（层次遍历）
class Tree(object):
    """
    二叉树
    """
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return

        queue = [self.root]
        while queue:
            curr_node = queue.pop(0)
            if curr_node.lchild is None:
                curr_node.lchild = node
                return
            else:
                queue.append(curr_node.lchild)

            if curr_node.rchild is None:
                curr_node.rchild = node
                return
            else:
                queue.append(curr_node.rchild)

    def remove(self, node):
        pass

    def size(self):
        pass

    # 树的遍历
    # 广度遍历
    def show_breadth_travel(self):
        queue = [self.root]
        while queue:
            # lrchild = ''
            curr_node = queue.pop(0)
            if curr_node.lchild:
                queue.append(curr_node.lchild)
                # lrchild += curr_node.lchild.elem

            if curr_node.rchild:
                queue.append(curr_node.rchild)
                # lrchild += curr_node.rchild.elem

            print(curr_node.elem, end=' ')

    # 深度遍历（前序遍历，中序遍历，后序遍历）
    # 前序遍历（根，左，右）
    def show_deepth_preorder(self, node):
        if node is None:
            return

        print(node.elem, end=' ')
        self.show_deepth_preorder(node.lchild)
        self.show_deepth_preorder(node.rchild)

    # 中序遍历（左，根，右）
    def show_deepth_inorder(self, node):
        if node is None:
            return

        self.show_deepth_inorder(node.lchild)
        print(node.elem, end=' ')
        self.show_deepth_inorder(node.rchild)

    # 后序遍历（左，右，根）
    def show_deepth_postorder(self, node):
        if node is None:
            return

        self.show_deepth_postorder(node.lchild)
        self.show_deepth_postorder(node.rchild)
        print(node.elem, end=' ')


tree = Tree()
tree.add(0)
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)
tree.add(6)
tree.add(7)
tree.add(8)
tree.add(9)
tree.show_breadth_travel()
print('\r')
tree.show_deepth_preorder(tree.root)
print('\r')
tree.show_deepth_inorder(tree.root)
print('\r')
tree.show_deepth_postorder(tree.root)

