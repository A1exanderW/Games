#!/usr/bin/env python3
################################################################################
#
#   CSSE1001/7030 - Assignment 3
#
#   Student Username: s4318841
#
#   
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
        self._status.pack(side=tk.BOTTOM)
        
        # Create reset button
        Button1=tk.Button(master,text = "Reset status", command = self._reset).pack(side = tk.BOTTOM)

        #create a file menu
        self._filemenu=Filemenu(master, self._player)

        menubar=tk.Menu(self._master)
        self._master.config(menu=menubar)
        filemenu=tk.Menu(menubar)
        
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New Game", command=self.new_game)
        filemenu.add_command(label="Exit", command=self.exit_game)
        
    def new_game(self):
        """ Attempts to start a new game, which involves resetting the current swaps and score status,
            if grid is being resolved it will raise an error. 
        """

        if self._grid_view.is_resolving()==True:
            new_game_messagebox=tk.messagebox.showerror('Error:', 'Cannot quit when grid is resolving, please wait ')

        else:
            self._game.reset()
            self._grid_view.draw()
            self._player.reset_score()
            self._status.score()
            self._player.reset_swaps()
            self._status.swaps()        
        
    def exit_game(self):
        """ Exits the game
        """
        self._master.destroy()
               

    def _reset(self):
        """
        Resets the player and status bar score and swaps
        """
        
        self._player.reset_score()
        self._status.score()
        self._player.reset_swaps()
        self._status.swaps()

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
        """
        Adds a score
        """
        self._score=str(score)
        return self._score

    def get_score(self):
        """
        Returns the current score
        """
        return self._score
        

    def reset_score(self):
        """
        Resets the players score and score status
        """
        self._player.reset_score
        self._status.score()

    def record_swap(self):
        """
        Records swaps
        """
        pass

    def get_swaps(self):
        """
        Returns swaps
        """
        pass

    def reset_swaps(self):
        """
        Resets the players swap count
        """
        self._player.reset_swaps
        self._status.swaps()
        
    
    def get_health(self):
        """
        prints the players health
        """        
        print("SimplePlayer health: {}".format(get_health()))
            

    def _handle_swap(self, from_pos, to_pos):
        """
        Run when a swap on the grid happens.
        """
        print("SimplePlayer made a swap from {} to {}!".format(
            from_pos, to_pos))
        self._player.record_swap()
        self._status.swaps()

    def _handle_score(self, score):
        """
        Run when a score update happens.
        """
        print("SimplePlayer scored {}!".format(score))
        self._player.add_score(10)
        self._status.score()

class SimplePlayer(object):
    """
    Creates a SimplePlayer
    """
    def __init__(self):
        """
        Constructor()
        """
        self._score=0
        self._scorecount=0
        self._swapscount=0

    def add_score(self, score):
        """
        Adds a score to the player scorecount
        Simpleplayer.add_score(int) -> int
        """
        self._score+=score
        return self._score

    def get_score(self):
        """
        Returns the players scorecount
        SimplePlayer.get_score() -> int
        """
        return self._score

    def reset_score(self):
        """
        Resets the player's scorecount
        SimplePlayer.reset_score() -> None
        """
        self._score=0
       
    def record_swap(self):
        """
        Adds 1 to the player's swapcount
        SimplePlayer.record_swap() -> None
        """
        self._swapscount+=1

    def get_swaps(self):
        """
        Returns the player's swapcount
        SimplePlayer.get_swaps() -> Int
        """
        return self._swapscount
       
    def reset_swaps(self):
        """
        Resets the player's swapcount
        SimplePlayer.reset_swaps()-> Int
        """
        self._swapscount=0

class SimpleStatusBar(tk.Frame):
    """
    Represents the player's status: displays the number of swaps the player has made and player's score.
    """
    def __init__(self, master, player):
        """
        Constructor: SimpleStatusBar(tk.Frame,player)->GUI
        """
        super().__init__(master)
        master.title('Simpletile Game')
        frame1=tk.Frame(master)
        frame2=tk.Frame(master)
        
        frame1.pack(side=tk.BOTTOM, expand=True, fill=tk.X)
        self._player = player

        self._swapstext=tk.Label(frame1, text='Swaps:')
        self._swapstext.pack(side=tk.LEFT, padx=20)
        self._swaps_label=tk.Label(frame1, text=str(0), bd=1, relief=tk.SUNKEN)
        self._swaps_label.pack(side=tk.LEFT)

        self._score_label=tk.Label(frame1,text=str(0), bd=1, relief=tk.SUNKEN)
        self._score_label.pack(side=tk.RIGHT, padx=20)
        self._scoretext=tk.Label(frame1, text='Score:')
        self._scoretext.pack(side=tk.RIGHT)
       

    def swaps(self):
        """
        Configures the swaps_label to display the player's swap count
        SimpleStatusBar.swaps() -> tk.Label
        """
        
        self._swaps_label.config(text=str(self._player.get_swaps()))
        

    def score(self):
        """
        Configures the score_label to display the player's score
        SimpleStatusBar.score() -> tk.Label
        """
        
        self._score_label.config(text=str(self._player.get_score()))

