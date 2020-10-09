#Name:Ashwin Pulla
#Date: 10/6/2020
from Workers import *
from random import randint 
from pyKarel import *

def work_one_row(arg, m):
    for k in range(m-1):
        arg.doYourThing()
        arg.move()
      
def work_square(arg, n):
    arg.turnToTheNorth() 
    work_one_row(arg, n)
    for k in range(n, 1, -1):
        arg.turnRight() 
        work_one_row(arg, k) 
        arg.turnRight() 
        work_one_row(arg, k) 
    arg.doYourThing() 
    
def main():
    size = raw_input("Which 'field' (3, 5, 8)?")
    wld=World("field"+size, delay=0.1)
    if randint(0,1) == 2:
        work_square(Harvester(wld), int(size)) 
    else: 
        work_square(Planter(wld), int(size) )
    wld.mainloop()

if __name__=="__main__":
   main()
