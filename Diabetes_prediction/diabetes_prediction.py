# -*- coding: utf-8 -*-
"""Diabetes_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19K5OXpPe4jihgD2JL9IegsWMNZf8lwTE
"""

AUTHOR: Adedolapo Sharon Olatunji

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score,roc_curve

# %matplotlib inline

"""LOAD DIABETES DATASET"""

data = pd.read_csv('diabetes.csv')
data

data.shape

data.head(10)

# check for any null values
data.isnull().values.any()

data.isnull().sum()

data.dtypes

"""CHECK TARGET VARIABLES"""

data['BloodPressure'].value_counts()

data['BMI'].value_counts()

data['Pregnancies'].value_counts()

"""DATA ANALYSIS"""

plt.figure(figsize=(20,12))
sb.heatmap(data.corr(),annot=True,linewidth =2)
plt.tight_layout()

sb.countplot(x= 'Outcome', data=data)
plt.show()

sb.barplot(x='Outcome',y='BMI',data=data)

sb.barplot(x='Outcome',y='Pregnancies',data=data)

# Histogram of each feature
import itertools

col = data.columns[:8]
plt.subplots(figsize = (20, 15))
length = len(col)

for i, j in itertools.zip_longest(col, range(length)):
    plt.subplot((length//2), 3, j + 1)
    plt.subplots_adjust(wspace = 0.1,hspace = 0.5)
    data[i].hist(bins = 20)
    plt.title(i)
plt.show()

# Scatter plot matrix
import pandas as pd
from pandas.plotting import scatter_matrix

scatter_matrix(data, figsize=(20, 20))

"""FEATURES AND LABELS"""

x = data.drop('Outcome',axis=1)
y = data['Outcome']
print(x.shape)
print(y.shape)

"""DATASET SPLITTING"""

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.30,random_state=42)

"""MODEL"""

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()

"""MODEL FITTING"""

model.fit(x_train,y_train)

print('Train Scr',model.score(x_train,y_train))
print('Test Scr',model.score(x_test,y_test))

y_pred = model.predict(x_test)
print(y_pred)

accuracy = accuracy_score(y_test,y_pred)
print(f"Accuracy: {accuracy:.2%}")

"""MODEL EVALUATION"""

eval_mat = confusion_matrix(y_test,y_pred)
print(eval_mat)

report = classification_report(y_test,y_pred)
print("Classification Report:")
print(report)

res = model.predict_proba(x_test)
print(res[:5])

# res = lr1.predict_proba(x_test[:,1])

fpr,tpr,thresh = roc_curve(y_test,res[:,1])
auc_scr = roc_auc_score(y_test,res[:,1])
print('AUC',auc_scr)
plt.plot(fpr,tpr)
plt.plot([0,1],[0,1],color='green')
plt.title('ROC-AUC Score')
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.show()

