<<<<<<< HEAD
import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
=======
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
>>>>>>> df68062b40b8f7ab5e72495993f9c4b8ebeed0a8
import matplotlib.pyplot as plt
import numpy as np


# create main window
root = tk.Tk()
root.title("Embedding in Tk")

<<<<<<< HEAD
fig = plt.figure()
ax = fig.add_subplot().plot([9, 5, 10, 20],
                            [5, 6, 6, 7])
=======
# get screen size and center the generalised window
screen_Height = root.winfo_screenheight()
screen_Width = root.winfo_screenwidth()

Height = screen_Height/1.1
Width = screen_Width/1.1

x_cord = screen_Width / 2 - Width / 2
y_cord = (screen_Height - 80) / 2 - Height / 2
>>>>>>> df68062b40b8f7ab5e72495993f9c4b8ebeed0a8

root.geometry("%dx%d+%d+%d" % (Width, Height, x_cord, y_cord))

# create graph
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.plot([3, 4], [5, 6])

<<<<<<< HEAD
button = tkinter.Button(master=root, text="Quit", command=root.quit)
=======
# set mainframe
Mainframe = tk.Frame(root, bg="gray")
Mainframe.place(relheight=1, relwidth=1)

# include graph
canvas = FigureCanvasTkAgg(fig, master=Mainframe)
canvas.get_tk_widget().place(relx=0.45, rely=0.03, relheight=0.7, relwidth=0.525)

Actionframe = tk.Frame(master=Mainframe, bg="yellow")
Actionframe.place(relx=0.025, relwidth=0.4, rely=0.03, relheight=0.45)

Calculateframe = tk.Frame(master=Mainframe, bg="green")
Calculateframe.place(relx=0.025, relwidth=0.4, rely=0.5, relheight=0.47)
>>>>>>> df68062b40b8f7ab5e72495993f9c4b8ebeed0a8

# create and add buttons
Buttonframe = tk.Frame(master=Mainframe, bg="blue")
Buttonframe.place(rely=0.75, relheight=0.22, relx=0.45, relwidth=0.525)

button = tk.Button(master=Buttonframe, text="Quit", command=root.quit)
randButton = tk.Button(master=Buttonframe, text="Test Button", command=lambda: print("press"))

<<<<<<< HEAD
button.pack(side=tkinter.BOTTOM)
randButton.pack(side=tkinter.BOTTOM)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
=======
button.grid()
randButton.grid()
>>>>>>> df68062b40b8f7ab5e72495993f9c4b8ebeed0a8

tk.mainloop()
