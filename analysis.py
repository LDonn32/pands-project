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


# 1.Outputs a summary of each variable to a single text file'

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


# 2. Outputs a histogram of each variable to a single png file

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

# 3. Outputs a scatter plot of each pair of variables. 


# Use plt.get_cmap to create a colormap.
# See: https://matplotlib.org/stable/tutorials/colors/colormaps.html
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_cmap.html
# This will create a colormap with 3 colours to match the 3 species in the dataset.
colourmap = plt.get_cmap('viridis', 3)

# Create the figure with 1 row x 2 columns.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# For the 1st Plot, Sepal Length vs Sepal Width.

# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html
axes[0].scatter(df['sepal length (cm)'], df['sepal width (cm)'], c=target_classes, cmap=colourmap, edgecolor='black')

# Set the x-axis label.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html
axes[0].set_xlabel('Sepal Length (cm)', fontsize=16)

# Set the y-axis label.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html
axes[0].set_ylabel('Sepal Width (cm)', fontsize=16)

# Set the title.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html
axes[0].set_title('Sepal Length vs Sepal Width', fontsize=18)

# The 2nd plot, Petal Length vs Petal Width.

# Repeat the above steps for the 2nd plot.
axes[1].scatter(df['petal length (cm)'], df['petal width (cm)'], c=target_classes, cmap=colourmap, edgecolor='black')
axes[1].set_xlabel('Petal Length (cm)', fontsize=16)
axes[1].set_ylabel('Petal Width (cm)', fontsize=16)
axes[1].set_title('Petal Length vs Petal Width', fontsize=18)
 
# Custom legend using Line2D.
# Colourmap will set the colours of the data in the legend. 
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markeredgecolor

legend_elements = [ Line2D([0], [0], marker='o', color='w',label='setosa', markerfacecolor=colourmap(0 / 2), markersize=16),
    Line2D([0], [0], marker='o', color='w',label='versicolor', markerfacecolor=colourmap(1 / 2), markersize=16),
    Line2D([0], [0], marker='o', color='w', label='virginica', markerfacecolor=colourmap(2 / 2), markersize=16)]

# Add the legend below the plots.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.legend.html
fig.legend(handles=legend_elements, title="Species", loc='lower center',bbox_to_anchor=(0.5, -0.05), ncol=3, fontsize=16)

# prevent overlap.
plt.tight_layout(rect=[0, 0.05, 1, 1])

# Save the scatterplot as a png.
plt.savefig('iris_scatterplot.png', bbox_inches='tight')
plt.show()





# 4.Performs any other analysis you think is appropriate. 

# Linear regression on the scatter plot of Sepal Length vs Sepal Width and Petal Length vs Petal Width.
# R² value for the regression line.

# Replicate the scatter plot with linear regression and R² value.
# Create a colormap with 3 colours for the 3 species
colourmap = plt.get_cmap('viridis', 3)

# Create the figure with 1 row x 2 columns. Seting a big figure size.
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Store sepal lenght as a varriable called x.
X = df['sepal length (cm)']

# Store sepal width as a varriable called y.
Y = df['sepal width (cm)']

# 1st scatter plot for Sepal Length vs Sepal Width.
axes[0].scatter(X, Y, c=target_classes, cmap=colourmap, edgecolor='black')

# Fit a regression line for Sepal Length vs Sepal Width using numpy.polyfit.
# See: https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html
slope, intercept = np.polyfit(X, Y, 1)

# Calculate the slope, m, and intercept ,b, for the line using numpy polyfit.
# np.polyfit will fit a straight line of 1 degree to x and y.
# Slope is how steep the line will be.
# Intercept is where the line will cross y.
Y_pred = slope * X + intercept

# Calculate R² using sklearn. 
# This will show how the regression line fits the data.
# See: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html
r2 = r2_score(Y, Y_pred)

# Plot regression line.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html
axes[0].plot(X, Y_pred, color='red', lw=2)

