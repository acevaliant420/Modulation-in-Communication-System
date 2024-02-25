import tkinter as tk
from customtkinter import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image

import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
def am_modulation():
    def plot_amplitude_modulation():
        # Get user input values
        carrier_frequency = float(carrier_frequency_entry.get())
        carrier_phase = float(carrier_phase_entry.get())
        carrier_amplitude = float(carrier_amplitude_entry.get())

        message_frequency = float(message_frequency_entry.get())
        message_phase = float(message_phase_entry.get())
        message_amplitude = float(message_amplitude_entry.get())

        modulation_index = float(modulation_index_entry.get())

        # Generate x values from 0 to 2*pi with a step of 0.1
        x = np.arange(0, 2 * np.pi, 0.1)

        # Calculate the carrier signal
        carrier_signal = carrier_amplitude * np.sin(carrier_frequency * x *6+ carrier_phase)

        # Calculate the message signal
        message_signal = message_amplitude * np.sin(message_frequency * x * 6 + message_phase)

        # Calculate the modulation signal (modulated carrier)
        modulation_signal = (1 + modulation_index * message_signal) * carrier_signal

        # Clear the previous plots
        ax_carrier.clear()
        ax_message.clear()
        ax_modulation.clear()

        # Plot the carrier signal
        ax_carrier.plot(x, carrier_signal, label="Carrier Signal")

        # Plot the message signal
        ax_message.plot(x, message_signal, label="Message Signal")

        # Plot the modulation signal
        ax_modulation.plot(x, modulation_signal, label="Modulation Signal")

        # Set legends and update the plots
        ax_carrier.legend()
        ax_message.legend()
        ax_modulation.legend()
        canvas_modulation.draw()
        canvas_message.draw()
        canvas_carrier.draw()

    # Create the Tkinter window
    window = tk.Tk()
    window.title("Amplitude Modulation Plot")
    window.geometry("1620x700")
    window.minsize(1620, 700)
    window.maxsize(1620, 700)



    # Create labels and entry fields for user input for carrier signal
    carrier_frame = tk.Frame(window)
    carrier_frame.pack(side=tk.LEFT)

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

    # Create labels and entry fields for user input for message signal
    message_frame = tk.Frame(window)
    message_frame.pack(side=tk.LEFT)

    message_frequency_label = tk.Label(message_frame, text="Message Frequency:")
    message_frequency_label.pack()

    message_frequency_entry = tk.Entry(message_frame)
    message_frequency_entry.pack()

    message_phase_label = tk.Label(message_frame, text="Message Phase:")
    message_phase_label.pack()

    message_phase_entry = tk.Entry(message_frame)
    message_phase_entry.pack()

    message_amplitude_label = tk.Label(message_frame, text="Message Amplitude:")
    message_amplitude_label.pack()

    message_amplitude_entry = tk.Entry(message_frame)
    message_amplitude_entry.pack()

    # Create a label and entry field for modulation index
    modulation_index_label = tk.Label(window, text="Modulation Index:")
    modulation_index_label.pack()

    modulation_index_entry = tk.Entry(window)
    modulation_index_entry.pack()

    # Create Figure instances for each signal
    fig_carrier = Figure(figsize=(4, 4), dpi=100)
    fig_message = Figure(figsize=(4, 4), dpi=100)
    fig_modulation = Figure(figsize=(4, 4), dpi=110)

    # Add subplots to the figures
    ax_carrier = fig_carrier.add_subplot(111)
    ax_message = fig_message.add_subplot(111)
    ax_modulation = fig_modulation.add_subplot(111)

    # Create Tkinter canvas for each figure
    canvas_carrier = FigureCanvasTkAgg(fig_carrier, master=carrier_frame)
    canvas_carrier.get_tk_widget().pack()

    canvas_message = FigureCanvasTkAgg(fig_message, master=message_frame)
    canvas_message.get_tk_widget().pack()

    canvas_modulation = FigureCanvasTkAgg(fig_modulation, master=window)
    canvas_modulation.get_tk_widget().pack()

    # Create a button to plot the amplitude modulation
    plot_button = tk.Button(window, text="Plot", command=plot_amplitude_modulation)
    plot_button.pack()

    # Start the Tkinter event loop
    tk.mainloop()


    # Create labels and entry fields for user input for carrier signal
    carrier_frame = tk.Frame(window)
    carrier_frame.pack(side=tk.LEFT)

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

    # Create labels and entry fields for user input for message signal
    message_frame = tk.Frame(window)
    message_frame.pack(side=tk.LEFT)

    message_frequency_label = tk.Label(message_frame, text="Message Frequency:")
    message_frequency_label.pack()

    message_frequency_entry = tk.Entry(message_frame)
    message_frequency_entry.pack()

    message_phase_label = tk.Label(message_frame, text="Message Phase:")
    message_phase_label.pack()

    message_phase_entry = tk.Entry(message_frame)
    message_phase_entry.pack()

    message_amplitude_label = tk.Label(message_frame, text="Message Amplitude:")
    message_amplitude_label.pack()

    message_amplitude_entry = tk.Entry(message_frame)
    message_amplitude_entry.pack()

    # Create a label and entry field for modulation index
    modulation_index_label = tk.Label(window, text="Modulation Index:")
    modulation_index_label.pack()

    modulation_index_entry = tk.Entry(window)
    modulation_index_entry.pack()

    # Create Figure instances for each signal
    fig_carrier = Figure(figsize=(4, 4), dpi=100)
    fig_message = Figure(figsize=(4, 4), dpi=100)
    fig_modulation = Figure(figsize=(4, 4), dpi=100)

    # Add subplots to the figures
    ax_carrier = fig_carrier.add_subplot(111)
    ax_message = fig_message.add_subplot(111)
    ax_modulation = fig_modulation.add_subplot(111)

    # Create Tkinter canvas for each figure
    canvas_carrier = FigureCanvasTkAgg(fig_carrier, master=carrier_frame)
    canvas_carrier.get_tk_widget().pack()

    canvas_message = FigureCanvasTkAgg(fig_message, master=message_frame)
    canvas_message.get_tk_widget().pack()

    canvas_modulation = FigureCanvasTkAgg(fig_modulation, master=window)
    canvas_modulation.get_tk_widget().pack()

    # Create a button to plot the amplitude modulation
    plot_button = tk.Button(window, text="Plot", command=plot_amplitude_modulation)
    plot_button.pack()

    # Start the Tkinter event loop
    tk.mainloop()
    print("BUTTON PRESSED")

