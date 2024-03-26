# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
# 分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

class CQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack1.append(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        if self.stack2:#表示stack2有数据
            return self.stack2.pop()

        if self.stack1:#表示stack2无数据
            while self.stack1:
                self.stack2.append(self.stack1.pop())

            return self.stack2.pop()

        return -1

if __name__ == "__main__":
    two_stack = CQueue()
    two_stack.appendTail(1)
    two_stack.appendTail(2)

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()