from tkinter import *

window = Tk()
window.geometry("800x600")
canvas = Canvas(window, width=800, height=600, bg="white")

canvas.pack()

canvas.create_rectangle(210, 210, 410, 410, fill="red", outline="black")
canvas.create_polygon(210, 210, 310, 150, 410, 210, fill="yellow", outline="black")



window.mainloop()