def pm_modulation():
    def plot_phase_modulation():
        # Get user input values
        carrier_frequency = float(carrier_frequency_entry.get())
        carrier_phase = float(carrier_phase_entry.get())
        carrier_amplitude = float(carrier_amplitude_entry.get())

        message_frequency = float(message_frequency_entry.get())
        message_phase = float(message_phase_entry.get())
        message_amplitude = float(message_amplitude_entry.get())

        modulation_index = float(modulation_index_entry.get())

        # Generate x values from 0 to 2*pi with a step of 0.1
        x = np.arange(0, 2 * np.pi, 0.1)

        # Calculate the carrier signal
        carrier_signal = carrier_amplitude * np.sin(carrier_frequency * x * 6 + carrier_phase)

        # Calculate the message signal
        message_signal = message_amplitude * np.sin(message_frequency * x * 6 + message_phase)

        # Calculate the modulation signal (modulated carrier)
        modulation_signal = carrier_amplitude * np.sin(carrier_frequency * x*6  + modulation_index * message_signal)

        # Clear the previous plots
        ax_carrier.clear()
        ax_message.clear()
        ax_modulation.clear()

        # Plot the carrier signal
        ax_carrier.plot(x, carrier_signal, label="Carrier Signal")

        # Plot the message signal
        ax_message.plot(x, message_signal, label="Message Signal")

        # Plot the modulation signal
        ax_modulation.plot(x, modulation_signal, label="Modulation Signal")

        # Set legends and update the plots
        ax_carrier.legend()
        ax_message.legend()
        ax_modulation.legend()

        canvas_carrier.draw()
        canvas_message.draw()
        canvas_modulation.draw()


    # Create the Tkinter window
    window = tk.Tk()
    window.title("Phase Modulation Plot")
    window.geometry("1620x700")
    window.minsize(1620, 700)
    window.maxsize(1620, 700)

    # Create labels and entry fields for user input for carrier signal
    carrier_frame = tk.Frame(window)
    carrier_frame.pack(side=tk.LEFT)

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

    # Create labels and entry fields for user input for message signal
    message_frame = tk.Frame(window)
    message_frame.pack(side=tk.LEFT)

    message_frequency_label = tk.Label(message_frame, text="Message Frequency:")
    message_frequency_label.pack()

    message_frequency_entry = tk.Entry(message_frame)
    message_frequency_entry.pack()

    message_phase_label = tk.Label(message_frame, text="Message Phase:")
    message_phase_label.pack()

    message_phase_entry = tk.Entry(message_frame)
    message_phase_entry.pack()

    message_amplitude_label = tk.Label(message_frame, text="Message Amplitude:")
    message_amplitude_label.pack()

    message_amplitude_entry = tk.Entry(message_frame)
    message_amplitude_entry.pack()

    # Create a label and entry field for modulation index
    modulation_index_label = tk.Label(window, text="Modulation Index:")
    modulation_index_label.pack()

    modulation_index_entry = tk.Entry(window)
    modulation_index_entry.pack()

    # Create Figure instances for each signal
    fig_carrier = Figure(figsize=(4, 4), dpi=100)
    fig_message = Figure(figsize=(4, 4), dpi=100)
    fig_modulation = Figure(figsize=(4, 4), dpi=100)

    # Add subplots to the figures
    ax_carrier = fig_carrier.add_subplot(111)
    ax_message = fig_message.add_subplot(111)
    ax_modulation = fig_modulation.add_subplot(111)

    # Create Tkinter canvas for each figure
    canvas_carrier = FigureCanvasTkAgg(fig_carrier, master=carrier_frame)
    canvas_carrier.get_tk_widget().pack()

    canvas_message = FigureCanvasTkAgg(fig_message, master=message_frame)
    canvas_message.get_tk_widget().pack()

    canvas_modulation = FigureCanvasTkAgg(fig_modulation, master=window)
    canvas_modulation.get_tk_widget().pack()

    # Create a button to plot the phase modulation
    plot_button = tk.Button(window, text="Plot", command=plot_phase_modulation)
    plot_button.pack()

    # Start the Tkinter event loop
    tk.mainloop()

