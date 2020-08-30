# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 23:05:08 2020

@author: Micha
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

#Salary Parsing
df['hourly'] = df['Salary Estimate'].apply (lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply (lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply (lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K', '').replace('$', ''))

min_hr = minus_kd.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary:',''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

#Company Name Text
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)

#Location Information
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts()

df['state_hq'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

#Age of Company
df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2020 - x)

#Job Description Parsing (word cloud)
df['Job Description'][0]

#Python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python_yn.value_counts()

#R
df['rstudio_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() or 'r,' in x.lower() or 'r language' in x.lower() or 'r languages' in x.lower() or 'or r' in x.lower() or 'languages r' in x.lower() else 0)
df.rstudio_yn.value_counts()

#Spark
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark_yn.value_counts()

#AWS
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws_yn.value_counts()

#Excel
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel_yn.value_counts()

#Java (JavaScript)
df['java_yn'] = df['Job Description'].apply(lambda x: 1 if 'java' in x.lower() or 'javascript' in x.lower() else 0)
df.java_yn.value_counts()

#Swift
df['swift_yn'] = df['Job Description'].apply(lambda x: 1 if 'swift' in x.lower() else 0)
df.swift_yn.value_counts()

#Scala
df['scala_yn'] = df['Job Description'].apply(lambda x: 1 if 'scala' in x.lower() else 0)
df.scala_yn.value_counts()

#Go
df['go_yn'] = df['Job Description'].apply(lambda x: 1 if 'go' in x.lower() else 0)
df.go_yn.value_counts()

#Elm
df['elm_yn'] = df['Job Description'].apply(lambda x: 1 if 'elm' in x.lower() else 0)
df.elm_yn.value_counts()

#Ruby
df['ruby_yn'] = df['Job Description'].apply(lambda x: 1 if 'ruby' in x.lower() else 0)
df.ruby_yn.value_counts()

#C Sharp
df['csharp_yn'] = df['Job Description'].apply(lambda x: 1 if 'C#' in x.lower() or 'c++' in x.lower() or 'c languages' in x.lower() or 'c language' in x.lower() else 0)
df.csharp_yn.value_counts()

#Rust
df['rust_yn'] = df['Job Description'].apply(lambda x: 1 if 'rust' in x.lower() else 0)
df.rust_yn.value_counts()

#SQL
df['sql_yn'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
df.sql_yn.value_counts()

#MatLab
df['matlab_yn'] = df['Job Description'].apply(lambda x: 1 if 'matlab' in x.lower() else 0)
df.matlab_yn.value_counts()

#Julia
df['julia_yn'] = df['Job Description'].apply(lambda x: 1 if 'julia' in x.lower() else 0)
df.julia_yn.value_counts()

df.columns

df_out = df.drop(['Unnamed: 0'], axis = 1)

df_out.to_csv('salary_data_cleaned.csv')