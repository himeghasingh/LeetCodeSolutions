class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        j = 0
        answer = []
        xortotal = 0
        prefixSum = [0] * (n+1)


        for i in range(0, n):
            prefixSum[i+1] = prefixSum[i] ^ arr[i]
        print(prefixSum)


        for i in range(0, len(queries)):
            start, end = queries[i]
            print(start, ", ", end)
            xorval = xortotal ^ prefixSum[end+1] ^ prefixSum[start]
            answer.append(xorval)

        return answer
            

            
        