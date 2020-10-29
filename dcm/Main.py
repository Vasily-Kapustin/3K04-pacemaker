# Entry point of application
from Gui import *
import tkinter as tk

# Starts gui loop
root = tk.Tk()
app = Application(master=root)

app.mainloop()