def fm_modulation():
    def plot_frequency_modulation():
        # Get user input values
        carrier_frequency = float(carrier_frequency_entry.get())
        carrier_phase = float(carrier_phase_entry.get())
        carrier_amplitude = float(carrier_amplitude_entry.get())

        message_frequency = float(message_frequency_entry.get())
        message_phase = float(message_phase_entry.get())
        message_amplitude = float(message_amplitude_entry.get())

        modulation_index = float(modulation_index_entry.get())

        # Generate x values from 0 to 2*pi with a step of 0.1
        x = np.arange(0, 2 * np.pi, 0.1)

        # Calculate the carrier signal
        carrier_signal = carrier_amplitude * np.sin(carrier_frequency * x * 6 + carrier_phase)

        # Calculate the message signal
        message_signal = message_amplitude * np.sin(message_frequency * x * 6 + message_phase)

        # Calculate the modulation signal (modulated carrier)
        modulation_signal = carrier_amplitude * np.cos(carrier_frequency * x *6 + modulation_index * np.sin(message_frequency * x*6) )

        # Clear the previous plots
        ax_carrier.clear()
        ax_message.clear()
        ax_modulation.clear()

        # Plot the carrier signal
        ax_carrier.plot(x, carrier_signal, label="Carrier Signal")

        # Plot the message signal
        ax_message.plot(x, message_signal, label="Message Signal")

        # Plot the modulation signal
        ax_modulation.plot(x, modulation_signal, label="Modulation Signal")

        # Set legends and update the plots
        ax_carrier.legend()
        ax_message.legend()
        ax_modulation.legend()

        canvas_carrier.draw()
        canvas_message.draw()
        canvas_modulation.draw()

    # Create the Tkinter window
    window = tk.Tk()
    window.title("Frequency Modulation Plot")
    window.geometry("1620x700")
    window.minsize(1620, 700)
    window.maxsize(1620, 700)

    # Create labels and entry fields for user input for carrier signal
    carrier_frame = tk.Frame(window)
    carrier_frame.pack(side=tk.LEFT)

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

    # Create labels and entry fields for user input for message signal
    message_frame = tk.Frame(window)
    message_frame.pack(side=tk.LEFT)

    message_frequency_label = tk.Label(message_frame, text="Message Frequency:")
    message_frequency_label.pack()

    message_frequency_entry = tk.Entry(message_frame)
    message_frequency_entry.pack()

    message_phase_label = tk.Label(message_frame, text="Message Phase:")
    message_phase_label.pack()

    message_phase_entry = tk.Entry(message_frame)
    message_phase_entry.pack()

    message_amplitude_label = tk.Label(message_frame, text="Message Amplitude:")
    message_amplitude_label.pack()

    message_amplitude_entry = tk.Entry(message_frame)
    message_amplitude_entry.pack()

    # Create a label and entry field for modulation index
    modulation_index_label = tk.Label(window, text="Modulation Index:")
    modulation_index_label.pack()

    modulation_index_entry = tk.Entry(window)
    modulation_index_entry.pack()

    # Create Figure instances for each signal
    fig_carrier = Figure(figsize=(4, 4), dpi=100)
    fig_message = Figure(figsize=(4, 4), dpi=100)
    fig_modulation = Figure(figsize=(4, 4), dpi=100)

    # Add subplots to the figures
    ax_carrier = fig_carrier.add_subplot(111)
    ax_message = fig_message.add_subplot(111)
    ax_modulation = fig_modulation.add_subplot(111)

    # Create Tkinter canvas for each figure
    canvas_carrier = FigureCanvasTkAgg(fig_carrier, master=carrier_frame)
    canvas_carrier.get_tk_widget().pack()

    canvas_message = FigureCanvasTkAgg(fig_message, master=message_frame)
    canvas_message.get_tk_widget().pack()

    canvas_modulation = FigureCanvasTkAgg(fig_modulation, master=window)
    canvas_modulation.get_tk_widget().pack()

    # Create a button to plot the frequency modulation
    plot_button = tk.Button(window, text="Plot", command=plot_frequency_modulation)
    plot_button.pack()

    # Start the Tkinter event loop
    tk.mainloop()

