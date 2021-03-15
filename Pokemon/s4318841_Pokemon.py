#!/usr/bin/env python3
###################################################################
#
#   CSSE1001/7030 - Assignment 1
#
#   Student Username: s4318841
#
#  
#
###################################################################

###################################################################
#
# The following is support code. DO NOT CHANGE.

from a1_support import *

# End of support code
################################################################

# Write your code here

## Direction deltas directions and direction deltas in lists.

DIRECTION_DELTASX = ['n','s', 'e', 'w']

DIRECTION_DELTASY= [(-1, 0),(1, 0),(0, 1),(0, -1)]
  

def get_position_in_direction(position, direction):
    """
    takes a position(row,column) and a direction(n,s,e,w) and returns the
    position of the adjacent square. Does not matter if direction is legal. 
    
    get_position_in_direction(tuple, str) -> (tuple)
    """

    dx, dy = DIRECTION_DELTAS[direction]
    x, y = position

    return (x + dx, y + dy)

    #get_position_in_direction was created with assistance by Ben Martin


def print_maze(maze, position):
    """
    takes a maze string and the position of the player, and prints the
    maze with the player shown as an 'A'
    
    print_maze(str, (int, int)) -> None 
    """
    columns= maze_columns(maze)
        
    index=(position_to_index(position, columns))
           
    G=(maze[0:index])+"A"+(maze[index+1:])
    print(G)


def move(maze, position, direction):
    """
    takes a maze string, position of a square and a direction and returns the
    resulting position and square after the move in the form of
    (position, square).
    If the move is an invalid one, the position returned is the
    same as the previous position.
    
    move(str, tuple, str) -> tuple<tuple, str>
    
    """
    special=[]
    special.append(position)
        
    position=get_position_in_direction(position, direction)
    columns= maze_columns(maze)

    index=(position_to_index(position, columns))
    
    if maze[index]==WALL:
        return(special[0], WALL)
                
    for i in POKEMON:
        if maze[index]==i:
                return(position,i)
          
    if maze[index]==OPEN:
        return(position, OPEN)

    elif maze[index]==PLAYER:
        return(position, PLAYER)

    else:
        return(index) 

def get_legal_directions(maze, position):
    """
    Takes the maze string and position and returns all possible legal directions
    (n,s,e,w)

    get_legal_directions(str, tuple) -> list<str>
    """
    D=[]
       
    for i in DIRECTION_DELTASX:
        z=move(maze,position,i)
        
        if z[1]!=WALL:
            D.append(i)
            
    return D 


def interact():
    """interact() is the top-level function that defines the text-based user
    interface. It takes no arguments and returns None)
    
    interact()-> None

    """

    #prompts the user for maze file
    
    A=input('Maze File: ')

    maze = load_maze(A)
    
    position=START_POSITION
    route=[]
    route.append(position)

    print()
    print_maze(maze, position)
    print()
            
    ##prompts user for command and processes commands
    ##repeatedly prompts user for command processes it until the game ends or the user quits
    ##Moves list is created which appends each position the position has taken. If the user
    ##backs up one move the last position is popped from the list.
        
    while True:
        B=input("Command: " )
        B=B.strip()
             
        if B==('q'):
            D=input("Are you sure you want to quit? [y] or n: ")
            if D==('y'):
                break
            if D==('n'):
                print()
                (print_maze(maze, position))
                print()
                
            else:
                break
                        
        elif B in DIRECTION_DELTASX:
            (position,G)=(move(maze, position, B))
            route.append(position)
            if G== WALL:
                print("You can't go in that direction.")
            if G in POKEMON:
                if G!= 'P':
                    print("Oh no! A wild "+ POKEMON[G]+ " appeared - you lose :(")
                    break

                else:
                    print("Congratulations - you found Pikachu!")
                    break
            print()
            (print_maze(maze, position))
            print()
            
        elif B==('b'):
            if len(route)>1:
                route.pop()
                position=(route[-1])
            else:
                print("You cannot go back from the beginning.")
            print()
            (print_maze(maze, position))
            print()
              

        elif B==('r'):
            route=[]
            position=START_POSITION
            print()
            (print_maze(maze, position))
            print()
        
        elif B==('p'):
             T=(get_legal_directions(maze, position))
             Y=', '.join(T)
             print("Possible directions: "+Y)
             print()
             (print_maze(maze, position))
             print()
        
        elif B==('?'):
            print(HELP_TEXT)
            print()
            (print_maze(maze, position))
            print()

        else:
            print("Invalid command: "+B)
            print()
            (print_maze(maze, position))
            print()                   
             
    pass







