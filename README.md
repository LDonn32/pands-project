# **pands-project**

Author: Laura Donnelly

## Contact Information:

Student ID: G00472977

Contact Email: G00472977@atu.ie

# Introduction:

This PANDS project will be looking at the well-known Iris data set.

This ReadMe file for the 2025 Programming and Scripting Module for the H. Dip in Science in Data Analytics, ATU will do the following:

*Give a description of the project objectives.

*State what technologies and libraries were used.

*Present additional information, comments and insights for code used in each of the tasks.

*Includes references and additional resources used.

## Repository Contents:

__$analysis.py$:__ Contains the code that will do the below:

- Outputs a summary of each variable to a single text file called 'summary.txt'
- Saves a histogram of of each variable to .png files:

hist_petal_length.png
hist_petal_width.png
hist_sepal_length.png
hist_sepal_width.png
Histogram_All_Features.png

- Outputs a scatter plot of each pair of variables to a .png files:

iris_scatterplot.png
iris_scatterplot_with_linear_regression_and_R2.png

Performs additional analysis to a .png files:

iris_boxplot.png
iris_heatmap.png
iris_violinplot_petal_length.png
iris_violinplot_petal_width.png
iris_violinplot_sepal_length.png
iris_violinplot_sepal_width.png

__analysis.ipynb:__ Jupyter Notebook that contains:

All assigned tasks for the project with;
Analysis on the datasets, 
Why certain graphs/methods were chosen and their limitations, 
Explanations for the code 
References are quoted in the notebook of when they were used.

__requirements.txt:__ List of the Python packages required to run the notebook. 

__.gitignore:__ Specifies files and directories to be ignored by Git.

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

## This section covers what technologies that were used: 

-Python
-Git
-GitHub
-Codespaces
-Jupyter

# Libraries / Packages used:

