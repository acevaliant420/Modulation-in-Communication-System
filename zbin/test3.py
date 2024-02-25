import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def plot_psk_modulation():
    # Get user input values
    carrier_frequency = float(carrier_frequency_entry.get())
    carrier_phase = float(carrier_phase_entry.get())
    carrier_amplitude = float(carrier_amplitude_entry.get())

    # Generate x values from 0 to 2*pi with a step of 0.1
    x = np.arange(0, 2 * np.pi, 0.1)

    # Calculate the carrier signal
    carrier_signal = carrier_amplitude * np.sin(carrier_frequency * x + carrier_phase)

    # Get the digital bit sequence from the user
    bit_sequence = bit_sequence_entry.get()

    # Convert bit sequence to digital wave (0s and 1s)
    digital_wave = np.array([int(bit) for bit in bit_sequence])

    # Generate the PSK modulated signal
    modulation_signal = carrier_amplitude * np.sin(carrier_frequency * x + carrier_phase * digital_wave)

    # Clear the previous plots
    ax_digital_wave.clear()
    ax_carrier.clear()
    ax_modulation.clear()

    # Plot the digital wave
    ax_digital_wave.step(x, digital_wave, where='post', label="Digital Bit Sequence")

    # Plot the carrier signal
    ax_carrier.plot(x, carrier_signal, label="Carrier Signal")

    # Plot the PSK modulated signal
    ax_modulation.plot(x, modulation_signal, label="PSK Modulated Signal")

    # Set legends and update the plots
    ax_digital_wave.legend()
    ax_carrier.legend()
    ax_modulation.legend()

    canvas_carrier.draw()
    canvas_digital_wave.draw()
    canvas_modulation.draw()


# Create the Tkinter window
window = tk.Tk()
window.title("Phase Shift Keying Modulation")
window.geometry("1620x700")
#window.minsize(1620, 700)
#window.maxsize(1620, 700)

message_frame = tk.Frame(window)
message_frame.pack(side=tk.LEFT)

# Create a label and entry field for the digital bit sequence
bit_sequence_label = tk.Label(message_frame, text="Digital Bit Sequence (0s and 1s):")
bit_sequence_label.pack()

bit_sequence_entry = tk.Entry(message_frame)
bit_sequence_entry.pack()

carrier_frame = tk.Frame(window)
carrier_frame.pack(side=tk.LEFT)

# Create labels and entry fields for user input for carrier signal
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

# Create Figure instances for digital wave, carrier signal, and modulation signal
fig_digital_wave = plt.figure(figsize=(4, 4), dpi=100)
fig_carrier = plt.figure(figsize=(4, 4), dpi=100)
fig_modulation = plt.figure(figsize=(4, 4), dpi=100)

# Add subplots to the figures
ax_digital_wave = fig_digital_wave.add_subplot(111)
ax_carrier = fig_carrier.add_subplot(111)
ax_modulation = fig_modulation.add_subplot(111)

# Create Tkinter canvas for each figure
canvas_digital_wave = FigureCanvasTkAgg(fig_digital_wave, master=message_frame)
canvas_digital_wave.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

canvas_carrier = FigureCanvasTkAgg(fig_carrier, master=carrier_frame)
canvas_carrier.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

canvas_modulation = FigureCanvasTkAgg(fig_modulation, master=window)
canvas_modulation.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create a button to plot the PSK modulation
plot_button = tk.Button(window, text="Plot", command=plot_psk_modulation)
plot_button.pack()

# Start the Tkinter event loop
window.mainloop()
