class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        firstLetter = word[0]
        rows = len(board)
        cols = len(board[0])
        startIndex = []
        directions = [[1,0], [-1,0], [0,1], [0, -1]]
        flag = False
        for i_ind in range(0, rows):
            for j_ind in range(0, cols):
                if board[i_ind][j_ind] == firstLetter:
                    startIndex.append([i_ind, j_ind])
                
        
        def findWord(iindex, jindex, currWord, visited):
            
            if currWord == word:
                nonlocal flag
                flag = True
                return 
            for idir, jdir in directions:
                new_i = iindex + idir
                new_j = jindex + jdir
                if (0 <= new_i < rows and 0 <= new_j < cols and board[new_i][new_j] == word[len(currWord)] and (new_i, new_j) not in visited):
                    visited.add((new_i, new_j))
                    findWord(new_i, new_j, currWord + board[new_i][new_j], visited)
                    visited.remove((new_i, new_j))
        
        # findWord(0, 0, "", set())
        # return flag
        if startIndex:
            for i_ind, j_ind in startIndex:
                visited = set()
                visited.add((i_ind, j_ind))
                findWord(i_ind, j_ind, firstLetter, visited)
                if flag:
                    return True
        return False