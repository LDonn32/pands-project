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

# Load Iris dataset
iris = load_iris()
data = iris.data
feature_names = iris.feature_names

# Plot and save histograms for each feature
for i, feature in enumerate(feature_names):
    # Create a new figure for each histogram
    plt.figure(figsize=(6, 4))
    
    # Plot the histogram for the current feature
    plt.hist(data[:, i], bins=20, color='pink', edgecolor='purple')
    
    # Add labels for x and y axes
    plt.xlabel(feature)
    plt.ylabel("Frequency")
    
    # Add a title
    plt.title(f"Histogram of {feature}")
    
    # Show
plt.show()
 
