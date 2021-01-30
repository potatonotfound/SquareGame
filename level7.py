from time import sleep
try:
    from tkinter import *  # using Python 3
except ImportError:
    from Tkinter import *  # using Python 2
    
root = Tk()
root.title('Square Game')
root.geometry("400x500")
c = Canvas(root, width=400, height=500, bg="yellow")
c.pack()

player= c.create_rectangle(200, 0, 240, 40, fill="cyan")

kill_1 = c.create_rectangle(280, 280, 320, 320, fill="red")

win_1= c.create_rectangle(80, 320, 120, 360, fill="gray")

level = c.create_text(200, 440, text="Level 6", font=("Arial", 50))

dead = False
win_boxes = [False] * 1
win = False

def game_over():
    over = Tk()
    over.title("Game Over!")
    can = Canvas(over, width=200, height=100, bg="red")
    can.pack()
    can.create_text(90, 40, text="Game Over", fill="black", font=('Comic Sans MS', 24))
def win_game():
    import level8
    root.destroy()
def win_boxes_touched():
    global win_boxes
    player_pos = c.coords(player)
    box1_pos = c.coords(win_1)
    if player_pos[0] == box1_pos[0] and player_pos[1] == box1_pos[1] and player_pos[2] == box1_pos[2] and player_pos[3] == box1_pos[3]:
        c.itemconfigure(win_1, fill="green")
        win_boxes[0] = True
        root.update()
      
def if_dead():
    global dead
    player_pos = c.coords(player)
    kill1_pos = c.coords(kill_1)
    if player_pos[0] == kill1_pos[0] and player_pos[1] == kill1_pos[1] and player_pos[2] == kill1_pos[2] and player_pos[3] == kill1_pos[3] and not dead and not win:
        dead = True
        game_over()

def if_win():
    global win_boxes
    global win
    yes = [True] * len(win_boxes)
    if win_boxes ==  yes and not win and not dead:
        win = True
        win_game()


def border():
    pos_player = c.coords(player)
    if pos_player[0] < 0:
        c.move(player, 40, 0)
        root.update()
    elif pos_player[1] < 0:
        c.move(player, 0, 40)
        root.update()
    elif pos_player[2] > 400:
        c.move(player, -40, 0)
        root.update()
    elif pos_player[3] > 400:
        c.move(player, 0, -40)
        root.update()
    elif pos_player[1] == 120:
        c.move(player, 0, -40)
        root.update()

#Player Movements        
def right(event):
    c.move(player, 40, 0)
    root.update()
    sleep(0.05)
    border()
    
    if_dead()
    win_boxes_touched()
    if_win()
    
def left(event):
    c.move(player, -40, 0)
    root.update()
    sleep(0.05)
    
    border()
    if_dead()
    win_boxes_touched()
    if_win()
    
def up(event):
    c.move(player, 0, -40)
    root.update()
    sleep(0.05)
    border()
    
    if_dead()
    win_boxes_touched()
    if_win()
    
def down(event):
    c.move(player, 0, 40)
    root.update()
    sleep(0.05)
    border()
    
    if_dead()
    win_boxes_touched()
    if_win()

    
#Keys
c.bind_all("<KeyPress-Right>", right)
c.bind_all("<KeyPress-Left>", left)
c.bind_all("<KeyPress-Up>", up)
c.bind_all("<KeyPress-Down>", down)   
