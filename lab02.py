#name Ashwin Pulla
#Date: 9/10/2020
from pyKarel import *
from Athelete import Athlete
wld = World("maze")
bolt= Athlete(wld)

def moveX_drop (robot, x, direction):
   for i in range(x):
      robot.putBeeper()
      robot.move()
   if direction == "left":
      robot.turnLeft()
   elif direction=='right':
      robot.turnRight()
      
moveX_drop(bolt, 1, 'right')
moveX_drop(bolt, 1, 'right')
moveX_drop(bolt, 1, 'left')
moveX_drop(bolt, 1, 'left')
moveX_drop(bolt, 1, 'right')
moveX_drop(bolt, 1, 'left')
moveX_drop(bolt, 1, 'left')
moveX_drop(bolt, 1, 'right')
moveX_drop(bolt, 1, 'right')
moveX_drop(bolt, 2, 'right')
moveX_drop(bolt, 1, 'right')
moveX_drop(bolt, 0, 'right')
moveX_drop(bolt, 0, 'right')
moveX_drop(bolt, 1, '')
moveX_drop(bolt, 0, 'left')
moveX_drop(bolt, 2, '')
moveX_drop(bolt, 0, 'right')

moveX_drop(bolt, 3, '')
wld.mainloop()
