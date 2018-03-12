# -*- coding: UTF-8 -*-
class BinaryHeap(object):
    def __init__(self):
        self.headList = [0]
        self.currentSize = 0  # 堆的大小

    def bublleUp(self, i):
        while i // 2 > 0:
            if self.headList[i] < self.headList[i // 2]:  # 当子节点的关键字小于父节点的关键字时两者交换
                self.headList[i], self.headList[i // 2] = self.headList[i // 2], self.headList[i]
                i = i // 2  # 子节点和父节点交换后，原子节点的序号变为父节点序号
        return self.headList

    def insert(self, n):
        self.headList.append(n)  # 在二叉树结尾插入值
        self.currentSize = self.currentSize + 1  # 二叉堆的大小加一,也是插入值的序号
        self.bublleUp(self.currentSize)  # 向上冒泡将插入的值放入适当的未知

    def minChild(self, i):  # 用于根节点“下沉”时，比较两个子节点，选择子节点中关键字较小的一个和父节点交换
        if (i * 2 + 1) > self.currentSize:  # 如果最后一个父节点只有一个子节点，则自然而然的返回这个唯一节点的序号
            return i * 2
        else:
            if self.headList[i * 2] <= self.headList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def nodeDown(self, i):
        while (i * 2) <= self.currentSize:
            sonNum = self.minChild(i)
            if self.headList[i] > self.headList[sonNum]:
                self.headList[i], self.headList[sonNum] = self.headList[sonNum], self.headList[i]
            i = sonNum

    def delMin(self):
        minNum = self.headList[1]  # 二叉堆的最小值为根节点，删除最小值从根节点开始删除
        self.headList[1] = self.headList[self.currentSize]  # 将最后一个叶节点补上删除的跟节点的位置，保持二叉堆的结构
        self.headList.pop()  # 最后的叶节点补上了根节点的位置，所以从最后一个位置删除
        self.currentSize = self.currentSize - 1
        self.nodeDown(1)  # 新的跟节点下沉
        return minNum

    def buildHeap(self, list):  # 用未排序的list生成二叉堆
        i = len(list) // 2
        self.currentSize = len(list)
        self.headList = [0] + list[:]
        while i > 0:
            self.nodeDown(i)
            i = i - 1

list = [9, 5, 9, 6, 2, 3, 5]
bh = BinaryHeap()
bh.buildHeap(list)
B = []
for i in range(len(list)):
    B.append(bh.delMin())
print B