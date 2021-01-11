class myStackImp(object):
    def __init__(self):
        self.items = []
    def push(self, x):
        if self.items == []:
            self.items.append(x)
        elif x > self.items[-1]:
            self.items.append(x)
        else:
            self.items.insert(-2, x)
    def pop(self):
        if self.items == []:
            print("Error, empty stack")
        else:
            self.items.pop()
    def top(self):
        if self.items == []:
            print("Error, empty stack")
        else:
            return self.items[-1]
    def getMax(self):
        return self.items[-1]

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