def ask_modulation():
    def plot_ask_modulation():
        # Get user input values
        carrier_frequency = float(carrier_frequency_entry.get())
        carrier_phase = float(carrier_phase_entry.get())
        carrier_amplitude = float(carrier_amplitude_entry.get())

        bit_sequence = bit_sequence_entry.get()

        # Generate x values from 0 to 2*pi with a step of 0.1
        x = np.arange(0, len(bit_sequence), 0.1)

        # Calculate the carrier signal
        carrier_signal = carrier_amplitude * np.sin(carrier_frequency * x * 6 + carrier_phase)

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

def psk_modulation():
    def plot_ask_modulation():
        # Get user input values
        carrier_frequency = float(carrier_frequency_entry.get())
        carrier_phase = float(carrier_phase_entry.get())
        carrier_amplitude = float(carrier_amplitude_entry.get())

        bit_sequence = bit_sequence_entry.get()

        # Generate x values from 0 to 2*pi with a step of 0.1
        x = np.arange(0, len(bit_sequence), 0.1)

        # Calculate the carrier signal
        carrier_signal = carrier_amplitude * np.sin(carrier_frequency * x * 6 + carrier_phase)

        # Create the digital bit sequence
        digital_bits = []

        for bit in bit_sequence:
            digital_bits.extend([int(bit)] * 10)  # Repeat each bit for 10 samples
        array = []
        array = digital_bits
        for i in range(0, len(array)):
            if(array[i]==0):
                array[i]=-1
        # ASK Modulation
        ask_modulated_signal = np.multiply( (0.5 * carrier_amplitude *carrier_amplitude * np.sin((carrier_frequency)*x * 6)), array)

        # Clear the previous plots
        ax_carrier.clear()
        ax_digital_bits.clear()
        ax_ask_modulated.clear()

        # Plot the carrier signal
        ax_carrier.plot(x, carrier_signal, label="Carrier Signal")

        # Plot the digital bit sequence
        ax_digital_bits.step(x, digital_bits, where='post', label="Digital Bit Sequence")

        # Plot the ASK modulated signal
        ax_ask_modulated.plot(x, ask_modulated_signal, label="PSK Modulated Signal")

        # Set legends and update the plots
        ax_carrier.legend()
        ax_digital_bits.legend()
        ax_ask_modulated.legend()

        canvas_ask_modulated.draw()
        canvas_carrier.draw()
        canvas_digital_bits.draw()

    # Create the Tkinter window
    window = tk.Tk()
    window.title("Phase Shift Keying (PSK) Modulation")
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

