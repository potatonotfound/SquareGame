from time import sleep
try:
    from tkinter import *  # using Python 3
except ImportError:
    from Tkinter import *  # using Python 2
    
root = Tk()
root.title('Square Game')
l = Label(root, text="You Win!")
l.pack()
