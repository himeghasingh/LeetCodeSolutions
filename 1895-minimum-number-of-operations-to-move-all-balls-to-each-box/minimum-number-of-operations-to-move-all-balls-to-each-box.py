class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        leftCount = 0
        rightCount = 0
        leftCost = 0
        rightCost = 0

        for i in range(1, n):
            if boxes[i-1] == '1':
                leftCount += 1
            leftCost += leftCount
            answer[i] = leftCost
        
        for i in range(n-2, -1, -1):
            if boxes[i+1] == '1':
                rightCount += 1
            rightCost += rightCount
            answer[i] += rightCost

        return answer






        # O(N*2)
        # n = len(boxes)
        # answer = [0] * n
        # for i in range(0, n):
        #     for j in range(0, n):
        #         if boxes[j] == '1':
        #             answer[i] += abs(i-j)
        # return answer
        