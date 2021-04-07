import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class PltFrame:
    """Class for implementing matplotlib graph into tkinter"""
    def __init__(self, main):
        self.plot_frame = tk.Frame(master=main, bg=frame_bg)
        self.plot_frame.place(relx=0.35, rely=0.03, relheight=0.7, relwidth=0.632)
        self.fig = plt.figure()
        self.plot_img = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.plot_img.get_tk_widget().place(relwidth=1, relheight=1)

    def create_graph2d(self, xs, ys):
        self.fig.clear()
        ax = self.fig.add_subplot()
        ax.plot(xs, ys)
        self.draw_plot()

    def create_graph3d(self, xs, ys, zs=None):
        if zs is None:
            zs = [0, 0]
        self.fig.clear()
        ax = self.fig.add_subplot(projection="3d")
        ax.plot(xs, ys, zs)
        self.draw_plot()

    def draw_plot(self):
        self.plot_img.draw()


VECTORS = []

# color variables
bg = "#282c34"
canvas_bg = "#505255"
frame_bg = "#505255"
button_bg = "#A9B6C9"

# create main window
root = tk.Tk()
root.iconbitmap('wave-square-solid.ico')
root.title("Vector Program")
root.geometry("+250+2500")
root.lift()

# get screen size and center the generalised window
screen_Height = root.winfo_screenheight()
screen_Width = root.winfo_screenwidth()

Height = screen_Height/1.1
Width = screen_Width/1.1

x_cord = screen_Width / 2 - Width / 2
y_cord = (screen_Height - 80) / 2 - Height / 2

root.geometry("%dx%d+%d+%d" % (Width, Height, x_cord, y_cord))

# set mainframe
Mainframe = tk.Frame(root, bg=bg)
Mainframe.place(relheight=1, relwidth=1)

plot_frame = PltFrame(Mainframe)

# create button_frame and buttons
vector_frame = tk.Frame(master=Mainframe, bg=frame_bg)
vector_frame.place(relx=0.0175, relwidth=0.315, rely=0.03, relheight=0.7)

vector_name = tk.Label(master=vector_frame, text="Vectors", font="Helvetica 24")
vector_list = tk.Label(master=vector_frame)
vector_name.place(relx=0.02, rely=0.015, relwidth=0.96, relheight=0.05)
vector_list.place(rely=0.075, relx=0.25, relwidth=0.73, relheight=0.38)

vec_label = tk.Label(master=vector_frame, text="Vector")
org_label = tk.Label(master=vector_frame, text="Origin")
vec_label.place(relx=0.02, rely=0.075, relheight=0.03, relwidth=0.1)
org_label.place(relx=0.13, rely=0.075, relheight=0.03, relwidth=0.1)

x_entry = tk.Entry(master=vector_frame, justify="center", font="Helvetica 15")
y_entry = tk.Entry(master=vector_frame, justify="center", font="Helvetica 15")
z_entry = tk.Entry(master=vector_frame, justify="center", font="Helvetica 15")
x_entry.place(relx=0.02, relwidth=0.1, rely=0.115, relheight=0.08)
y_entry.place(relx=0.02, relwidth=0.1, rely=0.205, relheight=0.08)
z_entry.place(relx=0.02, relwidth=0.1, rely=0.295, relheight=0.08)

x_org = tk.Entry(master=vector_frame, justify="center", font="Helvetica 15")
y_org = tk.Entry(master=vector_frame, justify="center", font="Helvetica 15")
z_org = tk.Entry(master=vector_frame, justify="center", font="Helvetica 15")
x_org.place(relx=0.13, relwidth=0.1, rely=0.115, relheight=0.08)
y_org.place(relx=0.13, relwidth=0.1, rely=0.205, relheight=0.08)
z_org.place(relx=0.13, relwidth=0.1, rely=0.295, relheight=0.08)

enter_button = tk.Button(master=vector_frame, text="Enter", font="Helvetica 13", command=print("enter"))
enter_button.place(relx=0.02, relwidth=0.212, relheight=0.07, rely=0.385)

# create settings_frame
settings_frame = tk.Frame(master=Mainframe, bg=frame_bg)
settings_frame.place(relx=0.0175, relwidth=0.315, rely=0.75, relheight=0.22)

button_2d = tk.Button(master=settings_frame, text="2D", bg=button_bg, font="Helvetica 20",
                      command=lambda: plot_frame.create_graph2d([0, 5], [0, 4]))
button_3d = tk.Button(master=settings_frame, text="3D", bg=button_bg, font="Helvetica 20",
                      command=lambda: plot_frame.create_graph3d([2, 4], [1, 7], [0, 4]))
button_2d.place(relx=0.025, relwidth=0.4625, rely=0.05, relheight=0.35)
button_3d.place(relx=0.5125, relwidth=0.4625, rely=0.05, relheight=0.35)

reset_button = tk.Button(master=settings_frame, text="Reset", bg=button_bg, font="Helvetica 10", command=print("reset"))
reset_button.place(relx=0.025, relwidth=0.95, rely=0.45, relheight=0.23)

quit_button = tk.Button(master=settings_frame, text="Quit", bg=button_bg, font="Helvetica 10", command=root.quit)
quit_button.place(rely=0.73, relheight=0.23, relx=0.025, relwidth=0.95)

# create action_frame
action_frame = tk.Frame(master=Mainframe, bg=frame_bg)
action_frame.place(rely=0.75, relheight=0.22, relx=0.35, relwidth=0.632)

tk.mainloop()
