#Data Cleaning Strategy
This project implements a multi-step data cleaning pipeline to transform raw data into a clean, analysis-ready format. The strategy addresses missing values, incorrect data types, and feature scaling.

1. Imputation of Missing Values
Missing data is handled first to create a more complete dataset. The strategy uses different techniques depending on the column:

Forward Fill (ffill): For the numeric_col and price columns, missing values are filled using the last known observation. This method is effective for sequential data where the most recent value is often the best estimate.

Median Fill: After initial filling, any remaining missing values in numerical columns are imputed with the column's median. Using the median is a robust technique that is not sensitive to outliers.

2. Data Type Correction
Several columns require type conversion to be useful for analysis:

Price Column: The price column, which is initially loaded as a string (e.g., '$100'), is cleaned by removing the dollar sign ($) and converting the data type to float.

Date Column: The date_str column is converted from a string to a proper datetime object, allowing for time-series analysis. Any values that cannot be converted are coerced into NaT (Not a Time).

3. Dropping Remaining Missing Rows
After the imputation and type conversion steps, any rows that still contain missing values (such as in categorical columns or dates that became NaT) are dropped entirely. This final step ensures the resulting dataset is complete and has no missing data points.

4. Normalization
As a final preprocessing step, the numerical columns in the cleaned dataset are scaled using Min-Max Normalization. This rescales the data to a uniform range of 0 to 1, ensuring that all features have a similar scale before being used in analysis or machine learning models.
