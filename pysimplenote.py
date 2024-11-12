import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

# Initialize the main application window
root = tk.Tk()
root.title("Text Editor")
root.geometry("800x600")

# Dark Mode Colors
bg_color = "#2E2E2E"
fg_color = "#FFFFFF"
highlight_color = "#404040"

# Configure root background
root.configure(bg=bg_color)

# Function to create new file
def new_file():
    text_area.delete("1.0", tk.END)

# Function to open existing file
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, file.read())
        root.title(f"Text Editor - {file_path}")

# Function to save file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get("1.0", tk.END))
        root.title(f"Text Editor - {file_path}")

# Function to run Python script
def run_python():
    code = text_area.get("1.0", tk.END)
    try:
        output = subprocess.check_output(["python3", "-c", code], stderr=subprocess.STDOUT, text=True)
        messagebox.showinfo("Output", output)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", e.output)

# Function to run Bash script
def run_bash():
    code = text_area.get("1.0", tk.END)
    try:
        output = subprocess.check_output(["bash", "-c", code], stderr=subprocess.STDOUT, text=True)
        messagebox.showinfo("Output", output)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", e.output)

# Creating the menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0, bg=bg_color, fg=fg_color)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Run menu
run_menu = tk.Menu(menu_bar, tearoff=0, bg=bg_color, fg=fg_color)
menu_bar.add_cascade(label="Run", menu=run_menu)
run_menu.add_command(label="Run Python", command=run_python)
run_menu.add_command(label="Run Bash", command=run_bash)

# Text Area with Scrollbar
text_area = tk.Text(root, wrap="word", bg=bg_color, fg=fg_color, insertbackground=fg_color, undo=True)
text_area.pack(expand=True, fill="both")

# Scrollbar
scrollbar = tk.Scrollbar(text_area)
scrollbar.pack(side="right", fill="y")
text_area.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_area.yview)

# Start the application
root.mainloop()