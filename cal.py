import tkinter as tk
import math

# --- Button Click Logic ---
def click(event):
    btn_text = event.widget.cget("text")
    if btn_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif btn_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, btn_text)

# --- Scientific Function Logic ---
def sci_function(func_name):
    try:
        expr = entry.get()
        value = eval(expr)
        if func_name == "sin":
            result = math.sin(math.radians(value))
        elif func_name == "cos":
            result = math.cos(math.radians(value))
        elif func_name == "tan":
            result = math.tan(math.radians(value))
        elif func_name == "log":
            result = math.log10(value)
        elif func_name == "ln":
            result = math.log(value)
        elif func_name == "√":
            result = math.sqrt(value)
        elif func_name == "π":
            result = math.pi
        elif func_name == "e":
            result = math.e
        elif func_name == "^":
            entry.insert(tk.END, "")
            return
        else:
            result = "?"
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# --- GUI Setup ---
root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=15, pady=10)

# --- Buttons Layout ---
button_texts = [
    ["7", "8", "9", "/", "C"],
    ["4", "5", "6", "*", "("],
    ["1", "2", "3", "-", ")"],
    ["0", ".", "=", "+", "^"]
]

for i, row in enumerate(button_texts):
    for j, text in enumerate(row):
        btn = tk.Button(root, text=text, font="Arial 18", width=4, height=2)
        btn.grid(row=i+1, column=j, padx=5, pady=5)
        btn.bind("<Button-1>", click)

# --- Scientific Buttons ---
sci_buttons = [
    ("sin", 5, 0), ("cos", 5, 1), ("tan", 5, 2), ("log", 5, 3), ("ln", 5, 4),
    ("√", 6, 0), ("π", 6, 1), ("e", 6, 2)
]

for text, r, c in sci_buttons:
    sci_btn = tk.Button(root, text=text, font="Arial 16", width=4, height=2, command=lambda f=text: sci_function(f))
    sci_btn.grid(row=r, column=c, padx=5, pady=5)

root.mainloop()