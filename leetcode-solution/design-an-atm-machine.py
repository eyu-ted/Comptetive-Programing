class ATM:

    def __init__(self):
        self.banknotes=[20,50,100,200,500]
        self.bank=[0]*5


    def deposit(self, banknotesCount: List[int]) -> None:
        for i,n in enumerate(banknotesCount):
            self.bank[i]+=n
        


    def withdraw(self, amount: int) -> List[int]:
        lis=[0]*5
        for i in range(4,-1,-1):
            lis[i] =min(self.bank[i],amount//self.banknotes[i])
            amount-=lis[i]*self.banknotes[i]
        if amount:
            return [-1]
        for i in range(5):
            self.bank[i]-=lis[i]
        return lis
        

        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)