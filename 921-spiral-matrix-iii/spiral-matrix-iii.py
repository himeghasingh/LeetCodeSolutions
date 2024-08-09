class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        total = rows * cols
        count = 1
        add = 1
        turn = 1
        result = [[rStart, cStart]]
        while (count < total):            
            if turn % 4 == 1:
                for j in range(cStart+1, cStart+add+1):
                    if 0 <= rStart < rows and 0 <= j < cols:
                        result.append([rStart,j])
                        count += 1
                cStart = cStart + add

            if turn % 4 == 2:
                for i in range(rStart+1, rStart+add+1):
                    if 0 <= i < rows and 0 <= cStart < cols:
                        result.append([i, cStart])
                        count += 1
                rStart = rStart + add

            if turn % 4 == 3:
                for j in range(cStart-1, cStart-1-add, -1):
                    if 0 <= rStart < rows and 0 <= j < cols:
                        result.append([rStart, j])
                        count += 1
                cStart = cStart - add

            if turn % 4 == 0:
                for i in range(rStart-1, rStart-add-1, -1):

                    if 0 <= i < rows and 0 <= cStart < cols:
                        result.append([i, cStart])
                        count += 1
                rStart = rStart - add
            
            if turn % 2 == 0:
                add += 1
            turn += 1
            
        return result


                    


        