##################################################
# !!!!!! Do not change (or add to) the code below !!!!!
# 
# This code will run the interact function if
# you use Run -> Run Module  (F5)
# Because of this we have supplied a "stub" definition
# for interact above so that you won't get an undefined
# error when you are writing and testing your other functions.
# When you are ready please change the definition of interact above.
###################################################

if __name__ == '__main__':
    interact()





"""
----------------------------------------------
MARKING:   

Total: 10

Meeting comments:
   Very good understanding of written code and support file usage

General comments:
   Functions
       get_position_in_direction
       print_maze
       move
       get_legal_directions
       interact
           resetting resets to different initalisation, causing back to fail one step early
           Well done on a perfect submission
   Commenting/Style
       (int, int) instead of tuple
   general

----------------------------------------------
TEST RUN:
Version: 2016s2_1.1.0
/------------------------------------------------------------------------------\
|                              Summary of Results                              |
\------------------------------------------------------------------------------/
--------------------------------------------------------------------------------
get_position_in_direction
--------------------------------------------------------------------------------
    +  1. ((2, 3), e) (from spec)
    +  2. ((2, 3), s) (from spec)
    +  3. ((5, 5), n) 
    +  4. ((45, 28), n) 
    +  5. ((45, 28), s) 
    +  6. ((45, 28), e) 
    +  7. ((45, 28), w) 
--------------------------------------------------------------------------------
print_maze
--------------------------------------------------------------------------------
    +  1. (maze1.txt, [(1, 1)])
    +  2. (M4Z3five, [(1, 1)])
    +  3. (M4Z3five, [(2, 14)])
    +  4. (M4Z3five, [(10, 18)])
    +  5. (M4Z3five, [(6, 17)])
    +  6. (M4Z3five, [(7, 18)])
--------------------------------------------------------------------------------
move
--------------------------------------------------------------------------------
    +  1.  (maze1.txt, [(1, 1), 's'])
    +  2.  (maze1.txt, [(1, 1), 'n'])
    +  3.  (maze1.txt, [(3, 2), 'e'])
    +  4.  (maze1.txt, [(1, 2), 'e'])
    +  5.  (M4Z3five, [(4, 13), 'n'])
    +  6.  (M4Z3five, [(4, 13), 's'])
    +  7.  (M4Z3five, [(6, 2), 'w'])
    +  8.  (M4Z3five, [(6, 2), 'e'])
    +  9.  (M4Z3five, [(6, 2), 'n'])
    +  10. (M4Z3five, [(6, 2), 's'])
    +  11. (M4Z3five, [(7, 17), 'e'])
    +  12. (M4Z3five, [(6, 18), 's'])
--------------------------------------------------------------------------------
get_legal_directions
--------------------------------------------------------------------------------
    +  1. (maze1.txt, [(1, 1)])
    +  2. (maze1.txt, [(1, 3)])
    +  3. (maze1.txt, [(3, 1)])
    +  4. (M4Z3five, [(3, 7)])
    +  5. (M4Z3five, [(6, 17)])
    +  6. (M4Z3five, [(2, 16)])
--------------------------------------------------------------------------------
interact
--------------------------------------------------------------------------------
    +  1.  Example 1 (from spec) + whitespace/case
    +  2.  Example 2 (from spec)
    +  3.  Example 3 (from spec)
    +  4.  Gracious Quit
    +  5.  Quit -> y
    +  6.  Quit -> n
    +  7.  Quit -> other
    +  8.  Full Game #1
    -  9.  Back/History
--------------------------------------------------------------------------------
Naming
--------------------------------------------------------------------------------
    +  1. get_position_in_direction
    +  2. print_maze
    +  3. move
    +  4. get_legal_directions
    +  5. interact
--------------------------------------------------------------------------------
Docstrings
--------------------------------------------------------------------------------
    +  1. get_position_in_direction
    +  2. print_maze
    +  3. move
    +  4. get_legal_directions
    +  5. interact
--------------------------------------------------------------------------------
/------------------------------------------------------------------------------\
|                                 Failed Tests                                 |
\------------------------------------------------------------------------------/
================================================================================
FAIL: interact 9.  Back/History
--------------------------------------------------------------------------------
    'Maze[1018 chars]and: You cannot go back from the beginning.\n\[97 chars] n: ' != 'Maze[1018 chars]and: \n######\n#A   #\n###  #\n#    #\n#P   #\[57 chars] n: '
    Diff is 1288 characters long. Set --diff to see it.

--------------------------------------------------------------------------------
Ran 50 tests in 0.008 seconds with 49 passed/0 skipped/1 failed.


END TESTS
"""

