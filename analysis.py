# Pands_Project 

# Author: Laura Donnelly

# Import libraries.

# Import sklearn to load the datasets.
import sklearn as skl
from sklearn import datasets

# Import r2_score to calculate the r2.
from sklearn.metrics import r2_score

# import pandas.
import pandas as pd

# import matplotlib.pyplot to plot the data.
import matplotlib.pyplot as plt

# import Line2D to create a custom legend.	
from matplotlib.lines import Line2D

# import matplotlib.cm to create a colormap.
import matplotlib.cm as cm

#import numpy to create arrays.
import numpy as np

#import seaborn for data visulation.
import seaborn as sns



# Load the iris dataset.
# See: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html

# Load dataset. This command loads the iris data set and its features. 
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



# Pands_Project 
# Section 5 - Saves a histogram of each variable to png file
# Author: Laura Donnelly



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