class VersusStatusBar(tk.Frame):
    """
    Reprsents the status of the game, player and enemy. It displays the current level, player's health,
    enemy's healh and the number of swaps made.
    
    """
    def __init__(self, master, player):
        super().__init__(master)
        master.title('Tile Game')
        
        self._player = player
        

        self._width=110
        self._changewidth=self._width-10
        
                                
        self._lbl = tk.Label(master, text="LEVEL 1")
        self._lbl.pack(side=tk.TOP, expand='100')

        self._frame1=tk.Frame(master)
        self._frame2=tk.Frame(master)
        self._frame1.pack(side=tk.TOP, expand=True, fill=tk.X)
        self._frame2.pack(side=tk.TOP, expand=True, fill=tk.X)
        

        self._health_player=tk.Label(self._frame1, text='Health:')
        self._health_player.pack(side=tk.LEFT)
        self._health_label=tk.Label(self._frame1, text=str(PLAYER_BASE_HEALTH))
        self._health_label.pack(side=tk.LEFT, padx=50)

        self._health_label2=tk.Label(self._frame1, text=str(PLAYER_BASE_HEALTH))
        self._health_label2.pack(side=tk.RIGHT)        
        self._health_enemy=tk.Label(self._frame1, text='Health:')
        self._health_enemy.pack(side=tk.RIGHT, padx=48)
        

        self._canvas1=tk.Canvas(self._frame2, bg='blue', width= self._width, height=15)
        self._canvas1.pack(side=tk.LEFT, padx=2, expand=True, anchor=tk.W)
                
        self._canvas2=tk.Canvas(self._frame2, bg='red', width= self._width, height=15)
        self._canvas2.pack(side=tk.LEFT, expand=True, anchor=tk.E)

##        def damage_enemy(self):
####            if self._player.get_swaps():
##            self._versusbar.config(width=self._changewidth)
##
##        def damage_player(self):
##            self._versusbar.config(width=self._canvaswidth)

class Filemenu(tk.Frame):
    """
    Creates a file menu with the follow items: New Game- which resets the tiles and the SimpleStatusbar,
    Exit- which terminates the game
    """
    def __init__(self, master, player):
        """
        Constructor:Filemenu(tk.Frame, player)-> GUI
        """
        super().__init__(master)
        self._master=master
                                   
        self._frame=tk.Frame(master, bg='yellow')
        self._frame.pack(side=tk.BOTTOM)

        #File menu
        menubar=tk.Menu(self._master)
        self._master.config(menu=menubar)
        filemenu=tk.Menu(menubar)
        

class ImageTileGridView(TileGridView):
    """
    Visual representation of a TileGrid."
    """
    
    def __init__(self, master, grid, *args, width=GRID_WIDTH,
               height=GRID_HEIGHT, cell_width=GRID_CELL_WIDTH, 
               cell_height=GRID_CELL_HEIGHT, **kwargs):
        """
        Constructor(tk.Frame, TileGrid, *, int, int, int, int, *)

        :param master: The tkinter master widget/window.
        :param width: Total width of the grid.
        :param height: Total height of the grid.
        :param cell_width: Width of each cell.
        :param cell_height: Height of each cell.
        """
        
        
        self._tile_images={'red':tk.PhotoImage(file='fire.gif'), 'green':tk.PhotoImage(file='poison.gif'),
                           'blue':tk.PhotoImage(file='water.gif'),'gold':tk.PhotoImage(file='coin.gif'),
                           'purple':tk.PhotoImage(file='psychic.gif'),'light sky blue':tk.PhotoImage(file='ice.gif')}
              

        super().__init__(master, grid, *args, width=width,
                         height=height, cell_width=cell_width,
                         cell_height=cell_height, **kwargs)

    def draw_tile_sprite(self, xy_pos, tile, selected):
        """Draws the sprite for the given tile at given (x, y) position.
        ImageTileGridView.draw_tile_sprite(TileGridView, (int, int), Tile, bool)
        -> None"""

        colour = tile.get_colour()
        width, height = self._calculate_tile_size(xy_pos, selected)
        x, y = xy_pos

        return self.create_image(x,y,image=self._tile_images[colour])


