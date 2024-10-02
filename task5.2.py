import tkinter as tk
from gpiozero import PWMLED
from time import sleep

# GPIO setup using gpiozero
# PWMLED allows control over LED brightness (0-100% intensity)
red_led = PWMLED(18)   # Red LED connected to GPIO pin 18
yellow_led = PWMLED(23)  # Yellow LED connected to GPIO pin 23
green_led = PWMLED(24)   # Green LED connected to GPIO pin 24

# Function to update LED intensities based on slider values
def update_intensities(event):
    # Get the slider values and convert them to a range between 0 and 1 for gpiozero
    redintensity = redslider.get() / 100.0  # Get red slider value and scale it (0-100) to (0-1)
    yellowintensity = yellowslider.get() / 100.0  # Same for yellow slider
    greenintensity = greenslider.get() / 100.0  # Same for green slider

    # Set the brightness of each LED based on slider values
    red_led.value = redintensity
    yellow_led.value = yellowintensity
    green_led.value = greenintensity

# GUI creation using tkinter
root = tk.Tk()  # Create the main window
root.title("LED Intensity Control")  # Set the window title
root.geometry("400x300")  # Set the window size

# Create a slider for controlling the red LED intensity
redslider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_intensities, label="Red")
redslider.pack(pady=10)  # Add some padding for spacing

# Create a slider for controlling the yellow LED intensity
yellowslider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_intensities, label="Yellow")
yellowslider.pack(pady=10)

# Create a slider for controlling the green LED intensity
greenslider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_intensities, label="Green")
greenslider.pack(pady=10)

# Create an exit button to close the GUI
exitbutton = tk.Button(root, text="Exit", command=root.quit)
exitbutton.pack(pady=20)

# Start the GUI event loop
root.mainloop()  # This keeps the window running and waits for user interactions