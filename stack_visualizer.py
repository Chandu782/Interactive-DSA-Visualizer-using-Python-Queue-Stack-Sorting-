import tkinter as tk

stack = []

def push():
    value = entry.get()
    if value:
        stack.append(value)
        entry.delete(0, tk.END)
        update_stack()

def pop():
    if stack:
        stack.pop()
        update_stack()

def update_stack():
    stack_display.delete("1.0", tk.END)
    for item in reversed(stack):
        stack_display.insert(tk.END, f"| {item} |\n")
    stack_display.insert(tk.END, " ‾‾‾‾‾ ")

# GUI setup
root = tk.Tk()
root.title("Stack Visualizer")
root.geometry("300x400")
root.config(bg="lightblue")

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

tk.Button(root, text="Push", font=("Arial", 12), command=push).pack(pady=5)
tk.Button(root, text="Pop", font=("Arial", 12), command=pop).pack(pady=5)

stack_display = tk.Text(root, height=15, width=20, font=("Courier", 14))
stack_display.pack(pady=20)

root.mainloop()
