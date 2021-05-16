import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt


def pass_placeholder():
    pass


class GUI:
    """class that holds the tkinter gui framework"""

    root = tk.Tk()
    root.withdraw()
    log = []
    for i in range(200):
        message = str("Log.message:" + str(i))
        log.append(message)

    def __init__(self):

        # cosmetics and colors
        self.root.iconbitmap('icon.ico')
        self.root.title("Vector Program")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bg = "#a4b0be"
        self.frame_bg = "#CDCDCD"
        self.button_bg = "#ffffff"

        # gui arrangement
        screen_height = self.root.winfo_screenheight()
        screen_width = self.root.winfo_screenwidth()
        height = screen_height / 1.1
        width = screen_width / 1.1
        x_cord = screen_width / 2 - width / 2
        y_cord = (screen_height - 80) / 2 - height / 2
        self.root.geometry("%dx%d+%d+%d" % (width, height, x_cord, y_cord))  # WINDOW SIZE

        # frames
        self.Mainframe = tk.Frame(self.root, bg = self.bg)
        self.vector_frame = tk.Frame(master = self.Mainframe, bg = self.frame_bg)
        self.settings_frame = tk.Frame(master = self.Mainframe, bg = self.frame_bg)
        self.action_frame = tk.Frame(master = self.Mainframe, bg = self.frame_bg)

        # frame placements
        self.Mainframe.place(relheight = 1, relwidth = 1)
        self.vector_frame.place(relx = 0.0175, relwidth = 0.315, rely = 0.03, relheight = 0.7)
        self.settings_frame.place(relx = 0.0175, relwidth = 0.315, rely = 0.75, relheight = 0.22)
        self.action_frame.place(rely = 0.75, relheight = 0.22, relx = 0.35, relwidth = 0.632)

        # functions class and vectors
        self.Vectors2d = []
        self.Vectors3d = []
        self.calc_modes_list = ["Mode List",
                                "1", "2", "3",
                                "4", "5", "6",
                                "7", "8", "9"]
        OPTIONS_VALUE = self.MODE_OPTION = tk.StringVar(self.vector_frame)
        OPTIONS_VALUE.set(self.calc_modes_list[0])
        self.function = ProgramControls(self.Mainframe, self.Vectors2d, self.Vectors3d)

        # VECTOR FRAME
        self.vector_name = tk.Label(master = self.vector_frame, text = "Vectors", font = "Helvetica 24")
        self.calc_mode = tk.OptionMenu(self.vector_frame, OPTIONS_VALUE, *self.calc_modes_list)
        self.calc_mode.configure(bg = "#ffffff")
        self.vector_list_win = tk.Label(master = self.vector_frame, anchor = "nw", font = "helvetica 14")
        self.origin_list_win = tk.Label(master = self.vector_frame, anchor = "nw", font = "helvetica 14")
        self.vector_label = tk.Label(master = self.vector_frame, text = "Vector")
        self.origin_label = tk.Label(master = self.vector_frame, text = "Origin")

        self.x_entry = tk.Entry(master = self.vector_frame, justify = "center", font = "Helvetica 15")
        self.y_entry = tk.Entry(master = self.vector_frame, justify = "center", font = "Helvetica 15")
        self.x_origin = tk.Entry(master = self.vector_frame, justify = "center", font = "Helvetica 15")
        self.y_origin = tk.Entry(master = self.vector_frame, justify = "center", font = "Helvetica 15")
        self.z_entry = None
        self.z_origin = None
        self.enter_btn = tk.Button(master = self.vector_frame, text = "Enter", font = "Helvetica 13",
                                   command = lambda: self.function.create_vector(self.x_entry, self.y_entry,
                                                                                 self.x_origin, self.y_origin,
                                                                                 self.z_entry, self.z_origin))
        self.vector_name.place(relx = 0.02, relwidth = 0.47, rely = 0.015, relheight = 0.05)
        self.calc_mode.place(relx = 0.51, relwidth = 0.47, rely = 0.015, relheight = 0.05)
        self.vector_list_win.place(relx = 0.25, relwidth = 0.365, rely = 0.075, relheight = 0.38)
        self.origin_list_win.place(relx = 0.615, relwidth = 0.365, rely = 0.075, relheight = 0.38)
        self.vector_label.place(relx = 0.02, relwidth = 0.1, rely = 0.075, relheight = 0.03)
        self.origin_label.place(relx = 0.13, relwidth = 0.1, rely = 0.075, relheight = 0.03)

        self.x_entry.place(relx = 0.02, relwidth = 0.1, rely = 0.115, relheight = 0.08)
        self.y_entry.place(relx = 0.02, relwidth = 0.1, rely = 0.205, relheight = 0.08)
        self.x_origin.place(relx = 0.13, relwidth = 0.1, rely = 0.115, relheight = 0.08)
        self.y_origin.place(relx = 0.13, relwidth = 0.1, rely = 0.205, relheight = 0.08)
        self.enter_btn.place(relx = 0.02, relwidth = 0.212, rely = 0.385, relheight = 0.07)

        # SETTINGS FRAME
        self.button_2d = tk.Button(master = self.settings_frame, text = "2D", bg = self.button_bg,
                                   font = "Helvetica 20", command = lambda: self.function.make_2d(self.remove_zs()))
        self.button_3d = tk.Button(master = self.settings_frame, text = "3D", bg = self.button_bg,
                                   font = "Helvetica 20", command = lambda: self.function.make_3d(self.make_zs()))
        self.log = tk.Button(master = self.settings_frame, text = "Log", bg = self.button_bg,
                             font = "Helvetica 20", command = self.function.make_log)
        self.place_holder = tk.Button(master = self.settings_frame, text = "Test", bg = self.button_bg,
                                      font = "Helvetica 20", command = lambda: pass_placeholder())
        self.reset_button = tk.Button(master = self.settings_frame, text = "Reset", bg = self.button_bg,
                                      font = "Helvetica 10", command = lambda: pass_placeholder())
        self.quit_button = tk.Button(master = self.settings_frame, text = "Quit", bg = self.button_bg,
                                     font = "Helvetica 10", command = self.root.quit)

        self.button_2d.place(relx = 0.025, relwidth = 0.21875, rely = 0.05, relheight = 0.35)
        self.button_3d.place(relx = 0.26875, relwidth = 0.21875, rely = 0.05, relheight = 0.35)
        self.log.place(relx = 0.5125, relwidth = 0.21875, rely = 0.05, relheight = 0.35)
        self.place_holder.place(relx = 0.75625, relwidth = 0.21875, rely = 0.05, relheight = 0.35)
        self.reset_button.place(relx = 0.025, relwidth = 0.95, rely = 0.45, relheight = 0.23)
        self.quit_button.place(rely = 0.73, relheight = 0.23, relx = 0.025, relwidth = 0.95)

        # Action Frame
        '''self.toolbar = NavigationToolbar2Tk(self.action_frame, PltFrame.plot_frame)
        self.toolbar.pack()'''
        self.x_axis_min = tk.Entry(master = self.action_frame, justify = "center", font = "Helvetica 15")
        self.x_axis_max = tk.Entry(master = self.action_frame, justify = "center", font = "Helvetica 15")
        self.y_axis_min = tk.Entry(master = self.action_frame, justify = "center", font = "Helvetica 15")
        self.y_axis_max = tk.Entry(master = self.action_frame, justify = "center", font = "Helvetica 15")

        self.x_axis_label = tk.Label(master = self.action_frame, text = "X axis min/max")
        self.y_axis_label = tk.Label(master = self.action_frame, text = "Y axis min/max")

        self.x_axis_label.place(relx = 0.025, relwidth = 0.15, rely = 0.05, relheight = 0.12)
        self.y_axis_label.place(relx = 0.2, relwidth = 0.15, rely = 0.05, relheight = 0.12)

        self.x_axis_min.place(relx = 0.025, relwidth = 0.070, rely = 0.22, relheight = 0.24)
        self.x_axis_max.place(relx = 0.105, relwidth = 0.070, rely = 0.22, relheight = 0.24)
        self.y_axis_min.place(relx = 0.2, relwidth = 0.070, rely = 0.22, relheight = 0.24)
        self.y_axis_max.place(relx = 0.28, relwidth = 0.070, rely = 0.22, relheight = 0.24)
        self.x_axis_min.insert(0, "x-")
        self.x_axis_max.insert(0, "x+")

        self.y_axis_min.insert(0, "y-")
        self.y_axis_max.insert(0, "y+")


        self.root.deiconify()

    def make_zs(self):
        if self.z_entry:
            return
        self.z_entry = tk.Entry(master = self.vector_frame, justify = "center", font = "Helvetica 15")
        self.z_origin = tk.Entry(master = self.vector_frame, justify = "center", font = "Helvetica 15")
        self.z_entry.place(relx = 0.02, relwidth = 0.1, rely = 0.295, relheight = 0.08)
        self.z_origin.place(relx = 0.13, relwidth = 0.1, rely = 0.295, relheight = 0.08)

    def remove_zs(self):
        try:
            self.z_entry.destroy()
            self.z_origin.destroy()
            self.z_entry = None
            self.z_origin = None
        except AttributeError:
            pass

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()




