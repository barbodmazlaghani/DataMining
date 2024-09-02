Overview
This assignment involves working with frequent pattern mining techniques and implementing data analysis using PySpark. The tasks include both theoretical exercises on pattern mining and practical implementation using the PySpark API on a provided dataset.

Sections
Theoretical Questions:

Question 1:
Given two transaction datasets, calculate frequent itemsets and generate association rules using the FP-Growth and Apriori algorithms.
Identify max-patterns, closed patterns, and generate all strong association rules.
Question 2:
Analyze the validity of various statements regarding strong association rules and itemsets.
Prove specific relationships between itemsets and their confidence values.
Question 3:
Compare frequent pattern mining with sequential pattern mining, explaining key differences.
Implement the PrefixSpan algorithm to identify sequential patterns in a given dataset.
Discuss the monotonicity of constraints applied in sequential pattern mining.
Question 4:
Analyze a given dataset of transactions involving two items (onions and carrots) and compute various statistical metrics (e.g., lift, chi-square, Kulczynski, imbalance ratio).
Determine the relationship between purchasing these items using calculated metrics.
Question 5:
Apply different constraints (e.g., sum of prices, presence of specific items) to frequent pattern mining in a shopping dataset and discuss how these constraints affect the mining process.
Practical Implementation:

Data Preprocessing with PySpark:
Load the provided Groceries.csv dataset into a PySpark DataFrame.
Perform initial data cleaning, such as removing unnecessary columns and restructuring data to aggregate all purchases by individual customers.
Frequent Pattern Mining:
Use the FPGrowth function in PySpark to identify frequent itemsets and generate association rules with specified minimum support and confidence levels.