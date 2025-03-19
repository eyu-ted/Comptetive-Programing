class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        dic = defaultdict(list)
        
        invalid = set()

        for i, transaction in enumerate(transactions):

            name,time,amount,city = transaction.split(",") 

            time = int(time)
            amount = int(amount)

            dic[name].append((time,city,i))

            if amount > 1000:
                invalid.add(i)

            for t,c,indx in dic[name]:
                if abs(time -t) <= 60 and c != city:
                    invalid.add(indx)
                    invalid.add(i)
        
        return [transactions[i] for i in invalid]