import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np


root = tkinter.Tk()
root.wm_title("Embedding in Tk")

fig = plt.figure()
ax = fig.add_subplot().plot([9, 5, 10, 20],
                            [5, 6, 6, 7])

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()

button = tkinter.Button(master=root, text="Quit", command=root.quit)


def randfunc():
    pass
randButton = tkinter.Button(master=root, text="Test Button", command=randfunc)

button.pack(side=tkinter.BOTTOM)
randButton.pack(side=tkinter.BOTTOM)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

tkinter.mainloop()
