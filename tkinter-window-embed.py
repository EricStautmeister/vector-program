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
ax = fig.add_subplot()
ax.plot([3, 4], [5, 6])

# set mainframe
Mainframe = tk.Frame(root, bg="gray")
Mainframe.place(relheight=1, relwidth=1)

# include graph
canvas = FigureCanvasTkAgg(fig, master=Mainframe)
canvas.get_tk_widget().place(relx=0.35, rely=0.03, relheight=0.7, relwidth=0.632)

# create buttonframe and buttons
Buttonframe = tk.Frame(master=Mainframe, bg="yellow")
Buttonframe.place(relx=0.0175, relwidth=0.315, rely=0.03, relheight=0.7)


button_2d = tk.Button(master=Buttonframe, text="2d")
button_3d = tk.Button(master=Buttonframe, text="3d")

button_2d.place(relx=0.05, relwidth=0.425, rely=0.025, relheight=0.1)
button_3d.place(relx=0.5125, relwidth=0.425, rely=0.025, relheight=0.1)


SettingsFrame = tk.Frame(master=Mainframe, bg="green")
SettingsFrame.place(relx=0.0175, relwidth=0.315, rely=0.75, relheight=0.22)

quit_button = tk.Button(master=SettingsFrame, text="Quit", command=root.quit)
quit_button.place(rely=0.75, relheight=0.22, relx=0.025, relwidth=0.95)

Actionframe = tk.Frame(master=Mainframe, bg="blue")
Actionframe.place(rely=0.75, relheight=0.22, relx=0.35, relwidth=0.632)

tk.mainloop()
