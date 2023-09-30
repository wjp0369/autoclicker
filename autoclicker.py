import threading
import keyboard
import pyautogui
import tkinter as tk
from tkinter import ttk

# Global variable for hotkey and previous hotkey
hotkey = '`'
previous_hotkey = hotkey.lower()

def autoclicker():
    pyautogui.PAUSE = 0.1
    while True:
        if autoclicker_active:
            pyautogui.click(button='left')

def toggle_autoclicker():
    global autoclicker_active
    autoclicker_active = not autoclicker_active
    print(f'Autoclicker {"enabled" if autoclicker_active else "disabled"}')

def on_hotkey_press(event):
    hotkey_entry.delete(0, tk.END)
    hotkey_entry.insert(0, event.name)

def set_values():
    global hotkey, previous_hotkey
    new_hotkey = hotkey_entry.get().lower()
    keyboard.remove_hotkey(previous_hotkey)
    keyboard.add_hotkey(new_hotkey, toggle_autoclicker)
    previous_hotkey = new_hotkey  # Update previous hotkey
    hotkey = new_hotkey  # Update hotkey

def update_hotkey(event):
    global hotkey, previous_hotkey
    new_hotkey = event.widget.get().lower()
    keyboard.remove_hotkey(previous_hotkey)
    keyboard.add_hotkey(new_hotkey, toggle_autoclicker)
    previous_hotkey = new_hotkey  # Update previous hotkey
    hotkey = new_hotkey  # Update hotkey

try:
    # Default hotkey
    hotkey = hotkey.upper()
    previous_hotkey = hotkey.lower()

    # Global variable to keep track of autoclicker status
    autoclicker_active = False

    root = tk.Tk()
    root.title("AutoClick by wjp0369")
    root.iconbitmap("curs.ico")

    hotkey_label = ttk.Label(root, text="Hotkey:")
    hotkey_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    hotkey_entry = ttk.Entry(root)
    hotkey_entry.insert(0, hotkey)
    hotkey_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    hotkey_entry.bind("<Key>", on_hotkey_press)

    set_button = ttk.Button(root, text="Set", command=set_values)
    set_button.grid(row=1, column=2, padx=6, pady=5, sticky="w")

    hotkey_entry.bind("<FocusOut>", update_hotkey)

    keyboard.add_hotkey(hotkey.lower(), toggle_autoclicker)  # Convert to lowercase

    autoclicker_thread = threading.Thread(target=autoclicker)
    autoclicker_thread.daemon = True
    autoclicker_thread.start()

    root.mainloop()

except Exception as e:
    print(f"An error occurred: {e}")
