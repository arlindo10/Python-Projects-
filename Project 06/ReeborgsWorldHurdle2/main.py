# Reeborg's World: Hurdle 2

# You need to Copy-paste this to https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def running_jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    # no need for this turn once the finish is reached
    if not at_goal():
        turn_left()


while not at_goal():
    running_jump()