class Character(object):
    """
    Represents the basic functionality of a player or enemy within the game.
    """
    
    def __init__(self, max_health):
        """
        Constructor: Character(int)
        """
        self._max_health= max_health
        self._health=max_health

    def get_max_health(self):
        """
        Returns the max health of the character
        Character.get_max_health()-> int
        """
        return self._max_health

    def get_health(self):
        """
        Returns the health of the character
        Character.get_health()-> Int
        """
        return self._health

    def lose_health(self, amount):
        """
        Decreases the health of the character by amount
        Character.lose_health(int) -> None
        """
        if self._health-amount>=0:
            self._health-=amount
        else:
            self._health=0
            
    def gain_health(self, amount):
        """
        Increases health of the character by amount
        Character.gain_health(int)-> None
        """
        if self._health+amount<=self._max_health:
            self._health+=amount
        else:
            self._health=self._max_health           

    def reset_health(self):
        """
        Resets the health of character
        Character.reset_health()-> None
        """
        self._health=self._max_health

    
     
class Enemy(Character):
    """
    Represents the enemy character
    """
    
    def __init__(self, type, max_health, attack):
        """
        Constructor: Enemy(str, int, (int,int))
        """
        self._type=type
        self._attack=attack
        self._damage=0

    def get_type(self):
        """
        Returns the enemy type
        Enemy.get_type() -> str
        """
        return self._type

    def attack(self):
        """
        Returns a random integer in the enemy's attack range
        Enemy.attack() -> int
        """
        return random.randint(self._attack[0],self._attack[1])


class Player(Character):
    def __init__(self, max_health, swaps_per_turn, base_attack):
        """ Constructs the player, max_health is an integer represnting the health of the player,
        swaps_per_turn is an integer representing no. of swaps a player can make each turn,
        base_attack is the player's base attack
        Constructor: Player(int, int, int)
        """
        
##        super().init(self, max_health)
        self._type=[]
        self._swapscount=0
        self._base_attack=base_attack
        self._swaps=swaps_per_turn
        self._attack=[]
        self._damage=[]
        self._max=0
        self._length=0
      
    def record_swap(self):
        """
        Adds a swap to swapcount
        Player.record_swap() -> None
        """
        
        if self._swaps-1>=0:
            self._swaps-=1
        else:
            self._swaps=0
        
    def get_swaps(self):
        """
        Returns player's swap count
        Player.get_swaps()-> int
        """
        
        return self._swaps

    def attack(self, runs, defender_type):
        """Takes a list of Run instances and a defender type, then returns a list of pairs
        of the form (tile,damage)
        Player.attack(list(runs), str) -> [(str, int), (str, int)]
        """
        for i in runs:
                self._max+=i.get_max_dimension()
                self._length+=i.__len__()
                A=i.__getitem__(i.find_dominant_cell())
                self._type.append(A.get_type())
                self._damage= self._base_attack*self._length*self._max
                (x,y)=(A.get_type(),self._damage)
                self._attack.append((x,y))
        return(self._attack)

    def reset_swaps(self):
        """
        Resets the player's swap count
        Player.reset_swaps() -> none
        """
        self._swapscount=0
        

