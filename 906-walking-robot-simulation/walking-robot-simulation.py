class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        i = 0
        j = 0
        moves = ["North", "East", "South", "West"]
        move = "North"
        result = 0
        obstacles_set = set(map(tuple, obstacles))


        for cmd in commands:
            if cmd == -1:
                moveIndex = moves.index(move)
                if moveIndex == 3:
                    move = "North"
                else:
                    move = moves[moveIndex+1]   
            elif cmd == -2:
                moveIndex = moves.index(move)
                if moveIndex == 0:
                    move = "West"
                else:
                    move = moves[moveIndex-1] 
            else:
                steps = 0

                while steps < cmd:
                    if move == "North":
                        j += 1
                    elif move == "East":
                        i += 1
                    elif move == "South":
                        j -= 1
                    elif move == "West":
                        i -= 1
                    steps += 1
                    

                    if (i,j) in obstacles_set:
                        if move == "North":
                            j -= 1
                        elif move == "East":
                            i -= 1
                        elif move == "South":
                            j += 1
                        elif move == "West":
                            i += 1
                        break
            result = max(result,(i*i) + (j*j))

        return result


                

            


                
