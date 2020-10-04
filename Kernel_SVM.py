# Kernel SVM tutorial from Machine Learning A-Z - SuperDataScience
# Input by Ryan L Buchanan 02OCT20

# Import libraries
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

# Import dataset
dataset = pd.read_csv('Social_Network_ads.csv')
X = dataset.iloc[:, 2:4].values
y = dataset.iloc[:, -1].values

# Split dataset