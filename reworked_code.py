import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class PltFrame:
    """Class for implementing matplotlib graph into tkinter"""

    def __init__(self, main):
        self.plot_frame = tk.Frame(master = main, bg = "#505255")
        self.plot_frame.place(relx = 0.35, rely = 0.03, relheight = 0.7, relwidth = 0.632)
        self.fig = plt.figure()
        self.plot_img = FigureCanvasTkAgg(self.fig, master = self.plot_frame)
        self.plot_img.get_tk_widget().place(relwidth = 1, relheight = 1)
        self.ax = None

    def create_graph2d(self, xs, ys):
        self.fig.clear()
        self.ax = self.fig.add_subplot()
        self.ax.plot(xs, ys)
        self.draw_plot()

    def create_graph3d(self, xs, ys, zs=None):
        if zs is None:
            zs = [0, 0]
        self.fig.clear()
        self.ax = self.fig.add_subplot(projection = "3d")
        self.ax.plot(xs, ys, zs)
        self.draw_plot()

    def draw_plot(self):
        self.plot_img.draw()


def pass_f():
    pass


class GUI(object):
    # CLASS VARIABLES
    bg = "#777777"
    canvas_bg = "#505255"
    frame_bg = "#B0B7C0"
    button_bg = "#ffffff"

    VECTORS3D = []
    VECTORS2D = []

    def __init__(self):
        self.root = tk.Tk()
        self.root.iconbitmap('icon.png')
        self.root.title("Vector Program")
        self.root.geometry("+250+2500")
        self.root.lift()  # MAIN WINDOW
        screen_height = self.root.winfo_screenheight()
        screen_width = self.root.winfo_screenwidth()
        height = screen_height / 1.1
        width = screen_width / 1.1
        x_cord = screen_width / 2 - width / 2
        y_cord = (screen_height - 80) / 2 - height / 2
        self.root.geometry("%dx%d+%d+%d" % (width, height, x_cord, y_cord))  # WINDOW SIZE
        self.Mainframe = tk.Frame(self.root, bg = self.bg)
        self.Mainframe.place(relheight = 1, relwidth = 1)  # MAINFRAME
        self.plot_frame = PltFrame(self.Mainframe)

        # FRAME AND LABEL ASSIGNMENT
        self.vector_frame = tk.Frame(master = self.Mainframe, bg = self.frame_bg)
        self.vector_name = tk.Label(master = self.vector_frame, text = "Vectors", font = "Helvetica 24")
        self.vector_list_win = tk.Label(master = self.vector_frame)
        self.vector_label = tk.Label(master = self.vector_frame, text = "Vector")
        self.origin_label = tk.Label(master = self.vector_frame, text = "Origin")
        self.settings_frame = tk.Frame(master = self.Mainframe, bg = self.frame_bg)
        self.action_frame = tk.Frame(master = self.Mainframe, bg = self.frame_bg)

        # FRAME AND LABEL PLACING
        self.vector_frame.place(relx = 0.0175, relwidth = 0.315, rely = 0.03, relheight = 0.7)
        self.vector_name.place(relx = 0.02, relwidth = 0.96, rely = 0.015, relheight = 0.05)
        self.vector_list_win.place(relx = 0.25, relwidth = 0.73, rely = 0.075, relheight = 0.38)
        self.vector_label.place(relx = 0.02, relwidth = 0.1, rely = 0.075, relheight = 0.03)
        self.origin_label.place(relx = 0.13, relwidth = 0.1, rely = 0.075, relheight = 0.03)
        self.settings_frame.place(relx = 0.0175, relwidth = 0.315, rely = 0.75, relheight = 0.22)
        self.action_frame.place(rely = 0.75, relheight = 0.22, relx = 0.35, relwidth = 0.632)

        # BUTTONS AND ENTRY ASSIGNMENTS
        self.x_entry = tk.Entry(master = self.vector_frame, justify = "center", font = "Helvetica 15")
        self.y_entry = tk.Entry(master = self.vector_frame, justify = "center", font = "Helvetica 15")
        self.z_entry = tk.Entry(master = self.vector_frame, justify = "center", font = "Helvetica 15")
        self.x_origin = tk.Entry(master = self.vector_frame, justify = "center", font = "Helvetica 15")
        self.y_origin = tk.Entry(master = self.vector_frame, justify = "center", font = "Helvetica 15")
        self.z_origin = tk.Entry(master = self.vector_frame, justify = "center", font = "Helvetica 15")
        self.enter_btn = tk.Button(master = self.vector_frame, text = "Enter", font = "Helvetica 13",
                                   command = self.add_vector)
        self.button_2d = tk.Button(master = self.settings_frame, text = "2D", bg = self.button_bg,
                                   font = "Helvetica 20",
                                   command = lambda: self.plot_frame.create_graph2d([0, 5], [0, 4]))
        self.button_3d = tk.Button(master = self.settings_frame, text = "3D", bg = self.button_bg,
                                   font = "Helvetica 20",
                                   command = lambda: self.plot_frame.create_graph3d([2, 4], [1, 7], [0, 4]))
        self.reset_button = tk.Button(master = self.settings_frame, text = "Reset", bg = self.button_bg,
                                      font = "Helvetica 10", command = pass_f)
        self.quit_button = tk.Button(master = self.settings_frame, text = "Quit", bg = self.button_bg,
                                     font = "Helvetica 10", command = self.root.quit)
        # BUTTONS AND ENTRY PLACING
        self.x_entry.place(relx = 0.02, relwidth = 0.1, rely = 0.115, relheight = 0.08)
        self.y_entry.place(relx = 0.02, relwidth = 0.1, rely = 0.205, relheight = 0.08)
        self.z_entry.place(relx = 0.02, relwidth = 0.1, rely = 0.295, relheight = 0.08)
        self.x_origin.place(relx = 0.13, relwidth = 0.1, rely = 0.115, relheight = 0.08)
        self.y_origin.place(relx = 0.13, relwidth = 0.1, rely = 0.205, relheight = 0.08)
        self.z_origin.place(relx = 0.13, relwidth = 0.1, rely = 0.295, relheight = 0.08)
        self.enter_btn.place(relx = 0.02, relwidth = 0.212, rely = 0.385, relheight = 0.07)
        self.button_2d.place(relx = 0.025, relwidth = 0.4625, rely = 0.05, relheight = 0.35)
        self.button_3d.place(relx = 0.5125, relwidth = 0.4625, rely = 0.05, relheight = 0.35)
        self.reset_button.place(relx = 0.025, relwidth = 0.95, rely = 0.45, relheight = 0.23)
        self.quit_button.place(rely = 0.73, relheight = 0.23, relx = 0.025, relwidth = 0.95)

    def get_values_from_input(self):
        try:
            x_v = int(self.x_entry.get())
            x_o = int(self.x_origin.get())
            y_v = int(self.y_entry.get())
            y_o = int(self.y_origin.get())
            try:
                z_v = int(self.z_entry.get())
                z_o = int(self.z_origin.get())
                values = [[x_v, x_o], [y_v, y_o], [z_v, z_o]]
                self.VECTORS3D.append(values)
            except ValueError:
                values = [[x_v, x_o], [y_v, y_o], [0, 0]]
                self.VECTORS2D.append(values)
        except x_v or x_o is None:
            print("No Values were given")

    def add_vector(self):
        vector = Vector()
        if True:
            GUI.VECTORS2D.append(vector)
            GUI.VECTORS3D.append(vector)
            self.x_entry.delete(0, "end")
            self.y_entry.delete(0, "end")
            self.z_entry.delete(0, "end")
            self.x_origin.delete(0, "end")
            self.y_origin.delete(0, "end")
            self.z_origin.delete(0, "end")
        else:
            pass

    def show_vectors(self):
        pass


gui = GUI()


class Vector:

    def __init__(self):
        self.data2D = gui.VECTORS2D
        self.data3D = gui.VECTORS3D
        self.sorted2D = [[self.data2D[0][1], self.data2D[0][1] + self.data2D[0][0]],
                       [self.data2D[1][1], self.data2D[1][1] + self.data2D[1][0]]]
        self.sorted = [[self.data3D[0][1], self.data3D[0][1] + self.data3D[0][0]],
                         [self.data3D[1][1], self.data3D[1][1] + self.data3D[1][0]],
                         [self.data3D[2][1], self.data3D[2][1] + self.data3D[2][0]]]
        gui.plot_frame.ax.plot(self.sorted[0], self.sorted[1], self.sorted[2])
        gui.plot_frame.draw_plot()


tk.mainloop()
