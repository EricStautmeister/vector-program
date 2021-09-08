import tkinter as tk


class LoadingScreen:
    loader = tk.Tk()
    destroy_counter = 4

    def countdown(self, time):
        if time == -1:
            self.loader.destroy()
        else:
            self.loader.after(1000, self.countdown, time - 1)

    def __init__(self):
        # cosmetics and colors
        self.loader.image = tk.PhotoImage(file='icon.png')
        self.label = tk.Label(self.loader, image=self.loader.image, bg='white')
        self.loader.overrideredirect(True)
        self.loader.geometry("+250+250")
        self.loader.lift()
        self.loader.wm_attributes("-topmost", True)
        self.loader.wm_attributes("-transparentcolor", "white")
        self.label.pack()

        # gui arrangement
        self.loader.update_idletasks()
        x = (self.loader.winfo_screenwidth() -
             self.loader.winfo_reqwidth()) / 2
        y = (self.loader.winfo_screenheight() -
             self.loader.winfo_reqheight()) / 2
        self.loader.geometry("+%d+%d" % (x, y))
        self.countdown(self.destroy_counter)


if __name__ == "__main__":
    load_screen = LoadingScreen()
    load_screen.loader.mainloop()
