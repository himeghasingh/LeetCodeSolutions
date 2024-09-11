class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        n = len(customers)
        sadCust = 0
        totalCust = 0
        prefixSum = [0] * (n+1)
        minSad = float("inf")

        for i in range(0, n):
            if grumpy[i] == 1:
                sadCust += customers[i]
                prefixSum[i+1] = prefixSum[i] + customers[i]
            else:
                prefixSum[i+1] = prefixSum[i]
            totalCust += customers[i]

        # print(prefixSum) 

        for i in range(0, n - minutes + 1):
            happyInRange = prefixSum[i+minutes] - prefixSum[i]
            sad = sadCust - happyInRange
            minSad = min(minSad, sad)

        # print(minSad)
        return totalCust - minSad





        