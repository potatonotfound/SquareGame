from time import sleep
try:
    from tkinter import *  # using Python 3
except ImportError:
    from Tkinter import *  # using Python 2
    
root = Tk()
root.title('Square Game')
root.geometry("400x500")
c = Canvas(root, width=400, height=500)
c.pack()

player= c.create_rectangle(200, 0, 240, 40, fill="cyan")
orange = c.create_rectangle(0, 0, 40, 40, fill="orange")
blue = c.create_rectangle(360, 360, 400, 400, fill="blue")

kill_1 = c.create_rectangle(280, 280, 320, 320, fill="red")
kill_2 = c.create_rectangle(80, 80, 120, 120, fill="red")
kill_3 = c.create_rectangle(200, 200, 240, 240, fill="red")
kill_4 = c.create_rectangle(320, 320, 360, 360, fill="red")
kill_5 = c.create_rectangle(40, 40, 80, 80, fill="red")

win_1 = c.create_rectangle(0, 80, 40, 120, fill="gray")
win_2= c.create_rectangle(360, 160, 400, 200, fill="gray")
win_3= c.create_rectangle(200, 240, 240, 280, fill="gray")
win_4= c.create_rectangle(360, 0, 400, 40, fill="gray")
win_5= c.create_rectangle(0, 360, 40, 400, fill="gray")
level = c.create_text(200, 440, text="Level 2", font=("Arial", 50))

dead = False
win_boxes = [False] * 5
win = False

def game_over():
    over = Tk()
    over.title("Game Over!")
    can = Canvas(over, width=200, height=100, bg="red")
    can.pack()
    can.create_text(90, 40, text="Game Over", fill="black", font=('Comic Sans MS', 24))
def win_game():
    import level3
    root.destroy()
def win_boxes_touched():
    global win_boxes
    player_pos = c.coords(player)
    box1_pos = c.coords(win_1)
    box2_pos = c.coords(win_2)
    box3_pos = c.coords(win_3)
    box4_pos = c.coords(win_4)
    box5_pos = c.coords(win_5)
    if player_pos[0] == box1_pos[0] and player_pos[1] == box1_pos[1] and player_pos[2] == box1_pos[2] and player_pos[3] == box1_pos[3]:
        c.itemconfigure(win_1, fill="green")
        win_boxes[0] = True
        root.update()
    elif player_pos[0] == box2_pos[0] and player_pos[1] == box2_pos[1] and player_pos[2] == box2_pos[2] and player_pos[3] == box2_pos[3]:
        c.itemconfigure(win_2, fill="green")
        win_boxes[1] = True
        root.update()
    elif player_pos[0] == box3_pos[0] and player_pos[1] == box3_pos[1] and player_pos[2] == box3_pos[2] and player_pos[3] == box3_pos[3]:
        c.itemconfigure(win_3, fill="green")
        win_boxes[2] = True
        root.update()
    elif player_pos[0] == box4_pos[0] and player_pos[1] == box4_pos[1] and player_pos[2] == box4_pos[2] and player_pos[3] == box4_pos[3]:
        c.itemconfigure(win_4, fill="green")
        win_boxes[3] = True
        root.update()
    elif player_pos[0] == box5_pos[0] and player_pos[1] == box5_pos[1] and player_pos[2] == box5_pos[2] and player_pos[3] == box5_pos[3]:
        c.itemconfigure(win_5, fill="green")
        win_boxes[4] = True
        root.update()
      
def if_dead():
    global dead
    player_pos = c.coords(player)
    kill1_pos = c.coords(kill_1)
    kill2_pos = c.coords(kill_2)
    kill3_pos = c.coords(kill_3)
    kill4_pos = c.coords(kill_4)
    kill5_pos = c.coords(kill_5)
    if player_pos[0] == kill1_pos[0] and player_pos[1] == kill1_pos[1] and player_pos[2] == kill1_pos[2] and player_pos[3] == kill1_pos[3] and not dead and not win:
        dead = True
        game_over()
    if player_pos[0] == kill2_pos[0] and player_pos[1] == kill2_pos[1] and player_pos[2] == kill2_pos[2] and player_pos[3] == kill2_pos[3] and not dead and not win:
        dead = True
        game_over()
    if player_pos[0] == kill3_pos[0] and player_pos[1] == kill3_pos[1] and player_pos[2] == kill3_pos[2] and player_pos[3] == kill3_pos[3] and not dead and not win:
        dead = True
        game_over()
    if player_pos[0] == kill4_pos[0] and player_pos[1] == kill4_pos[1] and player_pos[2] == kill4_pos[2] and player_pos[3] == kill4_pos[3] and not dead and not win:
        dead = True
        game_over()
    if player_pos[0] == kill5_pos[0] and player_pos[1] == kill5_pos[1] and player_pos[2] == kill5_pos[2] and player_pos[3] == kill5_pos[3] and not dead and not win:
        dead = True
        game_over()

def if_win():
    global win_boxes
    global win
    yes = [True] * len(win_boxes)
    if win_boxes ==  yes and not win and not dead:
        win = True
        win_game()

def portal():
    pos_player= c.coords(player)
    pos_o= c.coords(orange)
    pos_b = c.coords(blue)
    if (pos_player[0] == pos_o[0] and pos_player[1] == pos_o[1] and pos_player[2] == pos_o[2] and pos_player[3] == pos_o[3]):
        c.move(player, pos_b[1] - 40, pos_b[3])
        root.update()
    elif (pos_player[0] == pos_b[0] and pos_player[1] == pos_b[1] and pos_player[2] == pos_b[2] and pos_player[3] == pos_b[3]):
        c.move(player, (pos_b[1] - 40) * -1, pos_b[3] * -1)
        root.update()

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
    portal()
    if_dead()
    win_boxes_touched()
    if_win()
    
def left(event):
    c.move(player, -40, 0)
    root.update()
    sleep(0.05)
    portal()
    border()
    if_dead()
    win_boxes_touched()
    if_win()
    
def up(event):
    c.move(player, 0, -40)
    root.update()
    sleep(0.05)
    border()
    portal()
    if_dead()
    win_boxes_touched()
    if_win()
    
def down(event):
    c.move(player, 0, 40)
    root.update()
    sleep(0.05)
    border()
    portal()
    if_dead()
    win_boxes_touched()
    if_win()

#Keys
c.bind_all("<KeyPress-Right>", right)
c.bind_all("<KeyPress-Left>", left)
c.bind_all("<KeyPress-Up>", up)
c.bind_all("<KeyPress-Down>", down)   
