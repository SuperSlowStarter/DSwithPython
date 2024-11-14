from tkinter import *

window = Tk()
canvas = Canvas(window, height=600, width=600, bg='white')
canvas.pack()

cx = 600//2
cy = 600//2
r = 250
canvas.create_oval(cx-r, cy-r, cx+r, cy+r, width=2, outline="red")

window.mainloop()
