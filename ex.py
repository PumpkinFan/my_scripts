import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Callback function for the custom button
def on_custom_button_clicked(event):
    print("Custom button clicked!")

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create the figure and axes
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y)

# Set the position and size of the custom button
button_ax = plt.axes([0.7, 0.01, 0.2, 0.05])  # [left, bottom, width, height]

# Create the custom button
custom_button = Button(button_ax, 'Custom Button')

# Attach the callback function to the custom button
custom_button.on_clicked(on_custom_button_clicked)

# Show the plot
plt.show()
