import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_var.get()
    use_upper = upper_var.get()
    use_digits = digit_var.get()
    use_symbols = symbol_var.get()

    if length <= 0:
        messagebox.showwarning("Invalid Length", "Password length must be greater than 0")
        return

    chars = list(string.ascii_lowercase)
    if use_upper:
        chars += list(string.ascii_uppercase)
    if use_digits:
        chars += list(string.digits)
    if use_symbols:
        chars += list("!@#$%^&*()-_=+[]{};:,.<>?")

    if not chars:
        messagebox.showwarning("No Character Set", "Please select at least one character set")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Variables
length_var = tk.IntVar(value=12)
upper_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

# Title
tk.Label(root, text="Password Generator", font=("Arial", 18)).pack(pady=10)

# Options
frame_options = tk.Frame(root)
frame_options.pack(pady=5)

tk.Label(frame_options, text="Length:").grid(row=0, column=0, padx=5)
tk.Spinbox(frame_options, from_=4, to=64, textvariable=length_var, width=5).grid(row=0, column=1)

tk.Checkbutton(frame_options, text="Include Uppercase", variable=upper_var).grid(row=1, column=0, columnspan=2, sticky="w")
tk.Checkbutton(frame_options, text="Include Numbers", variable=digit_var).grid(row=2, column=0, columnspan=2, sticky="w")
tk.Checkbutton(frame_options, text="Include Symbols", variable=symbol_var).grid(row=3, column=0, columnspan=2, sticky="w")

# Password Display
password_entry = tk.Entry(root, font=("Arial", 16), justify="center")
password_entry.pack(pady=10, ipadx=20, ipady=5)

# Buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

tk.Button(frame_buttons, text="Generate", font=("Arial", 12), command=generate_password).pack(side="left", padx=10)
tk.Button(frame_buttons, text="Copy", font=("Arial", 12), command=copy_to_clipboard).pack(side="left", padx=10)

root.mainloop()
