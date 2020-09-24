#name Ashwin Pulla
#Date 09/17/2020
from pyKarel import *
from Athelete import Athlete
from Climber import Climber
wld=World('mountain',width=16, height=8)
bob=Climber(wld,x=8)
bill=Climber(wld,x=8)

#bob climbing up to the mountain

bob.turnRight()
bob.move()
bob.turnLeft()
bob.move()
bob.climbUpRight()
bob.turnLeft()
bob.move()
bob.climbUpRight()
bob.turnLeft()
bob.move()
bob.climbUpRight()

#bill climbing up to the mountain

bill.turnRight()
bill.move()
bill.turnLeft()
bill.move()
bill.climbUpRight()
bill.turnLeft()
bill.move()
bill.climbUpRight()
bill.turnLeft()
bill.move()
bill.climbUpRight()

#bob climbing down the mountain
bob.move()
bob.turnRight()
bob.climbDown()
bob.climbDown()
bob.turnLeft()
bob.move()
bob.turnRight()
bob.move()
bob.move()
bob.pickBeeper()

#bob climbing back up the mountain
bob.turnAround()
bob.move()
bob.move()
bob.turnLeft()
bob.move()
bob.turnRight()
bob.move()
bob.move()
bob.turnLeft()
bob.move()
bob.turnRight()

#bill climbing down the mountain
bill.turnAround()
bill.move()
bill.turnLeft()
bill.climbDown()
bill.climbDown()
bill.turnRight()
bill.move()
bill.turnLeft()
bill.climbDown() 
bill.climbDown()
bill.turnRight()
bill.climbDown()
bill.turnLeft()
bill.climbDown()
bill.climbDown()
bill.turnRight()

#bob climbing down the mountain
bob.turnLeft()
bob.move()
bob.turnLeft()
bob.climbDown()
bob.climbDown()
bob.turnRight()
bob.move()
bob.turnLeft()
bob.climbDown() 
bob.climbDown()
bob.turnRight()
bob.climbDown()
bob.turnLeft()
bob.climbDown()
bob.climbDown()
bob.turnRight()
bob.move()

#bob placing beeper
bob.putBeeper()
bob.turnAround()
bob.move()
bob.turnAround()





