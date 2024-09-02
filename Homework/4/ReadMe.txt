Overview
This assignment focuses on the implementation of decision trees for classification tasks and the application of machine learning models for time series prediction. It includes both theoretical exercises and practical tasks using Python libraries.

Sections
Theoretical Questions:

Entropy and Information Gain:
Calculate the entropy of the possibility of holding a tennis match based on provided weather data.
Compute the Information Gain for the temperature feature and determine the best feature to use as the root node in a decision tree using the ID3 algorithm.
Decision Tree Implementation:
Construct a decision tree up to a depth of 2 using the ID3 algorithm based on the given dataset.
Use the constructed decision tree to predict the labels of new samples and calculate the accuracy.
Extract and list all the rules derived from the decision tree.
Practical Implementation:

Data Preprocessing:
Handle missing values and imbalanced data in the provided dataset.
Normalize features and convert non-numeric features into numeric ones.
Model Training and Evaluation:
Split the dataset into training and testing sets.
Train a decision tree model and a k-Nearest Neighbors (k-NN) model, then compare their performance based on execution time, accuracy, precision, recall, and F1 score.
Visualize the results using bar charts and confusion matrices.
Time Series Prediction:
Transform a temperature dataset into a time series suitable for predicting the next day's temperature using a sliding window approach.
Train a linear regression model to predict future temperatures and evaluate its performance using metrics like Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).
Implement a Support Vector Machine (SVM) model and compare its predictions with those of the linear regression model.