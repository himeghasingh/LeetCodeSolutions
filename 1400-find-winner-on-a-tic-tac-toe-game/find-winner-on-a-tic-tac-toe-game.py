class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0] * 3
        cols = [0] * 3
        diag = 0
        antidiag = 0
        player = -1
        for r, c in moves:
            player = -1 * player
            if r == c:
                diag += player
            if r + c == 2:
                antidiag += player
            rows[r] += player
            cols[c] += player
            if (abs(diag) == 3 or abs(antidiag) == 3 or abs(rows[r]) == 3 or abs(cols[c]) == 3):
                if player == 1:
                    return "A"
                else:
                    return "B"
        if len(moves) == 9:
            return "Draw"
        return "Pending"


         # Brute Force
        # matrix = [[0]*3 for i in range(3)]
        # def checkSequence():
        #     if (
        #         (matrix[0][0] == matrix[0][1] == matrix[0][2] != 0) or
        #         (matrix[1][0] == matrix[1][1] == matrix[1][2] != 0) or
        #         (matrix[2][0] == matrix[2][1] == matrix[2][2] != 0) or

        #         (matrix[0][0] == matrix[1][0] == matrix[2][0] != 0) or
        #         (matrix[0][1] == matrix[1][1] == matrix[2][1] != 0) or
        #         (matrix[0][2] == matrix[1][2] == matrix[2][2] != 0) or

        #         (matrix[0][0] == matrix[1][1] == matrix[2][2] != 0) or
        #         (matrix[2][0] == matrix[1][1] == matrix[0][2] != 0)
        #     ):
        #         return True
        #     else:
        #         return False
                
        # player = -1
        # for move in moves:
        #     player = -1 * player
        #     x, y = move
        #     matrix[x][y] = player
        #     if checkSequence():
        #         if player == 1:
        #             return "A"
        #         else:
        #             return "B"
        # if len(moves) == 9:
        #     return "Draw"
        # return "Pending" 

        
            
        