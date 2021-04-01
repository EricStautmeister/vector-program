import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np


root = tk.Tk()
root.title("Embedding in Tk")

screen_Height = root.winfo_screenheight()
screen_Width = root.winfo_screenwidth()

Height = screen_Height/1.1
Width = screen_Width/1.1

x_cord = screen_Width / 2 - Width / 2
y_cord = (screen_Height - 80) / 2 - Height / 2

root.geometry("%dx%d+%d+%d" % (Width, Height, x_cord, y_cord))

fig = plt.figure()
ax = fig.add_subplot()
ax.plot([3, 4], [5, 6])
# ax.set_xlim(0, 6)
# ax.set_ylim(0, 6)

Mainframe = tk.Frame(root)
Mainframe.place(relheight=1, relwidth=1)

canvas = FigureCanvasTkAgg(fig, master=Mainframe)  # A tk.DrawingArea.
canvas.draw()

button = tk.Button(master=Mainframe, text="Quit", command=root.quit)

randButton = tk.Button(master=Mainframe, text="Test Button", command=lambda: print("press"))

button.place(relx=0.45, rely=0.95, anchor="n")
randButton.place(relx=0.5, rely=0.95, anchor="n")
canvas.get_tk_widget().place(relx=0.45, rely=0.05, relheight=0.7, relwidth=0.5)

tk.mainloop()
