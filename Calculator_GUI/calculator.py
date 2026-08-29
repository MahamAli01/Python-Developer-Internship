import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

display = tk.Entry(window, font=("Arial", 20), justify="right")
display.pack(pady=20, padx=10, fill="x")

def button_click(value):
    display.insert(tk.END, value)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def clear():
    display.delete(0, tk.END)

button_frame = tk.Frame(window)
button_frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

for i, button in enumerate(buttons):
    row = i // 4
    column = i % 4


    if button == "=":
        command = calculate

    elif button == "C":
        command = clear
    else:
        command = lambda b=button: button_click(b)
    
    tk.Button(
    button_frame,
    text=button,
    width=5,
    height=2,
    command=command
).grid(row=row, column=column, padx=2, pady=2)


window.mainloop()