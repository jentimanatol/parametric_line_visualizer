import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import messagebox

def print_data():
    try:
        x0 = float(entry_x.get())
        y0 = float(entry_y.get())
        z0 = float(entry_z.get())
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "❌ Please enter valid numbers.")
        return

    x1, y1, z1 = x0 + a, y0 + b, z0 + c
    info = (
        f"📌 Given Point P = ({x0}, {y0}, {z0})\n"
        f"➡️ Direction Vector u = <{a}, {b}, {c}>\n"
        f"🟢 Point on Line (t = 1): ({x1}, {y1}, {z1})\n"
        f"🧮 Parametric Equations:\n"
        f"  x(t) = {x0} + {a}t\n"
        f"  y(t) = {y0} + {b}t\n"
        f"  z(t) = {z0} + {c}t"
    )
    messagebox.showinfo("Parametric Line Data", info)

def visualize_line():
    try:
        x0 = float(entry_x.get())
        y0 = float(entry_y.get())
        z0 = float(entry_z.get())
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "❌ Please enter valid numbers.")
        return

    t = np.linspace(-10, 10, 100)
    x = x0 + a * t
    y = y0 + b * t
    z = z0 + c * t
    x1, y1, z1 = x0 + a, y0 + b, z0 + c

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, label='🟦 Parametric Line', color='blue')
    ax.scatter([x0], [y0], [z0], color='red', s=100, label=f'🔴 Point P ({x0}, {y0}, {z0})')
    ax.scatter([x1], [y1], [z1], color='green', s=100, label=f'🟢 Point (t=1) ({x1}, {y1}, {z1})')
    ax.quiver(x0, y0, z0, a, b, c, length=3, color='purple', arrow_length_ratio=0.1,
              label=f'🟣 Direction Vector <{a}, {b}, {c}>')

    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title('📈 3D Parametric Line Visualization')
    ax.legend(loc='upper left')
    plt.tight_layout()
    plt.show()

# GUI
root = tk.Tk()
root.title("🎓 Parametric Line Visualizer")

# Instructions
description = (
    "📚 This app helps visualize a parametric line in 3D space.\n"
    "🔺 Enter a point and a direction vector.\n"
    "🧠 Click 'Print Data' to review parametric form.\n"
    "🎨 Click 'Visualize Line' to display the 3D graph."
)
tk.Label(root, text=description, wraplength=500, justify='left', fg='darkblue').grid(row=0, column=0, columnspan=4, pady=10)

# Input fields
tk.Label(root, text="🔺 Point on Line (x₀, y₀, z₀):").grid(row=1, column=0, sticky="w")
entry_x = tk.Entry(root, width=7); entry_x.grid(row=1, column=1)
entry_y = tk.Entry(root, width=7); entry_y.grid(row=1, column=2)
entry_z = tk.Entry(root, width=7); entry_z.grid(row=1, column=3)

tk.Label(root, text="➡️ Direction Vector (a, b, c):").grid(row=2, column=0, sticky="w")
entry_a = tk.Entry(root, width=7); entry_a.grid(row=2, column=1)
entry_b = tk.Entry(root, width=7); entry_b.grid(row=2, column=2)
entry_c = tk.Entry(root, width=7); entry_c.grid(row=2, column=3)

# Buttons
tk.Button(root, text="📄 Print Data", command=print_data, bg="lightyellow").grid(row=3, column=0, columnspan=2, pady=10)
tk.Button(root, text="🎨 Visualize Line", command=visualize_line, bg="lightgreen").grid(row=3, column=2, columnspan=2, pady=10)

# Footer
tk.Label(root, text="🧮 Created for Calculus 3 students | Parametric Line Helper", fg="gray").grid(row=4, column=0, columnspan=4, pady=10)

root.mainloop()
