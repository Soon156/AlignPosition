import tkinter as tk
import win32con
import win32gui
from PIL import Image, ImageTk


def overlayNotification():
    root = tk.Tk()
    root['bg'] = 'grey'  # Make window transparent
    root.overrideredirect(True)  # Hide title bar
    root.attributes('-transparentcolor', 'grey')  # Make grey transparent
    root.attributes('-topmost', True)  # Always on top
    root.attributes('-alpha', 0.9)

    win_width = int(root.winfo_screenwidth() / 5)
    win_height = int(root.winfo_screenheight() / 5)

    root.geometry(f'{win_width}x{win_height}+0+0')  # set window size
    # Create a photo image object of the image in the path
    image1 = Image.open("./Resources/logo.ico").resize((100, 100))
    icon_image = ImageTk.PhotoImage(image1)
    label = tk.Label(image=icon_image, bg='grey')
    # Position image
    label.place(x=0, y=-20, anchor='nw')
    root.mainloop()
