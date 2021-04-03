import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class PltCanvas:

    def __init__(self, main):
        canvas = tk.Canvas(master=main)
        canvas.place(relx=0.35, rely=0.03, relheight=0.7, relwidth=0.632)
        self.fig = plt.figure()

    def create_graph2d(self, xs, ys):
        self.fig = plt.figure()
        ax = self.fig.add_subplot()
        ax.plot(xs, ys)

    def create_graph3d(self, xs, ys, zs=None):
        if zs is None:
            zs = [0, 0]
        self.fig = plt.figure()
        ax = self.fig.add_subplot(projection="3d")
        ax.plot(xs, ys, zs)

    def include_graph(self):
        canv = FigureCanvasTkAgg(self.fig, master=Mainframe)
        canv.get_tk_widget().place(relx=0.35, rely=0.03, relheight=0.7, relwidth=0.632)


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

# set mainframe
Mainframe = tk.Frame(root, bg="gray")
Mainframe.place(relheight=1, relwidth=1)

canvas = PltCanvas(Mainframe)

# create button_frame and buttons
button_frame = tk.Frame(master=Mainframe, bg="yellow")
button_frame.place(relx=0.0175, relwidth=0.315, rely=0.03, relheight=0.7)

button_2d = tk.Button(master=button_frame, text="2D", font="Helvetica 20",
                      command=lambda: canvas.create_graph2d([2, 4], [1, 7]))
button_3d = tk.Button(master=button_frame, text="3D", font="Helvetica 20",
                      command=lambda: canvas.create_graph3d([2, 4], [1, 7], [2, 5]))
enter_button = tk.Button(master=button_frame, text="Enter", command=canvas.include_graph)

button_2d.place(relx=0.05, relwidth=0.425, rely=0.025, relheight=0.1)
button_3d.place(relx=0.5125, relwidth=0.425, rely=0.025, relheight=0.1)
enter_button.place(relx=0.05, relwidth=0.9, rely=0.9, relheight=0.05)

# create settings_frame
settings_frame = tk.Frame(master=Mainframe, bg="green")
settings_frame.place(relx=0.0175, relwidth=0.315, rely=0.75, relheight=0.22)

quit_button = tk.Button(master=settings_frame, text="Quit", command=root.quit)
quit_button.place(rely=0.75, relheight=0.22, relx=0.025, relwidth=0.95)

# create action_frame
action_frame = tk.Frame(master=Mainframe, bg="blue")
action_frame.place(rely=0.75, relheight=0.22, relx=0.35, relwidth=0.632)

tk.mainloop()