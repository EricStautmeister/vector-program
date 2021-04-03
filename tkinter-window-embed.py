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

# create button_frame and buttons
button_frame = tk.Frame(master=Mainframe, bg="yellow")
button_frame.place(relx=0.0175, relwidth=0.315, rely=0.03, relheight=0.7)

quit_button = tk.Button(master=button_frame, text="Quit", command=root.quit())
button_2d = tk.Button(master=button_frame, text="2d")
button_3d = tk.Button(master=button_frame, text="3d")

button_2d.place(relx=0.05, relwidth=0.425, rely=0.025, relheight=0.05)
button_3d.place(relx=0.5125, relwidth=0.425, rely=0.025, relheight=0.05)
quit_button.place(rely=0.925, relheight=0.05, relx=0.05, relwidth=0.9)

settings_frame = tk.Frame(master=Mainframe, bg="green")
settings_frame.place(relx=0.0175, relwidth=0.315, rely=0.75, relheight=0.22)

action_frame = tk.Frame(master=Mainframe, bg="blue")
action_frame.place(rely=0.75, relheight=0.22, relx=0.35, relwidth=0.632)

tk.mainloop()
