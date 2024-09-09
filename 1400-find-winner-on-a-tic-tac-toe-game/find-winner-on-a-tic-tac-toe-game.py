class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        matrix = [[0]*3 for i in range(3)]
        def checkSequence():
            if (
        # Check rows
                (matrix[0][0] == matrix[0][1] == matrix[0][2] != 0) or
                (matrix[1][0] == matrix[1][1] == matrix[1][2] != 0) or
                (matrix[2][0] == matrix[2][1] == matrix[2][2] != 0) or

                # Check columns
                (matrix[0][0] == matrix[1][0] == matrix[2][0] != 0) or
                (matrix[0][1] == matrix[1][1] == matrix[2][1] != 0) or
                (matrix[0][2] == matrix[1][2] == matrix[2][2] != 0) or

                # Check diagonals
                (matrix[0][0] == matrix[1][1] == matrix[2][2] != 0) or
                (matrix[2][0] == matrix[1][1] == matrix[0][2] != 0)
            ):
                return True
            else:
                return False
        player = -1
        for move in moves:
            print("move ", move, "matrix ",matrix)

            player = -1 * player
            x, y = move
            matrix[x][y] = player
            if checkSequence():
                if player == 1:
                    return "A"
                else:
                    return "B"
        if len(moves) == 9:
            return "Draw"
        return "Pending" 

        
            
        