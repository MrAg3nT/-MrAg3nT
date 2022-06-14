# -MrAg3nT
#A sample coordination system for a game to move the character in any desired place using the keyboard.
#Created by Sailove Ghimire(c)

#Initializing variables
moves = 0 
row = 0
column = 0

#used while loop untill users want to quit
while True:
    direction = input("Which direction do you want to move? N, E, W, S?")     #initializing variable to store user input direction
    direction = direction.upper()     #convert direction into uppercase
    
    #if else conditions to confirm directions!
    if direction == "N": 
        moves += 1
        column +=1
      
    elif direction == "S":
        moves +=1
        column -= 1
       
    elif direction == "W":
        moves += 1
        row -= 1
            
    elif direction == "E":
        moves += 1
        row += 1
        
    elif direction == "Q":
        print("( ( %d  , %d ), %d )"%(column, row, moves))#d in %d signifies integer, F for float, and  s for string
        break     #to break the loop
