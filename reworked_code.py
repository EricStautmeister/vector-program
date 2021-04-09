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

    def create_graph2d(self):
        self.fig.clear()
        self.ax = self.fig.add_subplot()
        self.draw_plot()

    def create_graph3d(self, xs, ys, zs):
        self.fig.clear()
        self.ax = self.fig.add_subplot(projection = "3d")
        self.ax.plot(xs, ys, zs)
        self.draw_plot()

    def draw_plot(self):
        self.plot_img.draw()


class GUI(object):
    # CLASS VARIABLES
    bg = "#282c34"
    canvas_bg = "#505255"
    frame_bg = "#505255"
    button_bg = "#A9B6C9"

    VECTORS = []

    def __init__(self):
        self.root = tk.Tk()
        self.root.iconbitmap('wave-square-solid.ico')
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
        # self.dropdown = tk.OptionMenu(self.vector_frame, "name", "hi", "hello")
        self.vector_list_win = tk.Label(master = self.vector_frame, anchor = "nw", font = "helvetica 14")
        self.origin_list_win = tk.Label(master = self.vector_frame, anchor = "nw", font = "helvetica 14")
        self.vector_label = tk.Label(master = self.vector_frame, text = "Vector")
        self.origin_label = tk.Label(master = self.vector_frame, text = "Origin")
        self.settings_frame = tk.Frame(master = self.Mainframe, bg = self.frame_bg)
        self.action_frame = tk.Frame(master = self.Mainframe, bg = self.frame_bg)

        # FRAME AND LABEL PLACING
        self.vector_frame.place(relx = 0.0175, relwidth = 0.315, rely = 0.03, relheight = 0.7)
        self.vector_name.place(relx = 0.02, relwidth = 0.7, rely = 0.015, relheight = 0.05)
        # self.dropdown.place(relx = 0.73, relwidth = 0.24, rely = 0.015, relheight = 0.05)
        self.vector_list_win.place(relx = 0.25, relwidth = 0.365, rely = 0.075, relheight = 0.38)
        self.origin_list_win.place(relx = 0.615, relwidth = 0.365, rely = 0.075, relheight = 0.38)
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
                                   command = self.plot_frame.create_graph2d)
        self.button_3d = tk.Button(master = self.settings_frame, text = "3D", bg = self.button_bg,
                                   font = "Helvetica 20",
                                   command = lambda: self.plot_frame.create_graph3d([2, 4], [1, 7], [0, 4]))
        self.reset_button = tk.Button(master = self.settings_frame, text = "Reset", bg = self.button_bg,
                                      font = "Helvetica 10", command = self.show_vectors)
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
        x_v = int(self.x_entry.get())
        y_v = int(self.y_entry.get())
        z_v = int(self.z_entry.get())
        x_o = int(self.x_origin.get())
        y_o = int(self.y_origin.get())
        z_o = int(self.z_origin.get())

        values = [[x_v, x_o], [y_v, y_o], [z_v, z_o]]
        return values

    def add_vector(self):
        vector = Vector()
        GUI.VECTORS.append(vector)
        vector_label_give = "Vectors\n"
        origin_label_give = "Origins\n"
        for vec in GUI.VECTORS:
            vector_label_give += f"x: {vec.data[0][0]} y: {vec.data[1][0]} z: {vec.data[2][0]}\n"
        for org in GUI.VECTORS:
            origin_label_give += f"x: {org.data[0][1]} y: {org.data[1][1]} z: {org.data[2][1]}\n"
        self.vector_list_win.config(text=vector_label_give)
        self.origin_list_win.config(text=origin_label_give)
        self.x_entry.delete(0, "end")
        self.y_entry.delete(0, "end")
        self.z_entry.delete(0, "end")
        self.x_origin.delete(0, "end")
        self.y_origin.delete(0, "end")
        self.z_origin.delete(0, "end")

    def show_vectors(self):
        for vector in self.VECTORS:
            print(vector.data)


gui = GUI()


class Vector:

    def __init__(self):
        self.data = gui.get_values_from_input()
        self.sorted = [[self.data[0][1], self.data[0][1] + self.data[0][0]],
                       [self.data[1][1], self.data[1][1] + self.data[1][0]],
                       [self.data[2][1], self.data[2][1] + self.data[2][0]]]
        gui.plot_frame.ax.plot(self.sorted[0], self.sorted[1], self.sorted[2], color="green")
        gui.plot_frame.draw_plot()


tk.mainloop()
