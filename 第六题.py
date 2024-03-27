# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
# 分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )


class CQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def appendTail(self,num:int):
        self.stack1.append(num)
    def deleteHead(self):
        if not self.stack1 and not self.stack2:
            return -1
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        if self.stack2:
            return self.stack2.pop()

if __name__ == "__main__":
    two_stack = CQueue()
    two_stack.appendTail(1)
    two_stack.appendTail(2)