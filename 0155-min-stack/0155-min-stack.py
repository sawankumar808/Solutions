class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]

        

    def push(self, value: int) -> None:
        self.stack.append(value)
        #if min stack are empty and new are small than the old than add
        if not self.minstack or value<=self.minstack[-1]:
            self.minstack.append(value)
        else:# else add old as a tiz
            self.minstack.append(self.minstack[-1])
        

    def pop(self) -> None:
        self.stack.pop()#pop both 
        self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        
        

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()