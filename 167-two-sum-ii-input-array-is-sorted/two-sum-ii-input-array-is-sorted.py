class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = set()
        n = len(numbers)
        for i in range(0, n):
            first = i
            if (target-numbers[i]) in numbers[i+1:]:
                second = numbers[i+1:].index(target-numbers[i])
                return [first+1, first+1+second+1]
