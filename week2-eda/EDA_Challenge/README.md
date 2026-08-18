# Titanic Exploratory Data Analysis

## Overview

This project presents a complete Exploratory Data Analysis (EDA) of the Titanic passenger dataset.

The goal of this analysis is to take a raw and imperfect dataset, understand what information it contains, identify data-quality issues, clean the data appropriately, explore meaningful patterns, and communicate the most important findings clearly.

The analysis is designed from a data-science perspective, with particular attention to data quality, appropriate preprocessing, visualization, and potential modeling risks.

---

## Objective

The main objectives of this project are to:

- Understand the structure and contents of the dataset
- Profile the dataset before making any changes
- Identify missing values and data-quality issues
- Check column data types and duplicates
- Detect and evaluate potential outliers
- Clean the dataset using justified decisions
- Explore relationships between passenger characteristics and survival
- Create clear and labeled visualizations
- Extract three important and non-obvious insights
- Identify potential data-quality and target-leakage risks
- Provide an actionable summary of the findings

---

## Dataset

The dataset used in this project is the Titanic training dataset.

It contains information about passengers who were aboard the Titanic, along with whether or not they survived.

### Important Columns

| Column | Description |
|---|---|
| `PassengerId` | Unique identifier for each passenger |
| `Survived` | Survival status: 0 = No, 1 = Yes |
| `Pclass` | Passenger class: 1st, 2nd, or 3rd |
| `Name` | Passenger name |
| `Sex` | Passenger gender |
| `Age` | Passenger age |
| `SibSp` | Number of siblings/spouses aboard |
| `Parch` | Number of parents/children aboard |
| `Ticket` | Ticket number |
| `Fare` | Passenger fare |
| `Cabin` | Cabin information |
| `Embarked` | Port of embarkation |

The `Survived` column is treated as the target variable for the analysis.

---

## Dataset Profiling

Before cleaning the data, the notebook profiles the raw dataset using:

- Dataset shape
- Column names
- Data types
- Non-null values
- Missing-value counts
- Missing-value percentages
- Duplicate records
- Numerical descriptive statistics
- Categorical variable summaries
- Number of unique values

This initial profiling helps identify problems before making any modifications to the dataset.

---

## Data Cleaning

The dataset is cleaned carefully while preserving as much useful information as possible.

### Missing Values

Missing values are handled based on the meaning and amount of missing data.

- `Age` missing values are replaced using the median age because age is numerical and the median is less sensitive to extreme values.
- `Cabin` contains a large amount of missing information. Instead of directly filling the missing cabin values with an arbitrary category, a `Cabin_known` indicator is created to show whether cabin information was available.
- Missing `Embarked` values are filled using the most frequent category because only a small number of observations are missing.

### Data Types

Categorical variables such as:

- `Pclass`
- `Sex`
- `Embarked`

are converted to categorical data types because they represent groups rather than continuous numerical measurements.

### Duplicate Records

Duplicate rows are checked and removed where appropriate because exact duplicate observations can result in passengers being counted more than once and may affect statistical analysis.

### Outliers

Numerical variables such as `Age`, `Fare`, `SibSp`, and `Parch` are examined using descriptive statistics and the IQR method.

Extreme values are investigated rather than automatically removed because some unusual values may represent genuine passengers or valid observations.

---

## Exploratory Data Analysis

The cleaned dataset is explored through multiple visualizations.

The analysis focuses on the following questions:

### 1. Who survived?

The overall survival distribution is examined to understand how many passengers survived compared with those who did not.

### 2. Did survival differ by gender?

Survival outcomes are compared between male and female passengers to determine whether gender was associated with survival.

### 3. Did passenger class affect survival?

Survival is compared across first-, second-, and third-class passengers to investigate the relationship between passenger class and survival.

### 4. How did age relate to survival?

Age distributions are compared between survivors and non-survivors using histograms and statistical summaries.

Additional age analysis includes:

- Descriptive statistics by survival status
- Median age comparison
- Boxplot comparison

---

## Key Insights

The analysis identifies several important patterns.

### Insight 1 — Gender and Survival

Female passengers had a substantially higher survival rate than male passengers.

This makes gender one of the clearest variables associated with survival in the dataset.

### Insight 2 — Passenger Class and Survival

Survival outcomes differed across passenger classes.

Passengers in higher classes generally had better survival outcomes than passengers in lower classes.

### Insight 3 — Age and Survival

Age distributions differed between survivors and non-survivors, although the relationship was less straightforward than the relationship observed for gender and passenger class.

The age analysis therefore requires more careful interpretation rather than assuming that age alone determined survival.

---

## Data Quality Risks

The dataset contains several data-quality considerations.

### Missing Cabin Information

A large proportion of passengers do not have recorded cabin information.

Treating these missing values as if they represented a specific cabin could introduce misleading assumptions. Therefore, cabin availability is represented using a separate indicator.

### Missing Age Values

Age contains missing observations. Median imputation is used to retain these passengers while reducing the influence of extreme values.

### Potential Outliers

Variables such as `Fare` may contain unusually high values. These values are investigated but not automatically removed because they may represent genuine observations.

---

## Modeling and Leakage Risk

The `Survived` column represents the outcome we are trying to understand or predict.

Therefore, it must not be used as an input feature when building a predictive model.

Using `Survived` as a feature would introduce **target leakage**, allowing the model to access the answer it is supposed to predict.

`PassengerId` should also generally be treated as an identifier rather than a meaningful predictive variable.

Any future modeling work should ensure that only information available at prediction time is used as an input.

---

## Project Structure

```text
EDA_Challenge/
│
├── data/
│   └── train.csv
│
├── EDA.ipynb
├── README.md
├── summary.md
├── requirements.txt
└── .gitignore
