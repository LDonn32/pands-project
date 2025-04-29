# Pands_Project 
# Section 4 - Outputs a summary of each variable to a single text file
# Author: Laura Donnelly



# import Pandas to load the datasets
import pandas as pd

# Import sklearn
import sklearn as skl

# Load dataset. This command loads the iris data set and its features. 
data = skl.datasets.load_iris()

# print
data

# load the iris dataset through Pandas CVS
df = pd.read_csv('https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv')

# Summerise the data set
df.describe()

# Store the results as a variable
summary = df.describe()

# Save the summary to a text file
summary_txt = summary.to_string()

# Define the path where the file will be saved
file_path = 'iris_summary.txt'

# Write the summary to the text file
with open(file_path, 'w') as f:
    f.write(summary_txt)

# Print
print(f"Summary saved to {file_path}")



# Pands_Project 
# Section 5 - Saves a histogram of each variable to png file
# Author: Laura Donnelly


import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
# Plot histograms for each feature.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html

fig, axes = plt.subplots(2, 2, figsize=(10, 8))  # Create a 2x2 grid of subplots

# Plot each feature's histogram.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html

axes[0, 0].hist(df['sepal_length'], bins=20, color='skyblue', edgecolor='blue')

# Set the title.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html

axes[0, 0].set_title('Sepal Length (cm)')

# Set the x-axis.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html

axes[0, 0].set_xlabel('Sepal Length (cm)')

# Set the y-axis.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html

axes[0, 0].set_ylabel('Frequency')

# Repeat the above steps for the remaining 3 features, changing colours of each histogram to distinguish them from each other.

axes[0, 1].hist(df['sepal_width'], bins=20, color='lightpink', edgecolor='purple')
axes[0, 1].set_title('Sepal Width (cm)')
axes[0, 1].set_xlabel('Sepal Width (cm)')
axes[0, 1].set_ylabel('Frequency')

axes[1, 0].hist(df['petal_length'], bins=20, color='coral', edgecolor='red')
axes[1, 0].set_title('Petal Length (cm)')
axes[1, 0].set_xlabel('Petal Length (cm)')
axes[1, 0].set_ylabel('Frequency')

axes[1, 1].hist(df['petal_width'], bins=20, color='lightgreen', edgecolor='green')
axes[1, 1].set_title('Petal Width (cm)')
axes[1, 1].set_xlabel('Petal Width (cm)')
axes[1, 1].set_ylabel('Frequency')



# Adjust layout to prevent overlap
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html

plt.tight_layout()


# Save the histogram as a png.
plt.savefig('Histogram.png')

# Show the plots
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html

plt.show()