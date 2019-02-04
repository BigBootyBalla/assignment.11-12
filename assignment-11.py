import numpy as np
import matplotlib
matplotlib.use('Agg') # This is only required to use matplotlib on Cloud9
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("degrees-that-pay-back.csv") # df stands for Data Frame, the main data structure in Pandas
df.head() 
df = df.set_index('Undergraduate Major') 
df = df.sort_values(by='Starting Median Salary')
columns = ['Starting Median Salary', 'Mid-Career Median Salary',  'Mid-Career 90th Percentile Salary'] 
df = df[columns]
for column in columns:
    df[column] = df[column].str.replace('$','') # remove '$' signs
    df[column] = df[column].str.replace(',','') # remove ','
    df[column] = df[column].astype(float) # convert to float data type instead of string
plot = df.plot.barh(figsize=(25,25)) # this creates an horizontal bar chart
plot.get_figure().savefig('DegreesMoneyPlot.svg') 