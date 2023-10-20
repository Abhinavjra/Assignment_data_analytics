# -*- coding: utf-8 -*-
"""data_anlytics_assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aAekTR7FmPviMaMmQbrJrVixugdKwMbR
"""

#1)	Please take care of missing data present in the “Data.csv” file using python module
#“sklearn.impute” and its methods, also collect all the data that has “Salary” less than “70,000”.

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

data_df = pd.read_csv('/content/Data.csv')
indian_df = pd.read_csv('//content/Indian_cities.csv')

data_df.head()

imputer = SimpleImputer(strategy='mean')

# Impute missing values in the 'Salary' column

data_df['Salaries'] = imputer.fit_transform(data_df[['Salaries']])

# Filter data where 'Salary' is less than 70000

filtered_data = data_df[data_df['Salaries'] < 70000]

print(filtered_data)

#2)	Subtracting dates:
#Python date objects let us treat calendar dates as something similar to numbers: we can compare them, sort them, add, and even subtract them. Do math with dates
#in a way that would be a pain to do by hand. The 2007 Florida hurricane season was one of the busiest on record, with 8 hurricanes in one year. The first one
#hit on May 9th, 2007, and the last one hit on December 13th, 2007. How many days elapsed between the first and last hurricane in 2007?

from datetime import date


# Create a date object for May 9th, 2007
start = date(2007, 5, 9)

# Create a date object for December 13th, 2007
end = date(2007, 12, 13)

# Calculate the number of days between the two dates
elapsed_days = end - start

# Print the number of days
print(elapsed_days.days)

#3)	Representing dates in different ways
#Date objects in Python have a great number of ways they can be printed out as strings. In some cases, you want to know the date in a clear, language-agnostic format.
#In other cases, you want something which can fit into a paragraph and flow naturally.
#Print out the same date, August 26, 1992 (the day that Hurricane Andrew made landfall in Florida), in a number of different ways, by using the “ .strftime() ” method.
#Store it in a variable called “Andrew”.


from datetime import date

andrew = date(1992,8,26)
formated_date_1 = andrew.strftime('%Y-%M')
formated_date_2 = andrew.strftime('%Y-%j')
formated_data_3 = andrew.strftime('%B-%Y')
print(formated_date_1)
print(formated_date_2)
print(formated_data_3)

#4)	For the dataset “Indian_cities”,
#a)	Find out top 10 states in female-male sex ratio
indian_df.info()

indian_df['sex_ratio'] = (indian_df['population_male'] / indian_df['population_female'])
sorted_data = indian_df.sort_values(by='sex_ratio',ascending=False)
top_10_state = sorted_data.head(10)
print(top_10_state[['state_name','sex_ratio']])

#b)	Find out top 10 cities in total number of graduates

indian_df.groupby('name_of_city')['total_graduates'].sum().sort_values(ascending=False).head(10).reset_index()

#c)	Find out top 10 cities and their locations in respect of  total effective_literacy_rate.

sorted_city = indian_df.sort_values(by='effective_literacy_rate_total',ascending=False).head(10).reset_index()
print(sorted_city[['name_of_city','location','effective_literacy_rate_total']])

#5)	 For the data set “Indian_cities”
#a)	Construct histogram on literates_total and comment about the inferences

import matplotlib.pyplot as plt

plt.hist(indian_df['literates_total'],bins=8,color='red',alpha=0.7)
plt.xlabel('Total_literates')
plt.ylabel('Frequency')
plt.title('Histogram of total literates')
plt.show

#b)	Construct scatter  plot between  male graduates and female graduates

plt.scatter(['male_graduates'],['female_graduates'])

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('scallter plot')

plt.show

#6)	 For the data set “Indian_cities”
#a)	Construct Boxplot on total effective literacy rate and draw inferences

plt.figure(figsize=(8, 6))
plt.boxplot(df['effective_literacy_rate_total'], vert=False)
plt.title('Boxplot of Total Effective Literacy Rate')
plt.xlabel('Total Literacy Rate')
plt.yticks([])
plt.show()

#b)	Find out the number of null values in each column of the dataset and delete them.

null_value_counts = indian_df.isnull().sum()
print("null value count in eax]ch columns:\n")
print(null_value_counts)