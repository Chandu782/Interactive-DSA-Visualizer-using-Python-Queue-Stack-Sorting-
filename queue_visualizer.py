import tkinter as tk

queue = []

def enqueue():
    value = entry.get()
    if value:
        queue.append(value)
        entry.delete(0, tk.END)
        update_queue()

def dequeue():
    if queue:
        queue.pop(0)
        update_queue()

def update_queue():
    queue_display.delete("1.0", tk.END)
    queue_display.insert(tk.END, "Front → ")
    for item in queue:
        queue_display.insert(tk.END, f"[{item}] ")
    queue_display.insert(tk.END, "← Rear")

# GUI Setup
root = tk.Tk()
root.title("Queue Visualizer")
root.geometry("600x200")
root.config(bg="lightblue")

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

tk.Button(root, text="Enqueue", font=("Arial", 12), command=enqueue).pack(pady=5)
tk.Button(root, text="Dequeue", font=("Arial", 12), command=dequeue).pack(pady=5)

queue_display = tk.Text(root, height=3, width=60, font=("Courier", 14))
queue_display.pack(pady=10)

root.mainloop()
