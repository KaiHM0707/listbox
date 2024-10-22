import tkinter as tk
from tkinter import messagebox

def generate_table():
    try:
        number = int(entry.get())
        limit = int(radio_value.get())
        result_text.delete(1.0, tk.END)
        result = ""
        for i in range(limit + 1):
            result += f"{number} x {i} = {number * i}\n"
        result_text.insert(tk.END, result)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

scr = tk.Tk()
scr.title("Multiplication Table Generator")

label = tk.Label(scr, text="Enter a number:") 
label.pack(pady=10)

entry = tk.Entry(scr)
entry.pack(pady=10)

radio_value = tk.StringVar(value="10")
tk.Radiobutton(scr, text="10", variable=radio_value, value="10").pack()
tk.Radiobutton(scr, text="20", variable=radio_value, value="20").pack()
tk.Radiobutton(scr, text="30", variable=radio_value, value="30").pack()

button = tk.Button(scr, text="Generate Table", command=generate_table)
button.pack(pady=10)

result_text = tk.Text(scr, height=10, width=30)
result_text.pack(pady=10)

scr.mainloop()