def fsk_modulation():
    def plot_ask_modulation():
        # Get user input values
        carrier_frequency = float(carrier_frequency_entry.get())
        carrier_phase = float(carrier_phase_entry.get())
        carrier_amplitude = float(carrier_amplitude_entry.get())

        bit_sequence = bit_sequence_entry.get()

        # Generate x values from 0 to 2*pi with a step of 0.1
        x = np.arange(0, len(bit_sequence), 0.1)

        # Calculate the carrier signal
        carrier_signal = carrier_amplitude * np.sin(carrier_frequency * x * 6 + carrier_phase)

        # Create the digital bit sequence
        digital_bits = []
        for bit in bit_sequence:
            digital_bits.extend([int(bit)] * 10)  # Repeat each bit for 10 samples

        # ASK Modulation
        ask_modulated_signal = np.sin(2 * np.pi * (np.add(carrier_frequency, digital_bits)) * x)

        # Clear the previous plots
        ax_carrier.clear()
        ax_digital_bits.clear()
        ax_ask_modulated.clear()

        # Plot the carrier signal
        ax_carrier.plot(x, carrier_signal, label="Carrier Signal")

        # Plot the digital bit sequence
        ax_digital_bits.step(x, digital_bits, where='post', label="Digital Bit Sequence")

        # Plot the ASK modulated signal
        ax_ask_modulated.plot(x, ask_modulated_signal, label="FSK Modulated Signal")

        # Set legends and update the plots
        ax_carrier.legend()
        ax_digital_bits.legend()
        ax_ask_modulated.legend()

        canvas_ask_modulated.draw()
        canvas_carrier.draw()
        canvas_digital_bits.draw()

    # Create the Tkinter window
    window = tk.Tk()
    window.title("Frequency Shift Keying (FSK) Modulation")
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

def fqam_modulation():
    def plot_4qam_modulation():
        # Clear the previous plots
        ax_4qam.clear()

        # Define the 4-QAM constellation points
        constellation_points = {
            (0, 0): -1 - 1j,
            (0, 1): -1 + 1j,
            (1, 0): 1 - 1j,
            (1, 1): 1 + 1j
        }

        # Plot the 4-QAM constellation diagram
        for point, value in constellation_points.items():
            ax_4qam.plot(np.real(value), np.imag(value), 'bo')
            ax_4qam.annotate(f'{point}', (np.real(value), np.imag(value)), textcoords="offset points", xytext=(0, 10),
                             ha='center')

        # Set plot limits and labels
        ax_4qam.set_xlim([-2, 2])
        ax_4qam.set_ylim([-2, 2])
        ax_4qam.set_xlabel('In-phase')
        ax_4qam.set_ylabel('Quadrature')
        ax_4qam.set_title('4-QAM Constellation Diagram')

        # Update the plot
        canvas.draw()

    # Create the Tkinter window
    window = tk.Tk()
    window.title("4-QAM Modulation")
    window.geometry("1620x700")
    window.minsize(1620, 700)
    window.maxsize(1620, 700)

    # Create Figure instance for 4-QAM constellation diagram
    fig_4qam = plt.Figure(figsize=(4, 6), dpi=100)

    # Add a subplot to the figure
    ax_4qam = fig_4qam.add_subplot(111)

    # Create Tkinter canvas for the figure
    canvas = FigureCanvasTkAgg(fig_4qam, master=window)

    # Position the canvas in the Tkinter window
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

    # Create a button to plot the 4-QAM constellation diagram
    plot_4qam_modulation()

    # Start the Tkinter event loop
    window.mainloop()

