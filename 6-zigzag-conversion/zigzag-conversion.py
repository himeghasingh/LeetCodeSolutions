class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        n = len(s)
        cols = ceil(n / (2 * numRows - 2)) * (numRows - 1)
        matrix = [['']*cols for i in range (numRows)]
        index = 0
        turn = 1
        i = 0
        j = 0

        while (index < n):
            if turn % 2 == 1:
                for i in range(0, numRows):
                    if index < n:
                        matrix[i][j] = s[index]
                        index += 1
                j += 1
            
            elif turn % 2 == 0:
                for i in range(numRows-2, 0, -1):
                    if index < n:
                        matrix[i][j] = s[index]
                        index += 1
                        j += 1
            turn += 1

        
        res = ""
        for i in range(0, numRows):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] != '':
                    res += matrix[i][j]

        return res

                
                        


        