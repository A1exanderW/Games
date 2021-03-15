#!/usr/bin/env python3
################################################################################
#
#   CSSE1001/7030 - Assignment 3
#
#   Student Username: s4318841
#
#   Student Name: Alexander Wang
#
################################################################################

# VERSION 1.0.1

################################################################################
#
# The following is support code. DO NOT CHANGE.

from a3_support import *


# End of support code
################################################################################
# Write your code below
################################################################################

# Write your classes here (including import statements, etc.)


class SimpleTileApp(object):
    def __init__(self, master):
        """
        Constructor(SimpleTileApp, tk.Frame)
        """
        self._master = master

        self._game = SimpleGame()

        self._game.on('swap', self._handle_swap)
        self._game.on('score', self._handle_score)

        self._player = SimplePlayer()


        self._grid_view = TileGridView(
            master, self._game.get_grid(),
            width=GRID_WIDTH, height=GRID_HEIGHT, bg='black')
        self._grid_view.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        
        #Creates a status bar
        self._status = SimpleStatusBar(master, self._player)
        self._status.pack(side=tk.BOTTOM, fill=tk.X)

        # Create reset button
        Button1=tk.Button(text = "Reset", command = self._reset).pack(side = tk.BOTTOM)

    def _reset(self):
        print("Reset")

        # Add your code here

    def _handle_swap(self, from_pos, to_pos):
        """
        Run when a swap on the grid happens.
        """
        print("SimplePlayer made a swap from {} to {}!".format(
            from_pos, to_pos))

    def _handle_score(self, score):
        """
        Run when a score update happens.
        """
        print("SimplePlayer scored {}!".format(score))

    def add_score(self, score):
        self._score=str(score)
        return self._score

    def get_score(self):
        return self._score
        

    def reset_score(self):
        pass

    def record_swap(self):
        pass

    def get_swaps(self):
        pass

    def reset_swaps(self):
        pass

    def _handle_swap(self, from_pos, to_pos):
        """
        Run when a swap on the grid happens.
        """
        print("SimplePlayer made a swap from {} to {}!".format(
            from_pos, to_pos))

    def _handle_score(self, score):
        """
        Run when a score update happens.
        """
        print("SimplePlayer scored {}!".format(score))

class SimplePlayer(object):
    def __init__(self):
        self._score=0
        self._scorecount=0
        self._swapscount=0

    def add_score(self, score):
        self._score+=score
        return self._score

    def get_score(self):
        return self._score

    def reset_score(self):
        self._score=0
       
    def record_swap(self):
        self._swapscount+=1

    def get_swaps(self):
        return self._swapscount
       
    def reset_swaps(self):
        self._swapscount=0

class SimpleStatusBar(tk.Frame):
    def __init__(self, master, player):
       
        super().__init__(master)

        self._player = player
##        self._simpleplayer=SimplePlayer()
        swaps_label=tk.Label(master, text= self._player.get_swaps(), bd=1, relief=tk.SUNKEN)
        swaps_label.pack(side=tk.LEFT)
        score_label=tk.Label(master, text= self._player.get_score(), bd=1, relief=tk.SUNKEN)
        score_label.pack(side=tk.LEFT)
        

        ##    # Reset button#

    def resetStatus():
        player.reset_score()
        player.reset_swaps()
        reset_button=tk.Button(root, text='Reset Status', command=resetStatus)
        reset_button.pack()

class Character(object):
    def __init__(self, max_health):
        self._max_health= max_health
        self._health=max_health

    def get_max_health(self):
        return self._max_health

    def get_health(self):
        return self._health

    def lose_health(self, amount):
        if self._health-amount>=0:
            self._health-=amount
        else:
            self._health=0
            
    def gain_health(self, amount):
        if self._health+amount<=self._max_health:
            self._health+=amount
        else:
            self._health=self._max_health           

    def reset_health(self):
        self._health=self._max_health
     
class Enemy(Character):
    def __init__(self, type, max_health, attack):
        self._type=type
        self._attack=attack

    def get_type(self):
        return self._type

    def attack(self):
        return random.randint(self._attack[0],self._attack[1])


class Player(Character):
    def __init__(self, max_health, swaps_per_turn, base_attack):
##        super().init(self, max_health)
        self._type= type
        self.base_attack=base_attack
        self._swaps=swaps_per_turn
      
    def record_swap(self):
        if self._swaps-1>=0:
            self._swaps-=1
        else:
            self._swaps=0
        return self._swaps

    def get_swaps(self):
        return self._swaps

    def attack(self, runs, defender_type):
        pass       

def task1():
    master=tk.Tk()
    SimpleTileApp(master)
    master.mainloop()    



def task2():
    # Add task 2 GUI instantiation code here
    pass


def task3():
    # Add task 3 GUI instantiation code here
    pass


def main():
    # Choose relevant task to run
    task1()


if __name__ == '__main__':
    main()
