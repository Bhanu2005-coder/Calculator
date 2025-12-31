import tkinter as tk

def press(v):
    entry.insert(tk.END, v)

def clear():
    entry.delete(0, tk.END)

def calc():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("calculator")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

entry = tk.Entry(root, font=("Segoe UI", 20), bg="#2d2d2d", fg="black", bd=0, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10)

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

r, c = 1, 0
for b in buttons:
    cmd = calc if b == "=" else lambda x=b: press(x)
    tk.Button(root, text=b, command=cmd,
              font=("Segoe UI",14), width=5, height=2,
              bg="#3c3c3c", fg="white").grid(row=r, column=c, padx=5, pady=5)
    c += 1
    if c > 3:
        c = 0
        r += 1

# Clear button (red)
tk.Button(root, text="C", command=clear,
          font=("Segoe UI",14), width=22, height=2,
          bg="red", fg="white").grid(row=r+1, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
