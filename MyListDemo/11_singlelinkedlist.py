# -*- coding: utf-8 -*-


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    # 添加到头部
    def add(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    # 增加到尾部
    def append(self, val):
        new_code = Node(val)
        if self.head is None:
            self.head = new_code
            return True

        node = self.head
        while node.next:
            node = node.next

        node.next = new_code
        return True

    def insert(self, index, val):
        if index is '' or index is None:
            index = 0

        if val is '' or val is None:
            print('error: 插入的节点数据不能为空')
            return False

        if index == 0:
            # 插入到头部
            self.add(val)
        elif index > self.len():
            # 插入到尾部
            self.append(val)
        else:
            # 插入到中部
            lg = 0
            node = self.head
            while node is not None:
                lg += 1
                if lg == index:
                    # 添加到此位置
                    new_node = Node(val)
                    new_node.next = node.next
                    # 更新前一节点的next
                    node.next = new_node
                    break
                else:
                    node = node.next

        return True

    def update(self, index, val):
        lg = 0
        node = self.head
        while node is not None:
            if lg == index:
                # 更新此位置的节点
                node.data = val
                break
            else:
                node = node.next

            lg += 1

        return True

    def remove(self, index):
        if isinstance(index, list) or isinstance(index, tuple):
            # print('aaa')
            for i in index:
                self.delete(i)
        else:
            # print('bbb')
            self.delete(index)

    def delete(self, index):
        lg = 0
        node = self.head
        if index == 0:
            self.head = node.next
        else:
            # 要找到该节点的前一个节点
            while node is not None:
                if lg == index - 1:
                    # 移除此位置的节点
                    node.next = node.next.next
                    break
                else:
                    node = node.next

                lg += 1

        return True

    def clear(self):
        self.head = None

    def len(self):
        lg = 0
        node = self.head
        while node is not None:
            lg += 1
            node = node.next

        return lg

    def search(self, val):
        index = 0
        # previous = None
        # next = None
        target_node = None
        node = self.head
        while node is not None:
            if node.data == val:
                target_node = node
                break
            else:
                node = node.next

            index += 1

        return {
            'index': index,
            'node': target_node
        }

    def get_linklist(self):
        res = []
        s = ''
        node = self.head
        while node is not None:
            # print(node.data)
            s += node.data + '-->'
            res.append(node.data)
            node = node.next

        print(s[:-3])
        return res


n1 = Node('n1')
n2 = Node('n2')
n3 = Node('n3')

link = SingleLinkedList()
link.head = Node('n0')
link.head.next = n1

n1.next = n3
n3.next = n2

link.insert(0, 'n4')
link.insert(0, 'n5')
link.append('n6')
link.insert(1, 'n7')
link.insert(2, 'n8')
link.insert(3, 'n9')
link.insert(5, 'n10')

# link.remove(0)
# link.remove(2)
# link.remove(4)

# link.update(1, 's1')


# print(id(link.head), id(link))
# link.clear()

r = link.get_linklist()
print(r)

a = link.search('n10')
print(a['index'], a['node'].data, a['node'].next.data)

leng = link.len()
print(leng)


