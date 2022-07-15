"""
You are controlling a robot that is located somewhere in a room. The room is
modeled as an m x n binary grid where 0 represents a wall and 1 represents an
empty slot.

The robot starts at an unknown location in the room that is guaranteed to be
empty, and you do not have access to the grid, but you can move the robot using
the given API Robot.

You are tasked to use the robot to clean the entire room (i.e., clean every
empty cell in the room). The robot with the four given APIs can move forward,
turn left, or turn right. Each turn is 90 degrees.

When the robot tries to move into a wall cell, its bumper sensor detects the
obstacle, and it stays on the current cell.

Design an algorithm to clean the entire room using the following APIs:

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}

Note that the initial direction of the robot will be facing up. You can assume
all four edges of the grid are all surrounded by a wall.

"""

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
