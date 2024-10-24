#snake and ladder 
import random
board = 100
snakes = {17: 7, 54: 34, 62: 19, 98: 79}
ladders = {3: 38, 24: 33, 42: 93, 72: 84}
position = 0
while position<100:
    dice = random.randint(1, 6)
    position += dice

    if position in snakes:
        position = snakes[position]
    elif position in ladders:
        position = ladders[position]
    if position >= board:
        print("Congratulations, you won!")
        break
    
    
    print("You are now at position", position)

    