# Axis labels and title with R².
axes[0].set_xlabel('Sepal Length (cm)', fontsize=16)
axes[0].set_ylabel('Sepal Width (cm)', fontsize=16)

# Set the title with R² value.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html
# See: https://matplotlib.org/stable/tutorials/text/text_intro.html
axes[0].set_title(f'Sepal Length vs Sepal Width (R² = {r2:.2f})', fontsize=18)

# Repeat the above steps for the 2nd plot, Petal Length vs Petal Width.

# Store petal lenght as a varriable called x.
X = df['petal length (cm)']
# Store petal width as a varriable called y.
Y = df['petal width (cm)']

# Create scatter plot
axes[1].scatter(X, Y, c=target_classes, cmap=colourmap, edgecolor='black')

# # Fit a regression line for Petal Length vs Petal Width using numpy.polyfit.
slope, intercept = np.polyfit(X, Y, 1)

# Calculate the slope, m, and intercept, b, for the line using numpy polyfit.
Y_pred = slope * X + intercept

# Calculate R² using sklearn.
r2 = r2_score(Y, Y_pred)

# Plot regression line.
axes[1].plot(X, Y_pred, color='red', lw=2)

# Axis labels and title with R²
axes[1].set_xlabel('Petal Length (cm)', fontsize=16)
axes[1].set_ylabel('Petal Width (cm)', fontsize=16)

# Set the title with R² using f-string to format the it to 2 decimal places. 
# See: https://docs.python.org/3/library/string.html#format-specification-mini-language:~:text=Format%20examples%C2%B6,%27%7B%3A03.2f%7D%27.
axes[1].set_title(f'Petal Length vs Petal Width (R² = {r2:.2f})', fontsize=18)

# Set the Legend.
legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='setosa', markerfacecolor=colourmap(0 / 2), markersize=16),
    Line2D([0], [0], marker='o', color='w', label='versicolor', markerfacecolor=colourmap(1 / 2), markersize=16),
    Line2D([0], [0], marker='o', color='w', label='virginica', markerfacecolor=colourmap(2 / 2), markersize=16)
]

# Add the legend below the plots.
fig.legend(handles=legend_elements, title="Species", loc='lower center', bbox_to_anchor=(0.5, -0.05), ncol=3, fontsize=16)

# Adjust layout and prevent overlap
plt.tight_layout(rect=[0, 0.05, 1, 1])

# Save the figure as a png.
plt.savefig('iris_scatterplot_with_linear_regression_and_R2.png')

plt.show()

# 4.Performs any other analysis you think is appropriate. 
#  Outputs a boxplot of each variable by species to a single png file.

# Load the dataset.
# See: https://seaborn.pydata.org/generated/seaborn.load_dataset.html.
# This will load the iris dataset from seaborn's built-in datasets.
iris = sns.load_dataset("iris")

# Define the features to plot.
# See: https://seaborn.pydata.org/tutorial/axis_grids.html

features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

# Create the figure.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
# Setting the figure size to 15x10 inches.
# This will be a good size for showing the four subplots.

plt.figure(figsize=(15, 10))

# Manually create subplots for each feature.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html
# Using a 2x2 grid of subplots.
# Use seaborn's boxplot function to create the boxplots as I like the colours in them.
# See: https://seaborn.pydata.org/tutorial/axis_grids.html
# See: https://seaborn.pydata.org/tutorial/boxplot.html

# Each subplot will generate a boxplot of the feature against the species.

# The first subplot generates the sepal length for each species.

# Using the Colourblind palette to make it more accessible.
# See: https://seaborn.pydata.org/tutorial/color_palettes.html

plt.subplot(2, 2, 1)
sns.boxplot(data=iris, x='species', y=features[0], hue="species", palette="colorblind")
plt.title(f'{features[0].replace("_", " ").title()} by Species')

# The second subplot generates the sepal width for each species.

plt.subplot(2, 2, 2)
sns.boxplot(data=iris, x='species', y=features[1],hue="species", palette="colorblind")

