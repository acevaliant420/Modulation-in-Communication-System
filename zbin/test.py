import tkinter as tk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_ask_modulation():
    # Get user input values
    carrier_frequency = float(carrier_frequency_entry.get())
    carrier_phase = float(carrier_phase_entry.get())
    carrier_amplitude = float(carrier_amplitude_entry.get())

    bit_sequence = bit_sequence_entry.get()

    # Generate x values from 0 to 2*pi with a step of 0.1
    x = np.arange(0, len(bit_sequence), 0.1)

    # Calculate the carrier signal
    carrier_signal = carrier_amplitude * np.sin(carrier_frequency * x + carrier_phase)

    # Create the digital bit sequence
    digital_bits = []
    for bit in bit_sequence:
        digital_bits.extend([int(bit)] * 10)  # Repeat each bit for 10 samples

    # ASK Modulation
    ask_modulated_signal = np.multiply(digital_bits, carrier_signal)

    # Clear the previous plots
    ax_carrier.clear()
    ax_digital_bits.clear()
    ax_ask_modulated.clear()

    # Plot the carrier signal
    ax_carrier.plot(x, carrier_signal, label="Carrier Signal")

    # Plot the digital bit sequence
    ax_digital_bits.step(x, digital_bits, where='post', label="Digital Bit Sequence")

    # Plot the ASK modulated signal
    ax_ask_modulated.plot(x, ask_modulated_signal, label="ASK Modulated Signal")

    # Set legends and update the plots
    ax_carrier.legend()
    ax_digital_bits.legend()
    ax_ask_modulated.legend()

    canvas_ask_modulated.draw()
    canvas_carrier.draw()
    canvas_digital_bits.draw()

# Create the Tkinter window
window = tk.Tk()
window.title("Amplitude Shift Keying (ASK) Modulation")
window.geometry("1620x700")
window.minsize(1620, 700)
window.maxsize(1620, 700)


carrier_frame = tk.Frame(window)
carrier_frame.pack(side=tk.LEFT)

# Create labels and entry fields for user input
carrier_frequency_label = tk.Label(carrier_frame, text="Carrier Frequency:")
carrier_frequency_label.pack()

carrier_frequency_entry = tk.Entry(carrier_frame)
carrier_frequency_entry.pack()

carrier_phase_label = tk.Label(carrier_frame, text="Carrier Phase:")
carrier_phase_label.pack()

carrier_phase_entry = tk.Entry(carrier_frame)
carrier_phase_entry.pack()

carrier_amplitude_label = tk.Label(carrier_frame, text="Carrier Amplitude:")
carrier_amplitude_label.pack()

carrier_amplitude_entry = tk.Entry(carrier_frame)
carrier_amplitude_entry.pack()

message_frame = tk.Frame(window)
message_frame.pack(side=tk.LEFT)

bit_sequence_label = tk.Label(message_frame, text="Digital Bit Sequence (0s and 1s):")
bit_sequence_label.pack()

bit_sequence_entry = tk.Entry(message_frame)
bit_sequence_entry.pack()

# Create Figure instances for carrier, digital bits, and ASK modulated signal
fig_carrier = Figure(figsize=(4, 4), dpi=100)
fig_digital_bits = Figure(figsize=(4, 4), dpi=100)
fig_ask_modulated = Figure(figsize=(4, 4), dpi=100)

# Add subplots to the figures
ax_carrier = fig_carrier.add_subplot(111)
ax_digital_bits = fig_digital_bits.add_subplot(111)
ax_ask_modulated = fig_ask_modulated.add_subplot(111)

# Create Tkinter canvas for each figure
canvas_carrier = FigureCanvasTkAgg(fig_carrier, master=carrier_frame)
canvas_carrier.get_tk_widget().pack()

canvas_digital_bits = FigureCanvasTkAgg(fig_digital_bits, master=message_frame)
canvas_digital_bits.get_tk_widget().pack()

canvas_ask_modulated = FigureCanvasTkAgg(fig_ask_modulated, master=window)
canvas_ask_modulated.get_tk_widget().pack()

# Create a button to plot the ASK modulation
plot_button = tk.Button(window, text="Plot", command=plot_ask_modulation)
plot_button.pack()

# Start the Tkinter event loop
tk.mainloop()
