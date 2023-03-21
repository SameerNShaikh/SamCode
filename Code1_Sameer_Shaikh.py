# -*- coding: utf-8 -*-
"""MLCA1_LinearRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17sfw_J9LuZmALhh0eyifCh81JtSIqmF3

#LINEAR REGRESSION

> To predict life expectancy from data provided by the WHO using linear regression model

"""

######################################## Start of Un-optimised linear regression #######################################

import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.feature_selection import RFE
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV

df=pd.read_csv('LifeExpectancy.csv')

#Check missing values

check_missing=df.isnull()
#print(check_missing)
for column in check_missing.columns.values.tolist():
  print(column)
  print(check_missing[column].value_counts())
  print("")

# Replacing missing values with nan

df.replace(" ", np.nan, inplace = True)
pd.set_option('display.max_columns', None)
df.head(50)

# Replacing nan values with 0

df["Life expectancy"].replace(np.nan, 0, inplace=True)

df["Adult Mortality"].replace(np.nan, 0, inplace=True)

df["infant deaths"].replace(np.nan, 0, inplace=True)

df["Alcohol"].replace(np.nan, 0, inplace=True)

df["percentage expenditure"].replace(np.nan, 0, inplace=True)

df["Hepatitis B"].replace(np.nan, 0, inplace=True)

df["BMI"].replace(np.nan, 0, inplace=True)

df["Polio"].replace(np.nan, 0, inplace=True)

df["Total expenditure"].replace(np.nan, 0, inplace=True)

df["Diphtheria"].replace(np.nan, 0, inplace=True)

df["HIV/AIDS"].replace(np.nan, 0, inplace=True)

df["GDP"].replace(np.nan, 0, inplace=True)

df["Population"].replace(np.nan, 0, inplace=True)

df["thinness  1-19 years"].replace(np.nan, 0, inplace=True)

df["thinness 5-9 years"].replace(np.nan, 0, inplace=True)

df["Income composition of resources"].replace(np.nan, 0, inplace=True)

df["Schooling"].replace(np.nan, 0, inplace=True)

df.info()

x = df.drop(['Country', 'Status','Life expectancy'], axis = 1) # Features selection
y = df['Life expectancy']

reg = LinearRegression()
reg.fit(x, y)
print("r2 Score: ", reg.score(x, y))
ypred = reg.predict(x)
print("prediction", ypred)

######################################## End of Un-Optimised linear regression ######################################

######################################## Start of Optimised linear regression #######################################

df=pd.read_csv('LifeExpectancy.csv')

print(df.describe())

df.info()

# Setting values for 'developed' & 'developing' in 'Status' column

def converter(column):
  if column == 'Developed':
    return 0
  else:
    return 1

df['Status']=df['Status'].apply(converter)

df.info()

#Check missing values

check_missing=df.isnull()
#print(check_missing)
for column in check_missing.columns.values.tolist():
  print(column)
  print(check_missing[column].value_counts())
  print("")

# Replacing missing values with nan

df.replace(" ", np.nan, inplace = True)
pd.set_option('display.max_columns', None)
df.head(50)

"""check_missing=df.isnull()
#print(check_missing)
for column in check_missing.columns.values.tolist():
  print(column)
  print(check_missing[column].value_counts())
  print("")"""

# Replacing nan values with respective averages

avg_Le = df["Life expectancy"].mean(axis=0)
df["Life expectancy"].replace(np.nan, avg_Le, inplace=True)

avg_Am = df["Adult Mortality"].mean(axis=0)
df["Adult Mortality"].replace(np.nan, avg_Am, inplace=True)

avg_Id = df["infant deaths"].mean(axis=0)
df["infant deaths"].replace(np.nan, avg_Id, inplace=True)

avg_Alc = df["Alcohol"].mean(axis=0)
df["Alcohol"].replace(np.nan, avg_Alc, inplace=True)

avg_Pe = df["percentage expenditure"].mean(axis=0)
df["percentage expenditure"].replace(np.nan, avg_Pe, inplace=True)

