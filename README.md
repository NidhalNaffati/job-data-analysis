# Job Data Analysis

This repository contains a Jupyter Notebook for analyzing job data using Python and various libraries. The notebook covers several key steps in the data analysis process, including data scraping, cleaning, transformation, and clustering. Below, you'll find an overview of each section in the notebook.

## Table of Contents

1. [Prepare JSON Files](#prepare-json-files)
2. [Prepare DataFrames](#prepare-dataframes)
3. [Creating a Corpus](#creating-a-corpus)
4. [Remove Noise Function](#remove-noise-function)
5. [Creating tfidf_matrix](#creating-tfidf_matrix)
6. [Clustering with K-Means](#clustering-with-k-means)
7. [Visualizing Data](#visualizing-data)
8. [Creating a Spark Context and Reading the Data](#creating-a-spark-context-and-reading-the-data)
9. [Creating a Pipeline and Clustering Using K-Means Algorithm](#creating-a-pipeline-and-clustering-using-k-means-algorithm)

## 1. Prepare JSON Files

This section demonstrates how to scrape job data from websites using Scrapy. It provides Python code to define Scrapy spiders, run them, and save the scraped data in JSON format.

## 2. Prepare DataFrames

In this section, the notebook reads the previously created JSON files and attempts to create two Pandas DataFrames, 'df1' and 'df2'. It also includes a data cleaning function to clean the data. If the JSON files cannot be loaded, it provides an error message.

## 3. Creating a Corpus

This part of the notebook initializes an empty list to store job titles and iterates through the 'jobTitle' column of the DataFrames to create a corpus of job titles.

## 4. Remove Noise Function

Here, the notebook defines a function to remove noise from text data using the NLTK library. It removes non-alphanumeric characters, converts tokens to lowercase, and eliminates stopwords.

## 5. Creating tfidf_matrix

This section involves creating a TF-IDF matrix from the job title corpus. It uses the Scikit-Learn library's TfidfVectorizer to convert the text data into a numerical format for further analysis.

## 6. Clustering with K-Means

In this part, the notebook applies the K-Means clustering algorithm to cluster job titles based on their TF-IDF representations. It uses Scikit-Learn's KMeans class to create clusters and assigns cluster labels to job titles.

## 7. Visualizing Data

This section attempts to visualize the clustered job titles using PCA for dimensionality reduction and Matplotlib and Seaborn for plotting. It generates a scatterplot to visualize the data points in two dimensions.

## 8. Creating a Spark Context and Reading the Data

Here, the notebook utilizes PySpark to create a SparkContext and a SparkSession. It reads the JSON data from the previously created files ('jobs_1.json' and 'jobs_2.json') into Pandas DataFrames and then converts them into a PySpark DataFrame named 'jobs_dataFrame'.

## 9. Creating a Pipeline and Clustering Using K-Means Algorithm

In the final section, the notebook creates a data processing and modeling pipeline using PySpark's MLlib. It tokenizes the job titles, removes stopwords, calculates TF-IDF features, and applies the K-Means clustering algorithm. The results are displayed, and the first 25 rows are shown.

This Jupyter Notebook provides a comprehensive guide for scraping, cleaning, analyzing, and clustering job data using various Python libraries and tools. It is intended for educational purposes and can be used as a reference for similar data analysis tasks.
