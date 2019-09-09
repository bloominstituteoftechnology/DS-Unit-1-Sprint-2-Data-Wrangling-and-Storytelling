#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'module1-join-and-reshape-data'))
	#print(os.getcwd())
except:
	pass
#%% [markdown]
# _Lambda School Data Science_
# 
# # Join and Reshape datasets
# 
# Objectives
# - concatenate data with pandas
# - merge data with pandas
# -  understand tidy data formatting
# -  melt and pivot data with pandas
# 
# Links
# - [Pandas Cheat Sheet](https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf)
# - [Tidy Data](https://en.wikipedia.org/wiki/Tidy_data)
#   - Combine Data Sets: Standard Joins
#   - Tidy Data
#   - Reshaping Data
# - Python Data Science Handbook
#   - [Chapter 3.6](https://jakevdp.github.io/PythonDataScienceHandbook/03.06-concat-and-append.html), Combining Datasets: Concat and Append
#   - [Chapter 3.7](https://jakevdp.github.io/PythonDataScienceHandbook/03.07-merge-and-join.html), Combining Datasets: Merge and Join
#   - [Chapter 3.8](https://jakevdp.github.io/PythonDataScienceHandbook/03.08-aggregation-and-grouping.html), Aggregation and Grouping
#   - [Chapter 3.9](https://jakevdp.github.io/PythonDataScienceHandbook/03.09-pivot-tables.html), Pivot Tables
#   
# Reference
# - Pandas Documentation: [Reshaping and Pivot Tables](https://pandas.pydata.org/pandas-docs/stable/reshaping.html)
# - Modern Pandas, Part 5: [Tidy Data](https://tomaugspurger.github.io/modern-5-tidy.html)

#%%
get_ipython().system('rm instacart_2017_05_01/*')
get_ipython().system('wget -N https://s3.amazonaws.com/instacart-datasets/instacart_online_grocery_shopping_2017_05_01.tar.gz')


#%%
get_ipython().system('tar -xzvf instacart_online_grocery_shopping_2017_05_01.tar.gz')

#%%
get_ipython().system('ls instacart_2017_05_01 -Alh')


#%%
get_ipython().system('head instacart_2017_05_01/*.csv -n 3')

#%% [markdown]
# # Assignment
# 
# ## Join Data Practice
# 
# These are the top 10 most frequently ordered products. How many times was each ordered? 
# 
# 1. Banana
# 2. Bag of Organic Bananas
# 3. Organic Strawberries
# 4. Organic Baby Spinach 
# 5. Organic Hass Avocado
# 6. Organic Avocado
# 7. Large Lemon 
# 8. Strawberries
# 9. Limes 
# 10. Organic Whole Milk
# 
# First, write down which columns you need and which dataframes have them.
# 
# Next, merge these into a single dataframe.
# 
# Then, use pandas functions from the previous lesson to get the counts of the top 10 most frequently ordered products.

#%%
import pandas
order_products__prior = pandas.read_csv('instacart_2017_05_01/order_products__prior.csv')
order_products__train = pandas.read_csv('instacart_2017_05_01/order_products__train.csv')
order_products = pandas.concat([order_products__prior, order_products__train])
orders = pandas.read_csv('instacart_2017_05_01/orders.csv')
products = pandas.read_csv('instacart_2017_05_01/products.csv')

order_columns = ['order_id', 'order_hour_of_day']
product_columns = ['product_id', 'product_name']
order_product_columns = ['order_id', 'product_id']

df_instacart = pandas.merge(orders[order_columns],
					pandas.merge(products[product_columns], 
								order_products[order_product_columns], 
								on='product_id'),
					on='order_id')

df_instacart['product_name'].value_counts().head(10)


#%% [markdown]
# ## Reshape Data Section
# 
# - Replicate the lesson code
# - Complete the code cells we skipped near the beginning of the notebook
# - Table 2 --> Tidy
# - Tidy --> Table 2
# - Load seaborn's `flights` dataset by running the cell below. Then create a pivot table showing the number of passengers by month and year. Use year for the index and month for the columns. You've done it right if you get 112 passengers for January 1949 and 432 passengers for December 1960.

#%%
import pandas, numpy
table1 = pandas.DataFrame(
    [[numpy.nan, 2],
     [16,    11], 
     [3,      1]],
    index=['John Smith', 'Jane Doe', 'Mary Johnson'], 
    columns=['treatmenta', 'treatmentb'])

table2 = table1.T.reset_index().rename(columns={'index':'treatment'})
table2.head(10)

#%%


tidy = table2.melt(
				id_vars=['treatment'], 
				value_vars=['John Smith', 'Jane Doe', 'Mary Johnson'],
				var_name='name',
				value_name='result'
				).replace(
						to_replace={'treatmenta': 'a',
									'treatmentb': 'b'}
						)

tidy.head(10)

#%%
table2_rebuilt = tidy.replace(
							to_replace={'a': 'treatmenta',
										'b': 'treatmentb'}
							).pivot_table(
										index='treatment',
										columns='name',
										values='result'
										)

table2_rebuilt.head(10)

#%%
import seaborn
flights = seaborn.load_dataset('flights')
flights.head(30)


#%%
flights.pivot_table(
					index='year',
					columns='month',
					values='passengers'
					)

#%% [markdown]
# ## Join Data Stretch Challenge
# 
# The [Instacart blog post](https://tech.instacart.com/3-million-instacart-orders-open-sourced-d40d29ead6f2) has a visualization of "**Popular products** purchased earliest in the day (green) and latest in the day (red)." 
# 
# The post says,
# 
# > "We can also see the time of day that users purchase specific products.
# 
# > Healthier snacks and staples tend to be purchased earlier in the day, whereas ice cream (especially Half Baked and The Tonight Dough) are far more popular when customers are ordering in the evening.
# 
# > **In fact, of the top 25 latest ordered products, the first 24 are ice cream! The last one, of course, is a frozen pizza.**"
# 
# Your challenge is to reproduce the list of the top 25 latest ordered popular products.
# 
# We'll define "popular products" as products with more than 2,900 orders.
# 
# 

#%% [markdown]
# ### See Unit 1 Sprint 1 Module 4

#%% [markdown]
# ## Reshape Data Stretch Challenge
# 
# _Try whatever sounds most interesting to you!_
# 
# - Replicate more of Instacart's visualization showing "Hour of Day Ordered" vs "Percent of Orders by Product"
# - Replicate parts of the other visualization from [Instacart's blog post](https://tech.instacart.com/3-million-instacart-orders-open-sourced-d40d29ead6f2), showing "Number of Purchases" vs "Percent Reorder Purchases"
# - Get the most recent order for each user in Instacart's dataset. This is a useful baseline when [predicting a user's next order](https://www.kaggle.com/c/instacart-market-basket-analysis)
# - Replicate parts of the blog post linked at the top of this notebook: [Modern Pandas, Part 5: Tidy Data](https://tomaugspurger.github.io/modern-5-tidy.html)

#%%
recent_orders = orders.sort_values('order_id', ascending=False).groupby(['user_id']).first().reset_index()
# Reset the index so we can preserve user_id post-merge

recent_orders_products = pandas.merge(recent_orders,
									pandas.merge(order_products,
												products,
												on='product_id'
												),
									on='order_id'
									)

recent_orders_products.head(20)

