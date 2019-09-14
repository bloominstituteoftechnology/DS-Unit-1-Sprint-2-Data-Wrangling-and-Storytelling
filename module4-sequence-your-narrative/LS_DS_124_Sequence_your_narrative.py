#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'module4-sequence-your-narrative'))
	#print(os.getcwd())
except:
	pass
#%% [markdown]

#%% [markdown]
# _Lambda School Data Science_
# 
# # Sequence your narrative
# 
# Today we will create a sequence of visualizations inspired by [Hans Rosling's 200 Countries, 200 Years, 4 Minutes](https://www.youtube.com/watch?v=jbkSRLYSojo).
# 
# Using this [data from Gapminder](https://github.com/open-numbers/ddf--gapminder--systema_globalis/):
# - [Income Per Person (GDP Per Capital, Inflation Adjusted) by Geo & Time](https://raw.githubusercontent.com/open-numbers/ddf--gapminder--systema_globalis/master/ddf--datapoints--income_per_person_gdppercapita_ppp_inflation_adjusted--by--geo--time.csv)
# - [Life Expectancy (in Years) by Geo & Time](https://raw.githubusercontent.com/open-numbers/ddf--gapminder--systema_globalis/master/ddf--datapoints--life_expectancy_years--by--geo--time.csv)
# - [Population Totals, by Geo & Time](https://raw.githubusercontent.com/open-numbers/ddf--gapminder--systema_globalis/master/ddf--datapoints--population_total--by--geo--time.csv)
# - [Entities](https://raw.githubusercontent.com/open-numbers/ddf--gapminder--systema_globalis/master/ddf--entities--geo--country.csv)
# - [Concepts](https://raw.githubusercontent.com/open-numbers/ddf--gapminder--systema_globalis/master/ddf--concepts.csv)
#%% [markdown]
# Objectives
# - sequence multiple visualizations
# - combine qualitative anecdotes with quantitative aggregates
# 
# Links
# - [Hans Rosling’s TED talks](https://www.ted.com/speakers/hans_rosling)
# - [Spiralling global temperatures from 1850-2016](https://twitter.com/ed_hawkins/status/729753441459945474)
# - "[The Pudding](https://pudding.cool/) explains ideas debated in culture with visual essays."
# - [A Data Point Walks Into a Bar](https://lisacharlotterost.github.io/2016/12/27/datapoint-in-bar/): a thoughtful blog post about emotion and empathy in data storytelling
#%% [markdown]
# ## Make a plan
# 
# #### How to present the data?
# 
# Variables --> Visual Encodings
# - Income --> x
# - Lifespan --> y
# - Region --> color
# - Population --> size
# - Year --> animation frame (alternative: small multiple)
# - Country --> annotation
# 
# Qualitative --> Verbal
# - Editorial / contextual explanation --> audio narration (alternative: text)
# 
# 
# #### How to structure the data?
# 
# | Year | Country | Region   | Income | Lifespan | Population |
# |------|---------|----------|--------|----------|------------|
# | 1818 | USA     | Americas | ###    | ##       | #          |
# | 1918 | USA     | Americas | ####   | ###      | ##         |
# | 2018 | USA     | Americas | #####  | ###      | ###        |
# | 1818 | China   | Asia     | #      | #        | #          |
# | 1918 | China   | Asia     | ##     | ##       | ###        |
# | 2018 | China   | Asia     | ###    | ###      | #####      |
# 
#%% [markdown]
# ## Upgrade Seaborn
# 
# Make sure you have at least version 0.9.0.
# 
# In Colab, go to **Restart runtime** after you run the `pip` command.

#%%
get_ipython().system('pip install --upgrade seaborn')


#%%
import seaborn as sns
sns.__version__

#%% [markdown]
# ## More imports

#%%
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#%% [markdown]
# ## Load & look at data

#%%
income = pd.read_csv('https://raw.githubusercontent.com/open-numbers/ddf--gapminder--systema_globalis/master/ddf--datapoints--income_per_person_gdppercapita_ppp_inflation_adjusted--by--geo--time.csv')


#%%
lifespan = pd.read_csv('https://raw.githubusercontent.com/open-numbers/ddf--gapminder--systema_globalis/master/ddf--datapoints--life_expectancy_years--by--geo--time.csv')


#%%
population = pd.read_csv('https://raw.githubusercontent.com/open-numbers/ddf--gapminder--systema_globalis/master/ddf--datapoints--population_total--by--geo--time.csv')


#%%
entities = pd.read_csv('https://raw.githubusercontent.com/open-numbers/ddf--gapminder--systema_globalis/master/ddf--entities--geo--country.csv')


#%%
concepts = pd.read_csv('https://raw.githubusercontent.com/open-numbers/ddf--gapminder--systema_globalis/master/ddf--concepts.csv')


#%%
income.shape, lifespan.shape, population.shape, entities.shape, concepts.shape


#%%
income.head()


#%%
lifespan.head()


#%%
population.head()


#%%
pd.options.display.max_columns = 500
entities.head()


#%%
concepts.head()

#%% [markdown]
# ## Merge data
#%% [markdown]
# https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf

#%%


#%% [markdown]
# ## Explore data

#%%


#%% [markdown]
# ## Plot visualization

#%%


#%% [markdown]
# ## Analyze outliers

#%%


#%% [markdown]
# ## Plot multiple years

#%%


#%% [markdown]
# ## Point out a story

#%%



