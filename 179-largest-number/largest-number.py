class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        numStrings = [str(num) for num in nums]
        numStrings.sort(key=lambda n:n*10, reverse=True)
        if numStrings[0] == "0":
            return "0"

        return "".join(numStrings)
        