def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    while not at_goal():
        if front_is_clear():
            move()
        else:
            if wall_in_front():
                turn_left()
                while front_is_clear() and wall_on_right() and not at_goal():
                    move()
                if right_is_clear():
                    turn_right()
                    move()
                    turn_right()
                    while front_is_clear():
                        move()
jump()
