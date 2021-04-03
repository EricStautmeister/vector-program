import matplotlib.pyplot as plt
import tkinter as tk


class PltCanvas:

    def __init__(self, main):
        canvas = tk.Canvas(master=main)
        canvas.place(relx=0.35, rely=0.03, relheight=0.7, relwidth=0.632)
