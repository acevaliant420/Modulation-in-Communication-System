import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def plot_64qam_modulation():
    # Clear the previous plots
    ax_64qam.clear()

    # Define the 64-QAM constellation points
    constellation_points = {
        (0, 0): -7 - 7j,
        (0, 1): -7 - 5j,
        (0, 2): -7 - 1j,
        (0, 3): -7 - 3j,
        (0, 4): -7 + 7j,
        (0, 5): -7 + 5j,
        (0, 6): -7 + 1j,
        (0, 7): -7 + 3j,
        (1, 0): -5 - 7j,
        (1, 1): -5 - 5j,
        (1, 2): -5 - 1j,
        (1, 3): -5 - 3j,
        (1, 4): -5 + 7j,
        (1, 5): -5 + 5j,
        (1, 6): -5 + 1j,
        (1, 7): -5 + 3j,
        (2, 0): -1 - 7j,
        (2, 1): -1 - 5j,
        (2, 2): -1 - 1j,
        (2, 3): -1 - 3j,
        (2, 4): -1 + 7j,
        (2, 5): -1 + 5j,
        (2, 6): -1 + 1j,
        (2, 7): -1 + 3j,
        (3, 0): -3 - 7j,
        (3, 1): -3 - 5j,
        (3, 2): -3 - 1j,
        (3, 3): -3 - 3j,
        (3, 4): -3 + 7j,
        (3, 5): -3 + 5j,
        (3, 6): -3 + 1j,
        (3, 7): -3 + 3j,
        (4, 0): 7 - 7j,
        (4, 1): 7 - 5j,
        (4, 2): 7 - 1j,
        (4, 3): 7 - 3j,
        (4, 4): 7 + 7j,
        (4, 5): 7 + 5j,
        (4, 6): 7 + 1j,
        (4, 7): 7 + 3j,
        (5, 0): 5 - 7j,
        (5, 1): 5 - 5j,
        (5, 2): 5 - 1j,
        (5, 3): 5 - 3j,
        (5, 4): 5 + 7j,
        (5, 5): 5 + 5j,
        (5, 6): 5 + 1j,
        (5, 7): 5 + 3j,
        (6, 0): 1 - 7j,
        (6, 1): 1 - 5j,
        (6, 2): 1 - 1j,
        (6, 3): 1 - 3j,
        (6, 4): 1 + 7j,
        (6, 5): 1 + 5j,
        (6, 6): 1 + 1j,
        (6, 7): 1 + 3j,
        (7, 0): 3 - 7j,
        (7, 1): 3 - 5j,
        (7, 2): 3 - 1j,
        (7, 3): 3 - 3j,
        (7, 4): 3 + 7j,
        (7, 5): 3 + 5j,
        (7, 6): 3 + 1j,
        (7, 7): 3 + 3j
    }

    # Plot the 64-QAM constellation diagram
    for point, value in constellation_points.items():
        ax_64qam.plot(np.real(value), np.imag(value), 'bo')
        ax_64qam.annotate(f'{point}', (np.real(value), np.imag(value)), textcoords="offset points", xytext=(0,10), ha='center')

    # Set plot limits and labels
    ax_64qam.set_xlim([-8, 8])
    ax_64qam.set_ylim([-8, 8])
    ax_64qam.set_xlabel('In-phase')
    ax_64qam.set_ylabel('Quadrature')
    ax_64qam.set_title('64-QAM Constellation Diagram')

    # Update the plot
    canvas.draw()

# Create the Tkinter window
window = tk.Tk()
window.title("64-QAM Modulation")
window.geometry("1620x700")
window.minsize(1620, 700)
window.maxsize(1620, 700)

# Create Figure instance for 64-QAM constellation diagram
fig_64qam = plt.Figure(figsize=(4, 6), dpi=100)

# Add a subplot to the figure
ax_64qam = fig_64qam.add_subplot(111)

# Create Tkinter canvas for the figure
canvas = FigureCanvasTkAgg(fig_64qam, master=window)

# Position the canvas in the Tkinter window
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

# Create a button to plot the 64-QAM constellation diagram
plot_64qam_modulation()

# Start the Tkinter event loop
window.mainloop()
