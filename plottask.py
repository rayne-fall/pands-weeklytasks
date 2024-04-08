# plottask
# author: Sylvia Chapman Kent
# displays a histogram and plots the function h(x)=x^3 on the same axes

# importing the modules we need to create the function and plots
import matplotlib.pyplot as plt
import numpy as np

histogram_data = np.random.normal(loc= 5, scale= 2, size= 1000) # we want a normal distribution with 1000 values, a mean of 5 and a standard deviation of 2
x_points = np.array(range(0,10)) # we want these points to have a range of 0-10
hx_points = x_points*x_points*x_points # function is h(x)=x^3, in other words x times x times x

plt.hist(histogram_data, label ='normal distribution') # creates the histogram
plt.plot(x_points,hx_points, label = 'h(x)=x^3', marker = 'o', linestyle = '-', color = 'hotpink') # plots the h(x) function with round markers on a solid pink line
plt.title("Weekly Task 8") # puts a title on the plot

# put labels on both axes
plt.xlabel("x values")
plt.ylabel("h(x) values")

plt.grid(ls=':') # displays a grid of dotted lines on the axes
plt.legend() # puts a legend on the plot
plt.show() # displays the plot

# References
# W3Schools page showing how to plot histograms in Matplotlib https://www.w3schools.com/python/matplotlib_histograms.asp
# W3Schools page showing how to plot functions in Matplotlib https://www.w3schools.com/python/matplotlib_plotting.asp
# W3Schools page showing how to put markers on each coordinate https://www.w3schools.com/python/matplotlib_markers.asp
# W3Schools page showing how to colour and and change the style of a line plot https://www.w3schools.com/python/matplotlib_line.asp
# W3Schools page showing how to put labels and a title on a plot https://www.w3schools.com/python/matplotlib_labels.asp
# W3Schools page showing how to put a grid on a plot https://www.w3schools.com/python/matplotlib_grid.asp