[Matplotlib](https://matplotlib.org/stable/)

[Numpy](https://numpy.org/doc/stable/index.html)

[Seaborn](https://seaborn.pydata.org/)

[Pandas](https://pandas.pydata.org/)

[SKLearn](https://scikit-learn.org/stable/index.html)

# Project Objectives:
1. Research the data set online and write a summary about it in your README. 
2. Download the data set and add it to your repository.
   
3. Write a program called analysis.py that:
   
1. Outputs a summary of each variable to a single text file, 
2. Saves a histogram of each variable to png files, and 
3. Outputs a scatter plot of each pair of variables. 
4. Performs any other analysis you think is appropriate.


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
Looking at mean in the Iris dataset, I can see the average measurement for each feature. So looking at a mean petal lenght of 3.758cm tells me that on average the 3 flower species are that lenght [www.geeksforgeeks.org](https://www.geeksforgeeks.org/mean-median-mode/.

__Minimum__
Looking at the minimum in the Iris dataset, I can see the lowest measurement. So looking at a minimum sepal width of 2.0 cm means at least one flower had a sepal that small [trycatchdebug.net](https://trycatchdebug.net/news/1160983/max-and-min-values-in-data-sets).

__Maximum__
In contrast to the minimum, the maximum will show me the highest measurement. I can see a max petal width of 2.5 cm which shows me the widest petal among all samples [trycatchdebug.net](https://trycatchdebug.net/news/1160983/max-and-min-values-in-data-sets).

__Standard Deviation__
Taking a look at the Standard deviation in the Iris dataset, I can see a higher standard deviation in sepal length which indicates a greater spread in sepel lenght across the dataset [www.geeksforgeeks.org](https://www.geeksforgeeks.org/standard-deviation-formula/).

__Median__
Looking at the Iris dataset, I can use the median to help me understand the central tendency of the species without being affected by outliers. Looking at the median sepal lenght at 5.8cm, I can see that is that’s the middle value across all samples [/www.geeksforgeeks.org](https://www.geeksforgeeks.org/mean-median-mode/#what-are-mean-median-and-mode).


## 2. _Saves a histogram of each variable to png files._ 
I have detailed analysis in the Jupyter notebook, but an additional comment I would like to make is that I seperated out the PNG files for this task. I have one PNG with all the variables in a subplot, then I have each variable saved to a PNG indivdually. I did this so that I could make the indivual ones really big and visable, for anyone reading the project with any visual impairments.


## 3. _Outputs a scatter plot of each pair of variables._ 
I have detailed analysis in the Jupyter notebook, but an additional comment I would like to make is that I selected viridis as it is a known colour blind friendly colour map [www.nceas.ucsb.edu/](https://www.nceas.ucsb.edu/sites/default/files/2022-06/Colorblind%20Safe%20Color%20Schemes.pdf).

## 4. Performs any other analysis you think is appropriate.
I performed analysis for the following:

_Using a Scatterplot:_
Linear regression 
Coeffiecent of Determination

_Using a Boxplot:_
Distrubution

_Using a Heatmap:_
Correlation Coefficients

_Using a Pairplot:_
Distrubition
KDE (Kernal Distrubition Estimation)

_Using a Violin Plot:_ 
Distrubition

## Conclusion:

__Summary of Analysis__

I applied various analysis techniques. Often times i used different methods to acheive the same information, such as using both a heatmap and a scatterplot to find the coeffiencent fo dermination (R2 Value). I did this to fully understand the dataset and to double check my findings against another method to see if I would get similar results. By doing so, I was able to draw confident conclusions to certain correlations between features. Overall, I was able to conclude that the there was a positive correlation between the petal lenght and yje petal width and a negative correlation between the sepal length and the sepal width. 


__Additional comments__

I found this project to be a great entry point for me to start my journey in understanding Python for data analysis. It's a great dataset to play around with, and try out different types of analysis with, as it is a decent size set.  The dataset is used around the world, so for a student there was no shortage of resoucres available on the dataset. I found this project to be a good excerise in practicing referencing as I go. I find the Jupyter Notebooks great for using markdown cells to slot in links of references as well as in the comments of the code cells. I find it easier this way, so that I do not forget to include any.

I wanted to ensure this project was accessable for anyone who has dylexia or colourblindness. My background is in Social Science and I currently work in adult education, and I wanted to ensure that this project wouldn't limit to anyone who was affected by this. Pretty much all of the defaults are Ariel, which is dylexia friendly [for reference](https://www.bdadyslexia.org.uk/advice/employers/creating-a-dyslexia-friendly-workplace/dyslexia-friendly-style-guide), so I didn't have to change the font types. I did increase the size and space everything out for readability.  I found Seaborn had built in colour blind friendly palattes. I also found that it was easy to change font sizes, so it made it the best package to use for this project for accessability of readers. 


## Key Rescourse Used: 

Below are resources used frequently for the tasks but they are referenced directly in the Jupyter Notebook. 

[Panda Documentation](https://pandas.pydata.org/docs/)

[Numpy Documentation](https://numpy.org/doc/)

[Matplotlib Documentation](https://matplotlib.org/stable/users/index.html)

[Seaborn Documentation](https://seaborn.pydata.org/)

[scikit-learn.org](https://scikit-learn.org/stable/index.html)

[Geeksforgeeks.org](https://www.geeksforgeeks.org/)

[W3schools.com](https://www.w3schools.com/)

I used [ChatGBT](https://chatgpt.com/)chatGBT for support and prompts were referenced in the Jupyter Notebook.


## Additional Resources used: 

[www.kaggle.com](https://www.kaggle.com/code/shrutimechlearn/step-by-step-pca-with-iris-dataset?scriptVersionId=11461313&cellId=7)

[Iris Dataset Archive UCI ]( https://archive.ics.uci.edu/datasets/)

## Additional Resources:

Useful template for creating this ReadMe file- [Github Best ReadMe Template](https://github.com/othneildrew/Best-README-Template/blob/main/README.md)

Useful to help format and use correct syntax for the ReadMe File, particularly for quoting code or references - [Githubdocs](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

Useful introduction to Python - [Python.org](https://docs.python.org/3/tutorial/introduction.html#)

Python CheatSheet (2025) - [Geeksforgeeks.org](https://www.geeksforgeeks.org/python-cheat-sheet/)

For this project I referred to [plotset.com](https://plotset.com/blog/making-data-visualizations-accessible) for making data visualisation accessible .

I refered to this rescource for colour blind friendly palattes [www.nceas.ucsb.edu]( https://www.nceas.ucsb.edu/sites/default/files/2022-06/Colorblind%20Safe%20Color%20Schemes.pdf).






