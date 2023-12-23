# Retail Display Strategy Analysis

The project aims to leverage the available data to understand the factors influencing the display of products in stores. By utilizing this information, it's possible to develop more effective strategies to boost sales, enhance product visibility, and optimize commercial performance.


## Dataset
- The dataset used in this analysis is sourced from 'new_Base_CDM_balanced_V2.csv', consisting of 25782 rows and 8 columns. The columns include both categorical and numerical variables related to sales, turnover, store information, and display strategies.

### Data Exploration
- Analyzing the distribution of categorical variables ('y_display', 'X5_ENSEIGNE', 'X7_Feature') through count plots and contingency tables.
- Examining the relationship between categorical variables using chi-squared tests.
- Univariate and bivariate exploration of numerical variables to understand their distributions and relationships.

### Data Transformation
- Discretization of numerical variables using MDLP (Minimum Description Length Principle).

### Statistical Analysis
- Conducting chi-squared tests to assess the relationship between discretized numerical variables and 'y_display'.