class ProgramControls:
    """Creates Functions to control functionalities"""

    def __init__(self, guiframe, Vectors2d, Vectors3d):
        self.dim = None
        self.data = None
        self.plot_data = None
        self.Vectors2d = Vectors2d
        self.Vectors3d = Vectors3d
        self.pltframe = PltFrame(guiframe)
        self.pltframe.plot_frame.place(relx = 0.35, rely = 0.03, relheight = 0.7, relwidth = 0.632)

    def make_2d(self, empty_var):
        self.dim = 2
        self.pltframe.create_graph2d()

    def make_3d(self, empty_var):
        self.dim = 3
        self.pltframe.create_graph3d()
    
    def make_log(self):
        self.pltframe.create_log_window()

    def get_values(self, x_entry, y_entry, x_origin, y_origin, z_entry, z_origin):
        # data
        x_v = int(x_entry.get())
        y_v = int(y_entry.get())
        x_o = x_origin.get()
        y_o = y_origin.get()
        try:
            z_v = int(z_entry.get())
            z_o = z_origin.get()
            z_entry.delete(0, "end")
            z_origin.delete(0, "end")
        except Exception:
            z_o = False
            z_v = 0
        x_entry.delete(0, "end")
        y_entry.delete(0, "end")
        x_origin.delete(0, "end")
        y_origin.delete(0, "end")
        if self.dim == 2:
            if x_o and y_o:
                return [[int(x_o), x_v], [int(y_o), y_v]]
            else:
                return [[0, x_v], [0, y_v]]
        else:
            if x_o and y_o and z_o:
                return [[int(x_o), x_v], [int(y_o), y_v], [int(z_o), z_v]]
            else:
                return [[0, x_v], [0, y_v], [0, z_v]]

    def create_vector(self, x_entry, y_entry, x_origin, y_origin, z_entry, z_origin, ):
        self.data = self.get_values(x_entry, y_entry, x_origin, y_origin, z_entry, z_origin)
        if self.dim == 2:
            self.plot_data = [[self.data[0][0], self.data[0][0] + self.data[0][1]],
                              [self.data[1][0], self.data[1][0] + self.data[1][1]]]
            self.Vectors2d.append(self.plot_data)
            self.pltframe.ax.plot(self.plot_data[0], self.plot_data[1])
        else:
            self.plot_data = [[self.data[0][0], self.data[0][0] + self.data[0][1]],
                              [self.data[1][0], self.data[1][0] + self.data[1][1]],
                              [self.data[2][0], self.data[2][0] + self.data[2][1]]]
            self.Vectors3d.append(self.plot_data)
            self.pltframe.ax.plot(self.plot_data[0], self.plot_data[1], self.plot_data[2])
        self.pltframe.draw_plot()


