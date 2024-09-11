class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        for i in range(0, n):
            for j in range(0, n):
                if boxes[j] == '1':
                    answer[i] += abs(i-j)
        print(answer)
        return answer
        