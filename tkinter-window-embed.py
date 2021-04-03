import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np


# create main window
root = tk.Tk()
root.title("Embedding in Tk")

# get screen size and center the generalised window
screen_Height = root.winfo_screenheight()
screen_Width = root.winfo_screenwidth()

Height = screen_Height/1.1
Width = screen_Width/1.1

x_cord = screen_Width / 2 - Width / 2
y_cord = (screen_Height - 80) / 2 - Height / 2

root.geometry("%dx%d+%d+%d" % (Width, Height, x_cord, y_cord))

# create graph
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.plot([3, 4], [5, 6])

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

# create and add buttons
Buttonframe = tk.Frame(master=Mainframe, bg="blue")
Buttonframe.place(rely=0.75, relheight=0.22, relx=0.45, relwidth=0.525)

button = tk.Button(master=Buttonframe, text="Quit", command=root.quit)
randButton = tk.Button(master=Buttonframe, text="Test Button", command=lambda: print("press"))

button.grid()
randButton.grid()

tk.mainloop()
