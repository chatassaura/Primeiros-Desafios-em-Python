# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# Código Anterios Já resolveu o exercicío

def turn_right():
    turn_left()
    turn_left() 
    turn_left()     
       
while not at_goal():
    if right_is_clear() and not wall_in_front():
        move()
    elif front_is_clear() and not right_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif wall_in_front():
        turn_left()
