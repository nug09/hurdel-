def turn_right():
    turn_left()
    turn_left()
    turn_left()

def walk():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def jump():
   move()
   walk()
    
while not at_goal():
    jump()