class myStackImp(object):
    def __init__(self):
        self.max = []
        self.items = []
    def push(self, x):
        self.items.append(x)
        if self.max == []:
            self.max.append(x)
        else:
            if self.max[-1] < x:
                self.max.append(x)
    def pop(self):
        if self.items == []:
            print("Error, empty stack")
        else:
            self.items.pop()
            self.max.pop()
    def top(self):
        if self.items == []:
            print("Error, empty stack")
        else:
            return self.items[-1]
    def getMax(self):
        return self.max[-1]

x = myStackImp()
x.push(-3)
x.push(0)
x.push(9)
print(x.getMax())
# 9
x.pop()
print(x.top())
# 0
print(x.getMax())
