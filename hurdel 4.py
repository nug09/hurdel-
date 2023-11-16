def turn_right():
    turn_left()
    turn_left()
    turn_left()


def lompat():
    while not wall_in_front():
        move()
        if at_goal():
            done()
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()
 
while not at_goal():
    lompat()
    
    