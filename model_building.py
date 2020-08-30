# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 15:18:23 2020

@author: Micha
"""

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

df = pd.read_csv('eda_data.csv')

# choose relevant columns 
df.columns

df_model = df[['avg_salary', 'Rating', 'Size', 'Type of ownership', 'Industry', 'Sector', 'Revenue', 'hourly', 'employer_provided', 'job_state', 'age', 'python_yn', 'rstudio_yn', 'spark_yn', 'aws_yn', 'excel_yn', 'java_yn', 'scala_yn', 'go_yn', 'csharp_yn', 'rust_yn', 'sql_yn', 'matlab_yn', 'job_simple', 'seniority', 'desc_len']]

#df_model = df[['avg_salary', 'Rating', 'Size', 'Type of ownership', 'Industry', 'Sector', 'Revenue', 'hourly', 'employer_provided', 'job_state', 'age', 'python_yn', 'sql_yn', 'job_simple', 'seniority', 'desc_len']]

# get dummy data 
df_dum = pd.get_dummies(df_model)

# train test split 
from sklearn.model_selection import train_test_split

X = df_dum.drop('avg_salary', axis =1)
y = df_dum.avg_salary.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# multiple linear regression 
import statsmodels.api as sm

X_sm = X = sm.add_constant(X)
model = sm.OLS(y,X_sm)
model.fit().summary()

from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score

lm = LinearRegression()
lm.fit(X_train, y_train)

np.mean(cross_val_score(lm,X_train,y_train, scoring = 'neg_mean_absolute_error'))

# Lasso regression
lm_l = Lasso(alpha=.13)
lm_l.fit(X_train,y_train)

np.mean(cross_val_score(lm_l,X_train,y_train, scoring = 'neg_mean_absolute_error'))

alpha = []
error = []

for i in range(1,100):
    alpha.append(i/100)
    lml = Lasso(alpha=(i/100))
    error.append(np.mean(cross_val_score(lm_l,X_train,y_train, scoring = 'neg_mean_absolute_error')))
    
plt.plot(alpha,error)

err = tuple(zip(alpha,error))
df_err = pd.DataFrame(err, columns = ['alpha', 'error'])
df_err[df_err.error == max(df_err.error)]

# Random forest
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()

np.mean(cross_val_score(rf,X_train,y_train,scoring = 'neg_mean_absolute_error'))

# Tune models with GridsearchCV
from sklearn.model_selection import GridSearchCV
parameters = {'n_estimators':range(10,300,10),'criterion':('mse', 'mae'), 'max_features':('auto','sqrt', 'log2')}

gs = GridSearchCV(rf,parameters,scoring='neg_mean_absolute_error')
gs.fit(X_train,y_train)

gs.best_score_
gs.best_estimator_

# Test ensembles
tpred_lm = lm.predict(X_test)
tpred_lml = lm_l.predict(X_test)
tpred_rf = gs.best_estimator_.predict(X_test)

from sklearn.metrics import mean_absolute_error
#mean_absolute_error(y_test,tpred_lm)
mean_absolute_error(y_test,tpred_lml)
mean_absolute_error(y_test,tpred_rf)

#mean_absolute_error(y_test,(tpred_lml+tpred_rf)/2)