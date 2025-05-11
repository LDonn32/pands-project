# Pands_Project 
# Author: Laura Donnelly

# Import libraries.

import sklearn as skl
from sklearn import datasets
from sklearn.metrics import r2_score
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.cm as cm
import numpy as np
import seaborn as sns

# Write a program called analysis.py that:  
# Outputs a summary of each variable to a single text file'

# Load the iris dataset. 
data = skl.datasets.load_iris()

# Create a DataFrame from the iris dataset.
# See: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
df = pd.DataFrame(data.data, columns=data.feature_names)

# Summerise the data set.
# See: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html
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

# Saves a histogram of each variable to png file

# Check how the names of the features appear in the dataset.
print(df.columns)

# Plot histograms for each feature.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html

fig, axes = plt.subplots(2, 2, figsize=(10, 8))  

# Plot each feature's histogram.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html

axes[0, 0].hist(df['sepal length (cm)'], bins=20, color='skyblue', edgecolor='black')

# Set the title.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html

axes[0, 0].set_title('Sepal Length (cm)')

# Set the x-axis. This is set to show the feature data.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html

axes[0, 0].set_xlabel('Sepal Length (cm)')

# Set the y-axis. his is set to show the the frequency of the feature's measurements.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html

axes[0, 0].set_ylabel('Frequency')

# Repeat the above steps for the remaining 3 features, changing colours of each histogram to distinguish them from each other.

axes[0, 1].hist(df['sepal width (cm)'], bins=20, color='pink', edgecolor='black')
axes[0, 1].set_title('Sepal Width (cm)')
axes[0, 1].set_xlabel('Sepal Width (cm)')
axes[0, 1].set_ylabel('Frequency')

axes[1, 0].hist(df['petal length (cm)'], bins=20, color='red', edgecolor='black')
axes[1, 0].set_title('Petal Length (cm)')
axes[1, 0].set_xlabel('Petal Length (cm)')
axes[1, 0].set_ylabel('Frequency')

axes[1, 1].hist(df['petal width (cm)'], bins=20, color='yellow', edgecolor='black')
axes[1, 1].set_title('Petal Width (cm)')
axes[1, 1].set_xlabel('Petal Width (cm)')
axes[1, 1].set_ylabel('Frequency')

# Adjust layout to prevent overlap
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html

plt.tight_layout()

# Save the histogram as a png.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
plt.savefig('Histogram_All_Features.png')

# Show the plots.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html

plt.show()
# I create a histogram for each of the features in the iris dataset but this time I save them as separate images. 
# I wont use subplots for this but instead create separate figures using the plt.figure() function.

# Histogram for Sepal Length.

# Create the figure.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
plt.figure(figsize=(12, 8))

# Create the histogram.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
plt.hist(df['sepal length (cm)'], bins=20, color='skyblue', edgecolor='black')

# Set the title.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html
plt.title('Sepal Length (cm)', fontsize=28)

# Set the x-axis label.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html
plt.xlabel('Sepal Length (cm)', fontsize=18)

# Set the y-axis label.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html
plt.ylabel('Frequency', fontsize=18)

# Set the font size for the ticks on the x and y axes.
# This is to make the font size bigger.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html
plt.xticks(fontsize=16)
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html
plt.yticks(fontsize=16)

# prevent overlap.
plt.tight_layout()
# Save the histogram as a png.
plt.savefig('hist_sepal_length.png')

plt.show()

# Repeat the above steps for the remaining 3 features, I change colours of each histogram to distinguish them.

# Sepal Width
plt.figure(figsize=(12, 8))
plt.hist(df['sepal width (cm)'], bins=20, color='pink', edgecolor='black')
plt.title('Sepal Width (cm)', fontsize=22)
plt.xlabel('Sepal Width (cm)', fontsize=18)
plt.ylabel('Frequency', fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.tight_layout()
plt.savefig('hist_sepal_width.png')
plt.show()

# Petal Length
plt.figure(figsize=(12, 8))
plt.hist(df['petal length (cm)'], bins=20, color='red', edgecolor='black')
plt.title('Petal Length (cm)', fontsize=22)
plt.xlabel('Petal Length (cm)', fontsize=18)
plt.ylabel('Frequency', fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.tight_layout()
plt.savefig('hist_petal_length.png')
plt.show()

# Petal Width
plt.figure(figsize=(12, 8))
plt.hist(df['petal width (cm)'], bins=20, color='yellow', edgecolor='black')
plt.title('Petal Width (cm)', fontsize=22)
plt.xlabel('Petal Width (cm)', fontsize=18)
plt.ylabel('Frequency', fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.tight_layout()
plt.savefig('hist_petal_width.png')
plt.show()


