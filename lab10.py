#Name:Ashwin pulla
#Date:9/24/2020
from pyKarel import *
from Athlete import Athlete
global r
global l
global f
global b
global temp
global count
global k

def movement():
   temp=Athlete(wld,1,1,north,0)
   while not temp.nextToABeeper():
      if temp.rightIsClear():
         temp.turnRight()
         temp.move()
        # temp.turnLeft()
      elif temp.frontIsClear():
         temp.move()
      elif temp.leftIsClear():
         temp.turnLeft()
         temp.move()
        # temp.turnRight()
      elif temp.backIsClear():
         temp.turnAround()
         temp.move()
        # temp.turnAround()
      
         
         

def main():       
   name_of_world=raw_input("Which 'tasks' world? ")
   global wld
   wld=World(name_of_world, delay=0.1)
  
   
   movement()
      
if __name__=="__main__":
   main()



wld.mainloop()

  