class SinglePlayerTileApp(SimpleTileApp):
    """
    SingleplayerTileapp is responsible for displaying the top-level GUI, it has the follow features:
    ImageTileGRidView, VersusStatusBar, graphics and file menu
    """
    
    def __init__(self, master):
        """
        Constructor: SinglePLayerTileApp(tk.Frame)
        """
        self._master = master
        self._game = SimpleGame()

        self._game.on('swap', self._handle_swap)
        self._game.on('score', self._handle_score)

        self._player = SimplePlayer()
        self._char_images={}
        self._level=1

        self._player_swaps_per_turn=SWAPS_PER_TURN
        self._player_health=PLAYER_BASE_HEALTH
        self._player_base_attack=PLAYER_BASE_ATTACK

        self._enemy_stats=(generate_enemy_stats(self._level))
        self._enemy_health=self._enemy_stats[0]
        self._enemy_attackrange=self._enemy_stats[1]

        #Creates a status bar
        self._status = SimpleStatusBar(master, self._player)
        self._status.pack(side=tk.BOTTOM)

        #Creates a versus bar
        self._versusstatus=VersusStatusBar(master, self._player)
        self._versusstatus._lbl.config(text='Level: {}'.format(self._level))
        self._versusstatus._health_label.config(text=self._player_health)    
        self._versusstatus._health_label2.config(text=self._enemy_health)        
        self._versusstatus.pack(side=tk.TOP)

        
        #Creates character images 
        self._canvas= tk.Canvas(master, width = 100, height = 150)
        self._canvas.pack(side=tk.TOP,expand=1, fill=tk.X)
        
        self._char_images={'player':tk.PhotoImage(file='player.gif'),
                           'enemy1':tk.PhotoImage(file='enemy_1.gif'),
                           'enemy2':tk.PhotoImage(file='enemy_2.gif'),
                           'enemy3':tk.PhotoImage(file='enemy_3.gif'),
                           'enemy4':tk.PhotoImage(file='enemy_4.gif'),
                           'enemy5':tk.PhotoImage(file='enemy_5.gif')}
        
        #creates a dictionary to store image
        self._canvas.create_image(50,100,image=self._char_images['player'])
        self._canvas.create_image(500,100,image=self._char_images['enemy{}'.format(self._level)])       

        self._image_grid_view=ImageTileGridView(master, self._game.get_grid(),
                                       width=GRID_WIDTH, height=GRID_HEIGHT, bg='black')
        self._image_grid_view.pack(side=tk.TOP, expand=True, fill=tk.BOTH)            
          
        #create a file menu
        self._filemenu=Filemenu(master, self._player)

        menubar=tk.Menu(self._master)
        self._master.config(menu=menubar)
        filemenu=tk.Menu(menubar)
        
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New Game", command=self.new_game)
        filemenu.add_command(label="Exit", command=self.exit_game)
        
    def new_game(self):
        """ Attempts to create a new game: if image grid is resolving an error will be raised,
        otherwise, a confirmation message box will be raised: if Yes is selected the game will reset,
        else nothing will happen
        SinglePlayerTileApp()

        """

        if self._image_grid_view.is_resolving()==True:
            new_game_messagebox=tk.messagebox.showerror('Error:', 'Cannot quit when grid is resolving, please wait.. ')                        

        else:
            confirmation_messagebox=tk.messagebox.askyesno('New Game', 'Are you sure you want to start a new game?')
            if confirmation_messagebox:
                self._game.reset()
                self._image_grid_view.draw()
                self._player.reset_score()
                self._status.score()
                self._player.reset_swaps()
                self._status.swaps()
            else:
                pass
        
    def exit_game(self):
        self._master.destroy()

        
    def _reset(self):
        """
        Resets the player and status bar score and swaps
        """
        self._player.reset_score()
        self._status.score()
        self._player.reset_swaps()
        self._status.swaps()


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
        self._player.add_score(10)
        self._status.score()        
        A=self._enemy_health-self._player_base_attack

        if A>0:
            self._enemy_health-=self._player_base_attack
            self._versusstatus._health_label2.config(text=self._enemy_health)

        else:
            self._level+=1   
            self._enemy_health=0
            self._versusstatus._health_label2.config(text=self._enemy_health)                     
            self._image_grid_view.draw()
                     
            self._canvas.create_image(500,100,image=self._char_images['enemy{}'.format(self._level)])    
            self._player.reset_score()
            self._status.score()
            self._player.reset_swaps()
            self._status.swaps()                
            self._enemy_health=self._enemy_stats[0]                      

        print("SimplePlayer scored {}!".format(score))

    def add_score(self, score):
        """
        Adds a score
        """
        self._score=str(score)
        return self._score

    def get_score(self):
        """
        Returns the current score
        """        
        return self._score
        

    def reset_score(self):
        """
        Resets the players score and score status
        """
        self._player.reset_score
        self._status.score()

    def record_swap(self):
        pass

    def get_swaps(self):
        pass

    def reset_swaps(self):
        self._player.reset_swaps
        self._status.swaps()
        
    
    def get_health(self):
        print("SimplePlayer health: {}".format(get_health()))

    def _handle_swap(self, from_pos, to_pos):
        """
        Run when a swap on the grid happens.
        """
        print("SimplePlayer made a swap from {} to {}!".format(
            from_pos, to_pos))
        self._player.record_swap()
        self._status.swaps()

 
###############################################################################################################
def task1():
    root=tk.Tk()
    SimpleTileApp(root)
    root.mainloop()    


def task2():
    root=tk.Tk()
    SinglePlayerTileApp(root)
    root.mainloop()    
    

def task3():
    # Add task 3 GUI instantiation code here
    pass

def main():
    # Choose relevant task to run
    task2()  
    
if __name__ == '__main__':
    main()
