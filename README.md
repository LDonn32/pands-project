# **pands-project**

Author: Laura Donnelly

# Introduction:

This PANDS project will be looking at the well-known Iris data set.

This ReadMe file for the 2025 Programming and Scripting Module for the H. Dip in Science in Data Analytics, ATU will do the following:

*Give a description of the project objectives.

*State what technologies and libraries were used.

*Give an outline of the project's progress. (Perhaps with an issue on github. Unsure if I am using this correctly as of yet but been playing around with one that I can link later if works ok)

*Present additional information, comments and insights for code used in each of the tasks.

*Includes references and additional resources used.


## Repository Contents:

analysis.ipynb: Jupyter Notebook that contains all assigned tasks for the project, explanations for the code and references.

analysis.py: Contains just the code that can be run the project.

** requirements.txt: List of the Python packages required to run the notebook. 

.gitignore: Specifies files and directories to be ignored by Git.

## Setup your own repository
Sign up for a free GitHub account.
Go to the repository page in your browser.
Click the green Code button.
Click the Codespaces tab.
Click Create new Codespace on main.

## Clone the Repository:
```
git clone https://github.com/LDonn32/pands-project.git
```

## Install Required Packages:
```
pip install -r requirements.txt
```

Please see [Github.com](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) for reference on cloning repository.

# Technologies used:

-Python
-Git
-GitHub
-Codespaces
-Jupyter

# Libraries / Packages used:

[opendyslexic.org](https://opendyslexic.org/).


# Project Objectives:
1. Research the data set online and write a summary about it in your README. 
2. Download the data set and add it to your repository.
   
3. Write a program called analysis.py that:
   
1. Outputs a summary of each variable to a single text file, 
2. Saves a histogram of each variable to png files, and 
3. Outputs a scatter plot of each pair of variables. 
4. Performs any other analysis you think is appropriate.


# Project outline:

1 (Optional) set up an issue to plan out project outline. 
2 Make sure to reference as I go, link the references with the code I am using.
3 Explain the code back to myself so that I fully understand whats going on in the code.
4 Write my text files in my voice
5 Work through the tasks one by one, then when completed, go back over the code and look for new ways to improve. 



# **Project Tasks**

## *1. Research the data set online and write a summary about it in your README.*

The data set can be found online on UC Irvine Machine Learning Website.
[archive.ics.uci.edu](https://archive.ics.uci.edu/dataset/53/iris)

More information I found helpful about the dataset on the Intuitive Machine Learning ToutTbe channel can be accessed via [YouTube](https://www.youtube.com/watch?v=5dLG3JDk2VU).

__Summary:__

The Iris dataset is one of the most popualr datasets used in statistics and machine learning. It was collected in 1936 by Statistician and Biologist Ronald Fisher. The purpose of the dataset is to classify the data based on its features.

The dataset contains fifty samples from three different types of Iris flowers; Iris setosa, Iris virginica and Iris versicolor. It has four features that are measured for each of the fifty samples. They are; the length and the width of the sepals and petals, in cms.

Fisher used the data from this data set to create a linear discriminant model to distinguish each species. Following on from this it became a widely used test dataset for many statistical classification techniques in machine learning.

## *2. Download the data set and add it to your repository.*

I downloaded the iris data set from [archive.ics.uci.edu](https://archive.ics.uci.edu/dataset/53/iris) onto my own machine. From there I uploaded it to the repository by utilising the add file button (left to the green code button) and uploading the file there. I used [docs.github.com](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository) for support here.

## 3. __Write a program called analysis.py that__: 

## 1. _Outputs a summary of each variable to a single text file_. 

I used df.describe() here as it gives me a quick summary of key statsitics, which I will go into further detail. Getting a summary gives me a good insight into the spread of the data and a good place to start to make comparrisions of the features. 

__Mean__
_"The mean, or arithmetic average, is calculated by summing all the values in a dataset and dividing by the total number of values. It’s sensitive to outliers and is commonly used when the data is symmetrically distributed."_ [www.geeksforgeeks.org](https://www.geeksforgeeks.org/mean-median-mode/).

Looking at mean in the Iris dataset, I can see the average measurement for each feature. So looking at a mean petal lenght of 3.758cm tells me that on average the 3 flower species are that lenght.

__Minimum__
_"The minimum value, also known as the min, is the lowest value in a data set. It is another crucial concept in data analysis as it provides information about the lower limit of a variable. The min value can be used to identify outliers, detect trends, and compare different data sets."_ [trycatchdebug.net](https://trycatchdebug.net/news/1160983/max-and-min-values-in-data-sets)

Looking at the minimum in the Iris dataset, I can see the lowest measurement. So looking at a minimum sepal width of 2.0 cm means at least one flower had a sepal that small.

__Maximum__
_"The maximum value, also known as the max, is the highest value in a data set. It is an essential concept in data analysis as it provides information about the upper limit of a variable. The max value can be used to identify outliers, detect trends, and compare different data sets."_ [trycatchdebug.net](https://trycatchdebug.net/news/1160983/max-and-min-values-in-data-sets)

In contrast to the minimum, the maximum will show me the highest measurement. I can see a max petal width of 2.5 cm which shows me the widest petal among all samples.

__Standard Deviation__
_"Standard deviation is a statistical measure that describes how much variation or dispersion there is in a set of data points. It helps us understand how spread out the values in a dataset are compared to the mean (average). A higher standard deviation means the data points are more spread out, while a lower standard deviation means they are closer to the mean."_ [www.geeksforgeeks.org](https://www.geeksforgeeks.org/standard-deviation-formula/)

Taking a look at the Standard deviation in the Iris dataset, I can see a higher standard deviation in sepal length which indicates a greater spread in sepel lenght across the dataset.

__Median__
_"The median is the middle value when the dataset is arranged in ascending or descending order. If there’s an even number of values, it’s the average of the two middle values. The median is robust to outliers and is often used when the data is skewed."_ [/www.geeksforgeeks.org](https://www.geeksforgeeks.org/mean-median-mode/#what-are-mean-median-and-mode)

Looking at the Iris dataset, I can use the median to help me understand the central tendency of the species without being affected by outliers. Looking at the median sepal lenght at 5.8cm, I can see that is that’s the middle value across all samples.


## 2. _Saves a histogram of each variable to png files._ 


## 3. _Outputs a scatter plot of each pair of variables._ 


## 4. _Performs any other analysis you think is appropriate._



## Additional comments for the project:

I wanted to ensure this project was accessable for anyone who has dylexia or colourblindness. My background is in social science and I currently work in adult education, and I wanted to ensure that this project wouldnt be limited to anyone who had either of these. I found seaborn had built in colour blind friendly palattes. I also found that it was compatiable with OpenDyslexic, so it made it the easiest package to use for this project for accessability of readers.


## Additional Resources:

For this project I used OpenDyslexic, a new open sourced font created to increase readability for readers with dyslexia, website link [opendyslexic.org](https://opendyslexic.org/).

Another resource used for making data visualisation accessible, [plotset.com](https://plotset.com/blog/making-data-visualizations-accessible).

I refered to this rescource for colour blind friendly palattes [www.nceas.ucsb.edu]( https://www.nceas.ucsb.edu/sites/default/files/2022-06/Colorblind%20Safe%20Color%20Schemes.pdf).

## Contact Information:

Student ID: G00472977

Contact Email: G00472977@atu.ie

