# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 21:23:02 2023

@author: tomgr
"""

import pandas as pd
# file_name = pd.read_csv('file.csv') <-- format to read a file
data = pd.read_csv('transaction.csv',sep=';')

data = pd.read_csv('transaction.csv',sep=';')

# Summary of the data
data.info()

#working with calculations

#defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

# Mathimatical Operations on Tableau
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransation = NumberOfItemsPurchased * ProfitPerItem
SellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

# adding a new column to a dataframe
#data['CostPerTransaction'] = CostPerTransaction

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#Sales Per Transaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] - data['NumberOfItemsPurchased']

#Profit Per Transactions
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# markup = (sales-cost)/cost
data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']

#Round Function. Ruturns a number that is rounded vertion
roundmarkup = round(data['Markup'],2)
data['Markup'] = round(data['Markup'],2)

# Combine date fields

my_name = 'Dee' + 'Neidoo'
my_date = 'Day' + '-'+'Month'+'Year'

#my_date = data['Day']
#Checking columns Datatype
print(data['Day'].dtype)

#Change columns type
day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(year.dtype)
print(day.dtype)

my_date = day + '-'+data['Month']+'-'+year

data['date'] = my_date

# using iloc to view specific column / rows
data.iloc[0] # views the row with index = 0
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 

data.head(5) # first 5 rows

data.iloc[:,2] # all rows on 2nd column
data.iloc[4,2] # forth row, second column

# split client keywords seperated by comma into three fields 
# new_var = column.str.split('sep'),expand = true)
split_col = data['ClientKeywords'].str.split(',' , expand=True)

#creating new columns for the split columns in Client Keywords
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

# Using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']' , '')

# Using the lower function to change item to lower case
data['ItemDescription'] = data['ItemDescription'].str.lower()

# how to merge files
# bring in a new dataset
seasons = pd.read_csv('value_inc_seasons.csv')

seasons = pd.read_csv('value_inc_seasons.csv',sep=';')

# summary of the dataset
seasons.info()

# merging files: merge_df = pd.merge(df_old, df_new, on = 'key')
data = pd.merge(data, seasons, on = 'Month')

# drop clientkeywords and Month, day, year
# df = df.drop('columnname', axis = 1)
data = data.drop('ClientKeywords', axis =1)
data = data.drop('Day', axis =1)
data = data.drop(['Month','Year'], axis =1)

# export into CSF file
data.to_csv('ValueInc_Cleaned.csv', index = False)



















