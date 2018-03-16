#  冒泡排序
# from timeit import Timer
#
# # print('a')
# #  代码运行5次总共的时间
# timer = Timer("print('a')")
# print(timer.timeit(number=5))

#  链表：
class Node(object):

    def __init__(self,item):
        """初始化"""
        self.item = item
        self.next = None

class SingleLinkList(object):
    """dan lian biao"""

    def __init__(self):
        self.__head = None

    def is_empty(self):
        """连表是否为空"""
        # 判断首节点是否为空
        return self.__head is None


    def length(self):
        """长度"""
        pass

    def travel(self):
        """便利整个列表"""
        pass

    def add(self,item):
        """把传递进来的的item 创建一个节点"""
        node = Node(item)
        # 让新的节点的next 指向老的头
        node.next = self.__head
        #让头指向新的节点
        self.__head = node


    def append(self,item):
        pass

    def insert(self,pos,item):
        pass

    def remove(self,item):
        pass

    def search(self,item):
        """查找节点是否存在"""
        pass

if __name__ == '__main__':
    sll = SingleLinkList()
    print(sll.is_empty())
    sll.add(5)
    sll.add(2)
    print(sll.is_empty())