class PltFrame:
    """Class for implementing matplotlib graph into tkinter"""

    def __init__(self, main):
        self.plot_frame = tk.Frame(master = main, bg = "#505255")
        self.fig = plt.figure()
        self.plot_img = FigureCanvasTkAgg(self.fig, master = self.plot_frame)
        self.plot_img.get_tk_widget().place(relwidth = 1, relheight = 1)
        self.ax = None

    def create_graph2d(self):
        try:
            for widget in self.plot_frame.winfo_children():
                widget.destroy()
            self.fig = plt.figure()
            self.plot_img = FigureCanvasTkAgg(self.fig, master = self.plot_frame)
            self.plot_img.get_tk_widget().place(relwidth = 1, relheight = 1)
            self.ax = self.fig.add_subplot()
            self.draw_plot()
        except Exception:
            pass

    def create_graph3d(self):
        try:
            for widget in self.plot_frame.winfo_children():
                widget.destroy()
            self.fig = plt.figure()
            self.plot_img = FigureCanvasTkAgg(self.fig, master = self.plot_frame)
            self.plot_img.get_tk_widget().place(relwidth = 1, relheight = 1)
            self.ax = self.fig.add_subplot(projection = "3d")
            self.draw_plot()
        except Exception:
            pass

    def create_log_window(self):
        for widget in self.plot_frame.winfo_children():
            widget.destroy()
        scrollbar = tk.Scrollbar(self.plot_frame)
        scrollbar.pack(side = "right", fill = "both")
        # lbw = (round((self.plot_frame.winfo_reqwidth())/4))*2
        # lbh = round((self.plot_frame.winfo_reqheight() - 4) / 16)
        log = tk.Listbox(self.plot_frame, yscrollcommand = scrollbar.set)
        for message in GUI.log:
            log.insert("end", message)
        log.place(relheight = 1, relwidth = 1)
        scrollbar.config(command = log.yview)

    def draw_plot(self):
        self.plot_img.draw()


if __name__ == "__main__":
    gui = GUI()
    gui.root.mainloop()