plt.title(f'{features[1].replace("_", " ").title()} by Species')

# The third subplot generates the petal length for each species.

plt.subplot(2, 2, 3)
sns.boxplot(data=iris, x='species', y=features[2], hue="species", palette="colorblind")
plt.title(f'{features[2].replace("_", " ").title()} by Species')

# The fourth subplot generates the petal width for each species.

plt.subplot(2, 2, 4)
sns.boxplot(data=iris, x='species', y=features[3], hue="species", palette="colorblind")	
plt.title(f'{features[3].replace("_", " ").title()} by Species')

# Adjust the layout to prevent overlap.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html
# This will make sure the subplots are nice and tidy and not going to interfere with each other.

plt.tight_layout()

plt.savefig('iris_boxplots.png')

# Show the boxplots.

plt.show()


# 4.Performs any other analysis you think is appropriate. 

# Outputs a heatmap of the correlation matrix to a single png file.

# Using the corr() function to calculate correlations between columns in the DF. 
# See: https://www.geeksforgeeks.org/python-pandas-dataframe-corr/
corr_matrix = df.corr()

# Set the figure size.
plt.figure(figsize=(12, 8))  

# Create the heatmap using the imshow() function.
# See: https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html
# See: https://matplotlib.org/stable/tutorials/colors/colormaps.html
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html

plt.imshow(corr_matrix, cmap='viridis', interpolation='none')  

# Add a color bar.
plt.colorbar()  

# Set the x axis ticks.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html
plt.xticks(np.arange(len(corr_matrix.columns)), corr_matrix.columns, rotation=45)

# Set the y-axis ticks.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html
plt.yticks(np.arange(len(corr_matrix.columns)), corr_matrix.columns)

# Set a title and show.
plt.title('Heatmap of Correlation Matrix for Iris Dataset')

# Adjust layout for better spacing.
# See: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html
plt.tight_layout()  

plt.savefig('iris_heatmap.png')

# Show the heatmap.
plt.show()



# 4.Performs any other analysis you think is appropriate. 
# Outputs a pairplot of the dataset to a single png file.

# I am going to load the iris dataset for seaborn.
# See: https://seaborn.pydata.org/generated/seaborn.load_dataset.html
df = sns.load_dataset("iris")

# Create the pair plot. 
# I set the colour palette as one that is colorblind-friendly.
sns.pairplot(df, hue="species", palette="colorblind")

plt.savefig("iris_pairplot")

plt.show()

# 4.Performs any other analysis you think is appropriate. 
# Outputs a violin plot of the dataset to a indivdual png file.

# Create a violin plot to show the distribution of petal length by species.
# See: https://seaborn.pydata.org/tutorial/violinplots.html
sns.violinplot(data=iris, x="species", y="petal_length",hue="species", palette="colorblind")
plt.title("Distribution of Petal Length by Species")
plt.savefig("iris_violinplot_petal_length.png")
plt.show()

# Create a violin plot to show the distribution of petal length by species.
# See: https://seaborn.pydata.org/tutorial/violinplots.html
sns.violinplot(data=iris, x="species", y="petal_width",hue="species", palette="colorblind")
plt.title("Distribution of Petal Length by Species")
plt.savefig("iris_violinplot_petal_width.png")
plt.show()

# Create a violin plot to show the distribution of petal length by species.
# See: https://seaborn.pydata.org/tutorial/violinplots.html
sns.violinplot(data=iris, x="species", y="sepal_length", hue="species", palette="colorblind")
plt.title("Distribution of Petal Length by Species")
plt.savefig("iris_violinplot_sepal_length.png")
plt.show()

# Create a violin plot to show the distribution of petal length by species.
# See: https://seaborn.pydata.org/tutorial/violinplots.html
sns.violinplot(data=iris, x="species", y="sepal_width", hue="species", palette="colorblind")
plt.title("Distribution of Petal Length by Species")
plt.savefig("iris_violinplot_sepal_width.png")
plt.show()