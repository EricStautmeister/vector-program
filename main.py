import loading_screen
import merlin_main_code

loader = loading_screen.LoadingScreen()
trigger = True
while trigger is True:
    try:
        loader.loader.update_idletasks()
        loader.loader.update()
    except Exception:
       trigger = False

gui = merlin_main_code.GUI()
gui.root.lift()
gui.root.wm_attributes("-topmost", True)
gui.root.wm_attributes("-topmost", False)
gui.root.mainloop()
