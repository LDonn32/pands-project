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
