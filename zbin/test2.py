from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.garden.matplotlib import FigureCanvasKivy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.plot([1,2,3])
import numpy as np

class AmplitudeModulationApp(App):
    def build(self):
        # Main layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # User input labels and text inputs
        freq_label = Label(text='Carrier Frequency:')
        self.freq_input = TextInput(text='1000')

        phase_label = Label(text='Carrier Phase:')
        self.phase_input = TextInput(text='0')

        amp_label = Label(text='Carrier Amplitude:')
        self.amp_input = TextInput(text='1')

        # Button to trigger the plot
        plot_button = Button(text='Plot', size_hint=(1, 0.5))
        plot_button.bind(on_press=self.plot_amplitude_modulation)

        # Adding widgets to the layout
        layout.add_widget(freq_label)
        layout.add_widget(self.freq_input)
        layout.add_widget(phase_label)
        layout.add_widget(self.phase_input)
        layout.add_widget(amp_label)
        layout.add_widget(self.amp_input)
        layout.add_widget(plot_button)

        return layout

    def plot_amplitude_modulation(self, instance):
        # Retrieve user input values
        freq = float(self.freq_input.text)
        phase = float(self.phase_input.text)
        amp = float(self.amp_input.text)

        # Generate time vector
        t = np.linspace(0, 1, 1000)

        # Generate carrier signal
        carrier_signal = amp * np.cos(2 * np.pi * freq * t + np.radians(phase))

        # Generate message signal
        message_signal = np.sin(2 * np.pi * 2 * freq * t)

        # Perform amplitude modulation
        modulation_signal = carrier_signal * message_signal

        # Create figure and axes for plots
        fig, axs = plt.subplots(4, 1, figsize=(6, 10))

        # Plot carrier signal
        axs[0].plot(t, carrier_signal)
        axs[0].set_title('Carrier Signal')
        axs[0].set_xlabel('Time')
        axs[0].set_ylabel('Amplitude')

        # Plot message signal
        axs[1].plot(t, message_signal)
        axs[1].set_title('Message Signal')
        axs[1].set_xlabel('Time')
        axs[1].set_ylabel('Amplitude')

        # Plot modulation signal
        axs[2].plot(t, modulation_signal)
        axs[2].set_title('Modulation Signal')
        axs[2].set_xlabel('Time')
        axs[2].set_ylabel('Amplitude')

        # Plot amplitude modulation
        axs[3].plot(t, carrier_signal + modulation_signal)
        axs[3].set_title('Amplitude Modulation')
        axs[3].set_xlabel('Time')
        axs[3].set_ylabel('Amplitude')

        # Adjust subplot spacing
        plt.tight_layout()

        # Create a Kivy canvas widget for matplotlib figure
        canvas = FigureCanvasKivy(fig)

        # Clear the layout and add the canvas
        layout = self.root
        layout.clear_widgets()
        layout.add_widget(canvas)

if __name__ == '__main__':
    AmplitudeModulationApp().run()