def sixteenqam_modulation():
    def plot_16qam_modulation():
        # Clear the previous plots
        ax_16qam.clear()

        # Define the 16-QAM constellation points
        constellation_points = {
            (0, 0): -3 - 3j,
            (0, 1): -3 - 1j,
            (0, 2): -3 + 3j,
            (0, 3): -3 + 1j,
            (1, 0): -1 - 3j,
            (1, 1): -1 - 1j,
            (1, 2): -1 + 3j,
            (1, 3): -1 + 1j,
            (2, 0): 3 - 3j,
            (2, 1): 3 - 1j,
            (2, 2): 3 + 3j,
            (2, 3): 3 + 1j,
            (3, 0): 1 - 3j,
            (3, 1): 1 - 1j,
            (3, 2): 1 + 3j,
            (3, 3): 1 + 1j
        }

        # Plot the 16-QAM constellation diagram
        for point, value in constellation_points.items():
            ax_16qam.plot(np.real(value), np.imag(value), 'bo')
            ax_16qam.annotate(f'{point}', (np.real(value), np.imag(value)), textcoords="offset points", xytext=(0, 10),
                              ha='center')

        # Set plot limits and labels
        ax_16qam.set_xlim([-4, 4])
        ax_16qam.set_ylim([-4, 4])
        ax_16qam.set_xlabel('In-phase')
        ax_16qam.set_ylabel('Quadrature')
        ax_16qam.set_title('16-QAM Constellation Diagram')

        # Update the plot
        canvas.draw()

    # Create the Tkinter window
    window = tk.Tk()
    window.title("16-QAM Modulation")
    window.geometry("1620x700")
    window.minsize(1620, 700)
    window.maxsize(1620, 700)

    # Create Figure instance for 16-QAM constellation diagram
    fig_16qam = plt.Figure(figsize=(4, 6), dpi=100)

    # Add a subplot to the figure
    ax_16qam = fig_16qam.add_subplot(111)

    # Create Tkinter canvas for the figure
    canvas = FigureCanvasTkAgg(fig_16qam, master=window)

    # Position the canvas in the Tkinter window
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

    # Create a button to plot the 16-QAM constellation diagram
    plot_16qam_modulation()

    # Start the Tkinter event loop
    window.mainloop()

def sixtyfourqam_modulation():
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
            ax_64qam.annotate(f'{point}', (np.real(value), np.imag(value)), textcoords="offset points", xytext=(0, 10),
                              ha='center')

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


window = CTk()
window.title("Modulation in a Communication System")
window.geometry("1200x675")

# Add image file
bg = tk.PhotoImage(file=resource_path("background.png"))
label = CTkLabel(window, image=bg, text="")
label.place(x=0, y=0)


set_appearance_mode("DARK")
window.maxsize(1200, 675)
window.minsize(1200, 675)

am_button = CTkButton(window, text="Amplitude Modulation", command=am_modulation, width=250, height=45, font=("Comic Sans", 20))
#am_button.grid(row=1, column=1, sticky="ew", padx=20, pady=20)
am_button.place(x=40, y=230)

pm_button = CTkButton(window, text="Phase Modulation", command=pm_modulation, width=250, height=45, font=("Comic Sans", 20))
#pm_button.grid(row=1, column=2, sticky="ew", padx=20, pady=20)
pm_button.place(x=40, y=330)

fm_button = CTkButton(window, text="Frequency Modulation", command=fm_modulation, width=250, height=45, font=("Comic Sans", 20))
#fm_button.grid(row=1, column=3, sticky="ew", padx=20, pady=20)
fm_button.place(x=40, y=430)


ask_button = CTkButton(window, text="Amplitude Shift Keying", command=ask_modulation, width=270, height=45, font=("Comic Sans", 20))
#ask_button.grid(row=2, column=1, sticky="ew", padx=20, pady=20)
ask_button.place(x=880, y=230)

psk_button = CTkButton(window, text="Phase Shift Keying", command=psk_modulation, width=270, height=45, font=("Comic Sans", 20))
#psk_button.grid(row=2, column=2, sticky="ew", padx=20, pady=20)
psk_button.place(x=880, y=330)

fsk_button = CTkButton(window, text="Frequency Shift Keying", command=fsk_modulation, width=270, height=45, font=("Comic Sans", 20))
#fsk_button.grid(row=2, column=3, sticky="ew", padx=20, pady=20)
fsk_button.place(x=880, y=430)

fqam_button = CTkButton(window, text="4 - Quadrature Amplitude Modulation", command=fqam_modulation, width=380, height=45, font=("Comic Sans", 20))
#fqam_button.grid(row=3, column=1, sticky="ew", padx=20, pady=20)
fqam_button.place(x=410, y=230)

sqam_button = CTkButton(window, text="16 - Quadrature Amplitude Modulation", command=sixteenqam_modulation, width=380, height=45, font=("Comic Sans", 20))
#sqam_button.grid(row=3, column=2, sticky="ew", padx=20, pady=20)
sqam_button.place(x=410, y=330)

iqam_button = CTkButton(window, text="64 - Quadrature Amplitude Modulation", command=sixtyfourqam_modulation, width=380, height=45, font=("Comic Sans", 20))
#iqam_button.grid(row=3, column=3, sticky="ew", padx=20, pady=20)
iqam_button.place(x=410, y=430)

window.mainloop()