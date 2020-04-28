"""
Generating a sine vs cosine curve

For this project, you will have a generate a sine vs cosine curve. 
You will need to use the numpy library to access the sine and cosine functions. 
You will also need to use the matplotlib library to draw the curve. 
To make this more difficult, make the graph go from -360° to 360°, 
with there being a 180° difference between each point on the x-axis.
"""

import matplotlib.pyplot as plt
import numpy as np

x_axis = np.linspace(-2*np.pi, 2*np.pi)
y_axis_sin = np.sin(x_axis/2)
y_axis_cos = np.cos(x_axis/2)

plt.plot(x_axis, y_axis_sin, color = 'purple', marker = "")
plt.plot(x_axis, y_axis_cos, color = 'yellow', marker = "")

plt.show()