avg_Hb = df["Hepatitis B"].mean(axis=0)
df["Hepatitis B"].replace(np.nan, avg_Hb, inplace=True)

avg_Bmi = df["BMI"].mean(axis=0)
df["BMI"].replace(np.nan, avg_Bmi, inplace=True)

avg_Po = df["Polio"].mean(axis=0)
df["Polio"].replace(np.nan, avg_Po, inplace=True)

avg_Te = df["Total expenditure"].mean(axis=0)
df["Total expenditure"].replace(np.nan, avg_Te, inplace=True)

avg_Dp = df["Diphtheria"].mean(axis=0)
df["Diphtheria"].replace(np.nan, avg_Dp, inplace=True)

avg_Ha = df["HIV/AIDS"].mean(axis=0)
df["HIV/AIDS"].replace(np.nan, avg_Ha, inplace=True)

avg_Gd = df["GDP"].mean(axis=0)
df["GDP"].replace(np.nan, avg_Gd, inplace=True)

avg_Pop = df["Population"].mean(axis=0)
df["Population"].replace(np.nan, avg_Pop, inplace=True)

avg_Th1 = df["thinness  1-19 years"].mean(axis=0)
df["thinness  1-19 years"].replace(np.nan, avg_Th1, inplace=True)

avg_Th2 = df["thinness 5-9 years"].mean(axis=0)
df["thinness 5-9 years"].replace(np.nan, avg_Th2, inplace=True)

avg_Ic = df["Income composition of resources"].mean(axis=0)
df["Income composition of resources"].replace(np.nan, avg_Ic, inplace=True)

avg_Sch = df["Schooling"].mean(axis=0)
df["Schooling"].replace(np.nan, avg_Sch, inplace=True)

df.head(50)

"""AllAvgs=[avg_Le, avg_Am, avg_Id, avg_Alc, avg_Pe, avg_Po, avg_Te, avg_Dp, avg_Ha, avg_Gd, avg_Pop, avg_Th1, avg_Th2, avg_Ic,avg_Sch]
print(AllAvgs)"""

df.info()

corrs = df.corr()
figure = ff.create_annotated_heatmap(
    z=corrs.values,
    x=list(corrs.columns),
    y=list(corrs.index),
    annotation_text=corrs.round(2).values,
    showscale=True)
figure.show()

X = df.drop(['Country','Life expectancy', 'Income composition of resources','infant deaths','percentage expenditure','thinness 5-9 years'], axis = 1) # Features selection
y = df['Life expectancy']

#performing scaling
feature_scaler = StandardScaler()
X_scaled = feature_scaler.fit_transform(X)

#splitting into train and test data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

X_train.shape, y_train.shape

reg = LinearRegression()
reg.fit(X_train,y_train)
print("Score: ", reg.score(X_test,y_test))
ypred = reg.predict(X_test)

r2 = r2_score(y_test, ypred)
print("r2 Score: ", r2)

# creating a cross-validation scheme
folds = KFold(n_splits = 5, shuffle = True, random_state = 100)

# specifying range of hyperparameters to tune
hyper_params = [{'n_features_to_select': list(range(1, 17))}]

reg = LinearRegression()
reg.fit(X_train,y_train)
rfe = RFE(reg)             

#calling GridSearchCV for cross validation
gd_sr = GridSearchCV(estimator = rfe, param_grid = hyper_params, scoring= 'r2', cv = folds, verbose = 1, return_train_score=True)      

# fitting the model
gd_sr.fit(X_train, y_train)
crossval_results = pd.DataFrame(gd_sr.cv_results_)
best_result = gd_sr.best_score_
print("best result: ", best_result)
print("prediction", ypred)

# plotting the graph for cv results
plt.figure(figsize=(18,10))

plt.plot(crossval_results["param_n_features_to_select"], crossval_results["mean_test_score"])
plt.plot(crossval_results["param_n_features_to_select"], crossval_results["mean_train_score"])
plt.xlabel('number of features')
plt.ylabel('r-squared')
plt.title("Optimal Number of Features")
plt.legend(['test score', 'train score'], loc='lower right')

######################################## End of Optimised linear regression ######################################