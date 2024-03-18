# plottask
# author: Sylvia Chapman Kent
# displays a histogram and plots a function on the same axes

import matplotlib # importing matplotlib and numpy so we can create the histrogram and plot the function

import matplotlib.pyplot as plt
import numpy as np

histogram_data = np.random.normal(loc= 5, scale= 2, size= 1000) # we want a normal distribution with 1000 values, a mean of 5 and a standard deviation of 2
x_points = np.array(range(0,10))
hx_points = x_points*x_points*x_points # function is h(x)=x^3, in other words x times x times x

plt.hist(histogram_data) # creates the histogram
plt.plot(x_points,hx_points) # plots the h(x) function
plt.show # displays the plot