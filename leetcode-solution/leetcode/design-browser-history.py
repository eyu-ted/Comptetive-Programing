class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [ homepage ]
        self.p = 0

    def visit(self, url: str) -> None:
        self.stack = self.stack[:self.p + 1]
        self.stack.append( url )
        self.p = len( self.stack ) - 1

    def back(self, steps: int) -> str:
        self.p=max(self.p - steps , 0)
        return self.stack[ self.p ]

    def forward(self, steps: int) -> str:
        self.p=min(self.p + steps , len( self.stack ) - 1)
        return self.stack[ self.p ]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)