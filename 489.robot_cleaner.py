class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        
        # move in direction, starting from an orientation o
        # return whether move was successful
        # robot is now in orientation 'direction'
        def maybe_move(ori, target_direction):
            while ori < target_direction:
                robot.turnRight()
                ori += 1
                
            while ori > target_direction:
                robot.turnLeft()
                ori -= 1
                
            return robot.move(), ori
        
        blocked = set()
        
        # robot has just successfully entered the x,y space, and is
        # in orientation ori.  when this function returns, the robot
        # will again be in x,y
        def backtrack(x, y, ori):
            robot.clean()
            blocked.add((x,y))
            
            positions = [(x + xd, y + yd) for xd, yd in [(0, -1), (1, 0), (0, 1), (-1, 0)]]
            for target_dir, pos in enumerate(positions):
                if pos in blocked:
                    continue
                moved, ori = maybe_move(ori, target_dir)
                if moved:
                    ori = backtrack(*pos, ori)
                    rev_dir = (target_dir + 2) % 4
                    _, ori = maybe_move(ori, rev_dir)
                else:
                    blocked.add(pos)
                    
                
            return ori

        backtrack(0, 0, 0)
        
"""
This took about 2 hours.  Many mistakes were made, in the maybe_move function,
and the choice of when to set blocked, and also the basic API of the backtrack
function.

new_ori = backtrack(x, y, ori)

Before the call, the robot is in orientation ori, and has just entered the x,y square.
blocked holds a set of all squares that are either already cleaned or have obstacles.

After the call, the robot is again in the x,y square, and in orientation new_ori.  It has
cleaned all nonblocked squares that were reachable from x,y, and added them to blocked.

"""
