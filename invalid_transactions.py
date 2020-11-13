from typing import List
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        events = []
        for t in transactions:
            name, time, cost, city = t.split(",")
            events.append([name, int(time), int(cost), city, t])

        questionable = set()

        for event in events:
            if event[2] > 1000:
                questionable.add(event[4])
            for value in events:
                if event[0] == value[0] and abs(event[1] - value[1]) <= 60 and event[3] != value[3]:
                    questionable.add(event[4])
        return list(questionable)

s = Solution()
s.invalidTransactions(["alice,20,800,mtv","alice,50,100,beijing"])
