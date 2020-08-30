class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minStack=[]
        self.t=-1

    def push(self, x: int) -> None:
        self.minStack.append(x)
        self.t+=1

    def pop(self) -> None:
        if len(self.minStack)==0:
            return
        self.minStack.pop()
        self.t-=1

    def top(self) -> int:
        if len(self.minStack)==0:
            return
        return self.minStack[self.t]

    def getMin(self) -> int:
        if len(self.minStack)==0:
            return
        return min(self.minStack)

x=MinStack()
x.push(2)
x.push(3)
print(x.top())
        