class BrowserHistory:

    def __init__(self, homepage: str):
        self.currHistory=[]
        self.forwardHistory=[]
        self.currHistory.append(homepage)


    
    def visit(self, url: str) -> void:
        #visit karo and forward delete
        self.currHistory.append(url)
        while self.forwardHistory:
            self.forwardHistory.pop()

    def back(self, steps: int) -> str:
        #homepase back nahi karna hai history hai to back karna 
        while (steps>0):
            if len(self.currHistory)>1:
                back=self.currHistory.pop()
                self.forwardHistory.append(back)
            else:
                #back nahi kar skte 
                break
            steps-=1
        return self.currHistory[-1]

    def forward(self, steps: int) -> str:
        #agr forward history me tab hai toh forward hoga nahi to nahi
        while steps>0:
            if len(self.forwardHistory)>0:
                forward=self.forwardHistory.pop()
                self.currHistory.append(forward)
            else:
                break
            steps-=1
        return self.currHistory[-1]      

#Your BrowserHistory object will be instantiated and called as such:
#obj = BrowserHistory(homepage)
#obj.visit(url)
#param_2 = obj.back(steps)
#param_3 = obj.forward(steps)