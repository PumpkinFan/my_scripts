import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector

# Step 2: Event handler function to capture the selected region
def onselect(eclick, erelease):
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    xmin, xmax = min(x1, x2), max(x1, x2)
    ymin, ymax = min(y1, y2), max(y1, y2)

    # Step 3: Process the selected portion and generate the updated image data
    updated_image_data = original_image_data.copy()
    updated_image_data[int(ymin):int(ymax), int(xmin):int(xmax)] = 255  # Example processing (setting selected region to white)

    # Step 4: Update the displayed image using imshow with the new image data
    im.set_array(updated_image_data)
    plt.draw()

# Step 1: Set up the figure and axes with the original image using imshow
original_image_data = np.random.randint(0, 256, (100, 100))  # Replace this with your actual image data
fig, ax = plt.subplots()
im = ax.imshow(original_image_data, cmap='gray')

# Connect the event handler to the figure
rs = RectangleSelector(ax, onselect, drawtype='box', useblit=True, button=[1], minspanx=5, minspany=5, spancoords='pixels')

plt.show()
