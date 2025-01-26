#!/usr/bin/env python
# coding: utf-8

# # Welcome to Covid19 Data Analysis Notebook
# ------------------------------------------

# ### Let's Import the modules 

# In[1]:


import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
print('Modules are imported.')


# ## Task 2 

# ### Task 2.1: importing covid19 dataset
# importing "Covid19_Confirmed_dataset.csv" from "./Dataset" folder. 
# 

# In[4]:


corona_dataset=pd.read_csv("Datasets/covid19_Confirmed_dataset.csv")
corona_dataset.head(5)


# #### Let's check the shape of the dataframe

# In[5]:


corona_dataset.shape


# ### Task 2.2: Delete the useless columns

# In[12]:


corona_dataset.drop(["Lat","Long"],axis=1,inplace=True)


# In[13]:


corona_dataset.head(5)


# ### Task 2.3: Aggregating the rows by the country

# In[14]:


corona_dataset_agg=corona_dataset.groupby("Country/Region").sum()


# In[16]:


corona_dataset_agg.head(5)


# In[17]:


corona_dataset_agg.shape


# ### Task 2.4: Visualizing data related to a country for example China
# visualization always helps for better understanding of our data.

# In[21]:


corona_dataset_agg.loc['China'].plot()
corona_dataset_agg.loc['Italy'].plot()
corona_dataset_agg.loc['Spain'].plot()
plt.legend()


# ### Task3: Calculating a good measure 
# we need to find a good measure reperestend as a number, describing the spread of the virus in a country. 

# In[22]:


corona_dataset_agg.loc['China'].plot()


# In[23]:


corona_dataset_agg.loc['China'][:3].plot()


# ### task 3.1: caculating the first derivative of the curve

# In[25]:


corona_dataset_agg.loc['China'].diff().plot()


# ### task 3.2: find maxmimum infection rate for China

# In[26]:


corona_dataset_agg.loc['China'].diff().max()


# In[27]:


corona_dataset_agg.loc['Italy'].diff().max()


# In[28]:


corona_dataset_agg.loc['Spain'].diff().max()


# ### Task 3.3: find maximum infection rate for all of the countries. 

# In[32]:


countries=list(corona_dataset_agg.index)
rates=[]
for c in countries:
    rates.append(corona_dataset_agg.loc[c].diff().max())
corona_dataset_agg["max_inflection_rates"]=rates


# In[33]:


corona_dataset_agg.head(5)


# ### Task 3.4: create a new dataframe with only needed column 

# In[36]:


new_df=pd.DataFrame(corona_dataset_agg["max_inflection_rates"])


# In[37]:


new_df.head(5)


# ### Task4: 
# - Importing the WorldHappinessReport.csv dataset
# - selecting needed columns for our analysis 
# - join the datasets 
# - calculate the correlations as the result of our analysis

# ### Task 4.1 : importing the dataset

# In[53]:


happiness_dff=pd.read_csv("Datasets/worldwide_happiness_report.csv")


# In[54]:


happiness_dff.head(5)


# ### Task 4.2: let's drop the useless columns 

# In[55]:


useless_cols=["Overall rank","Score","Generosity","Perceptions of corruption"]


# In[57]:


print(happiness_dff.columns)


# In[58]:


happiness_dff.drop(["Overall rank", "Score", "Generosity", "Perceptions of corruption"], axis=1, inplace=True, errors='ignore')


# In[59]:


happiness_dff.head(5)


# ### Task 4.3: changing the indices of the dataframe

# In[60]:


happiness_dff.set_index(["Country or region"],inplace=True)


# In[61]:


happiness_dff.head()


# ### Task4.4: now let's join two dataset we have prepared  

# #### Corona Dataset :

# In[62]:


new_df.head(5)


# In[63]:


new_df.shape


# #### wolrd happiness report Dataset :

# In[64]:


happiness_dff.head()


# In[65]:


happiness_dff.shape


# In[66]:


data=new_df.join(happiness_dff,how="inner")
data.head(5)


# ### Task 4.5: correlation matrix 

# In[67]:


data.corr()


# ### Task 5: Visualization of the results
# our Analysis is not finished unless we visualize the results in terms figures and graphs so that everyone can understand what you get out of our analysis

# In[68]:


data.head()


# ### Task 5.1: Plotting GDP vs maximum Infection rate

# In[70]:


x=data["GDP per capita"]
y=data["max_inflection_rates"]
sns.scatterplot(x=x,y=y)


# In[72]:


sns.regplot(x=x,y=np.log(y))


# ### Task 5.2: Plotting Social support vs maximum Infection rate

# In[73]:


x=data["Social support"]
y=data["max_inflection_rates"]
sns.scatterplot(x=x,y=y)


# In[74]:


sns.regplot(x=x,y=np.log(y))


# ### Task 5.3: Plotting Healthy life expectancy vs maximum Infection rate

# In[75]:


x=data["Healthy life expectancy"]
y=data["max_inflection_rates"]
sns.scatterplot(x=x,y=y)


# In[76]:


sns.regplot(x=x,y=np.log(y))


# ### Task 5.4: Plotting Freedom to make life choices vs maximum Infection rate

# In[77]:


x=data["Freedom to make life choices"]
y=data["max_inflection_rates"]
sns.scatterplot(x=x,y=y)


# In[78]:


sns.regplot(x=x,y=np.log(y))


# In[ ]:




