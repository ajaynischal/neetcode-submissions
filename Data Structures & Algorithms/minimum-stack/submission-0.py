class MinStack:

    def __init__(self):
        self.stack = [] #arraylist technically
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val = min(val, self.minStack[-1]) #min of itself and the top of the min stack
        else:
            val = min(val, val)
        self.minStack.append(val)
        

        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        #this is hard because stack doesnt support this therefore use second stack
        return self.minStack[-1]

        
