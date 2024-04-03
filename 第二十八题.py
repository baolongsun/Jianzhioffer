# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
class MinStack(object):
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self,x):
        self.stack1.append(x)
        if not self.stack2 or x <= self.stack2[-1]:
            self.stack2.append(x)

    def pop(self):
        if self.stack1:
            if self.stack1[-1] == self.stack2[-1]:
                self.stack2.pop()
            self.stack1.pop()

    def top(self):
        if self.stack1:
            return self.stack1[-1]

    def min(self):
        if self.stack2:
            return self.stack1[-1]

if __name__ == "__main__":
    myStack = MinStack()
    myStack.push(1)
    myStack.push(2)
    myStack.push(3)
    myStack.push(-2)
    print(myStack.min())