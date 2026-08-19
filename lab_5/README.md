# Lab 5 - Visualization and Mini-EDA

## Overview

This lab focuses on exploring and visualizing the Titanic dataset using Python. 
The main objective is to perform a mini Exploratory Data Analysis (EDA) using different visualization techniques.

## Dataset

The dataset used in this lab is the Titanic `train.csv` dataset.

It contains information about passengers such as:

- Passenger ID
- Survival status
- Passenger class
- Name
- Gender
- Age
- Number of siblings/spouses
- Number of parents/children
- Ticket
- Fare
- Cabin
- Embarked port

## Objectives

The objectives of this lab are:

- Understand the structure of the dataset
- Identify missing values
- Analyze the distribution of passenger ages
- Identify potential outliers using boxplots
- Analyze passenger survival
- Compare survival across different groups
- Analyze fare distribution
- Understand relationships between numerical variables using correlation

## Visualizations

The following visualizations are included:

1. Age Distribution Histogram
2. Age Boxplot
3. Survival Count Plot
4. Survival by Gender
5. Survival by Passenger Class
6. Fare Distribution
7. Correlation Heatmap

## Key Findings

- Most passengers were between approximately 20 and 40 years old.
- The Age distribution is slightly right-skewed.
- The Age boxplot shows some potential high-age outliers.
- Age and Cabin contain a significant number of missing values.
- More passengers did not survive than survived.
- Female passengers had better survival outcomes than male passengers.
- First-class passengers generally had better survival outcomes.
- Fare distribution is strongly right-skewed.
- Correlation analysis helps identify relationships between numerical variables.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## Requirements

Install the required dependencies using:

```bash
pip install -r requirements.txt
