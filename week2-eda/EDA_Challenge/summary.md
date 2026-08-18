# Titanic EDA — One-Page Insight Summary

## Three Key Insights

### 1. Gender was strongly associated with survival

Female passengers had a substantially higher survival rate than male passengers. Gender was one of the clearest variables associated with survival in the Titanic dataset.

### 2. Passenger class was associated with survival

Passengers in higher classes generally had better survival outcomes than passengers in lower classes. This suggests that passenger class was an important characteristic associated with survival.

### 3. Age showed differences between survivors and non-survivors

The age distributions of survivors and non-survivors were different, although the relationship between age and survival was less straightforward than the patterns observed for gender and passenger class.

## Data Quality / Leakage Risk

The dataset contains missing values, particularly in the Age and Cabin columns. Age was handled using median imputation, while Cabin information was converted into a `Cabin_known` indicator.

The `Survived` column is the target variable and must not be used as an input feature when building a predictive model. Using it as a feature would cause target leakage and produce misleading model performance.

`PassengerId` should generally be treated as an identifier rather than a meaningful predictive feature.

## Actionable Takeaway

Gender and passenger class are the clearest variables associated with survival in this dataset. Any future predictive analysis should carefully handle missing values, categorical variables, and potential leakage.

## Conclusion

The EDA shows that Titanic survival was not evenly distributed across passengers. Female passengers and passengers in higher classes generally had better survival outcomes, while age showed a more nuanced relationship with survival.

The analysis demonstrates the importance of profiling and cleaning data before drawing conclusions or building predictive models.
