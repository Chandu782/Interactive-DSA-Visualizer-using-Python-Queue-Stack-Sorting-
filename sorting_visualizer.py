import tkinter as tk
import random
import time

def draw_bars():
    canvas.delete("all")
    c_width = 500
    c_height = 300
    bar_width = c_width // len(data)

    for i, val in enumerate(data):
        x0 = i * bar_width
        y0 = c_height - val
        x1 = x0 + bar_width - 2
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill="skyblue")
        canvas.create_text(x0+15, y0-10, text=str(val), font=("Arial", 10))

def bubble_sort():
    for i in range(len(data)):
        for j in range(len(data)-1-i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                draw_bars()
                time.sleep(0.3)
                root.update()

def generate_data():
    global data
    data = [random.randint(10, 250) for _ in range(10)]
    draw_bars()

# GUI setup
root = tk.Tk()
root.title("Bubble Sort Visualizer")
root.geometry("600x400")

canvas = tk.Canvas(root, width=500, height=300)
canvas.pack()

tk.Button(root, text="Generate New Data", command=generate_data).pack(pady=5)
tk.Button(root, text="Start Bubble Sort", command=bubble_sort).pack(pady=5)

data = []
generate_data()

root.mainloop()
