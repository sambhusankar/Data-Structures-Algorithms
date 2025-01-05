class Solution(object):
    def robotSim(self, commands, obstacles):
        w = [-1, 1]
        n = [1, 1]
        e = [1, -1]
        s = [-1, -1]
        dir = w
        pos = [0, 0]

        WestObs = [i for i in obstacles if i[0] < 0 and i[1] > 0]
        EastObs = [i for i in obstacles if i[0] > 0 and i[1] < 0]
        SouthObs = [i for i in obstacles if i[0] < 0 and i[1] < 0]
        NorthObs = [i for i in obstacles if i[0] > 0 and i[1] > 0]
        print(WestObs, EastObs, SouthObs, NorthObs)

        # Here only changing the directions 
        for i in range(len(commands)):
            if (dir == w and commands[i] == -1) or (dir == e and commands[i]  == -2):
                dir = s
                continue
            if (dir == w and commands[i] == -2) or (dir == e and commands[i]  == -1):
                dir = n
                continue
            if (dir == s and commands[i] == -1) or (dir == n and commands[i]  == -2):
                dir = e
                continue
            if (dir == s and commands[i] == -2) or (dir == n and commands[i]  == -1):
                dir = w
                continue

            # This is for checking abstraction and movement
            if commands[i] > 0:
                # Checking for the West Direction 
                if dir == w:
                    for obs in WestObs:
                        if (obs[0]) < pos[0 - commands[i]] and (obs[1]) < pos[1]:
                            pos[0] -= obstacles[i][0]
                        else:
                            pos[0] -= commands[i]
                        
              
                    
        print(pos)

S = Solution()
S.robotSim([5, -1, 5, -1, 10, -2, 5], [[4, 4], [-3, 3], [-3, -5], [-1, -2], ])