# Titanic Survival Analysis

## Description
This project analyses Titanic passenger data to find out which groups of passengers were more likely to survive.

## Data
The Titanic dataset from seaborn-data (891 passengers). It is loaded directly from a URL.

## Steps
- Filled missing `age` values with the median.
- Dropped the `deck` column because 77% of its values were missing.
- Grouped the survival rate by `sex` and `pclass`.

## Output
- A table of survival rates by sex and class.
- A bar chart of survival rate by class.

## Findings
- Female passengers had a higher survival rate than male passengers.
- Passengers in class 1 had the highest survival rate.
- Passengers who paid the highest fares were all in class 1.
- Although there were more male passengers, only 19% of them survived, compared with 74% of female passengers.
## How to Run
1. Install the libraries: `pip install pandas matplotlib`
2. Run: `python titanic.py` (an internet connection is required)

## Libraries
- pandas
- matplotlib