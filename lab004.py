from pyKarel import *
from Athlete import Athlete
wld = World("arena")
bill=Robot(wld)

takeTheField(bill)


def takeTheField(arg):
   arg.turnRight()
   arg.move()
   arg.turnLeft()
   arg.move()
   arg.move()
   arg.move()
   arg.move()
   arg.turnRight()
   arg.move()
