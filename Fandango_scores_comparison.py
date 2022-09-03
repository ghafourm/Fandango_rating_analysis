#!/usr/bin/env python
# coding: utf-8

# # <b>Investigating Fandango Movie Ratings</b><br/>
# 
# In this project we will study movie ratings in Fandango's web site rating sytem.<br/>
# We would like to check if rating in this website is biased and the movies are over rated

# In[36]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

fandango_compare = pd.read_csv('fandango_score_comparison.csv')
movie_ratings_1617 = pd.read_csv('movie_ratings_16_17.csv')


# In[37]:


fandango_compare.info()
movie_ratings_1617.info()


# # Equal chance for all movies?

# Movies having less than 30 fan reviews on Fandango or without tickets on sale <br/> were not included in the samples. Therefore all movies do not have equal chance to <br/> be included in the study.

# # The difference between Fandango and the other movie rating sites

# Since we are dealing with dataframes containing data from several rating <br/>
# site, we can compare these data to have a better idea about the difference <br/>
# between Fandango and other sites.

# In[38]:


# We can use describe() to have a first look
fandango_compare['Fandango_Ratingvalue'].describe()


# In[39]:


fandango_compare['RT_user_norm'].describe()


# In[40]:


fandango_compare['IMDB_norm'].describe()


# In[41]:


fandango_compare['Metacritic_user_nom'].describe()


# In[42]:


# We can also use grouped frequency tables to have a better idea about diffrences 
# between Fandango and the other rating sites

rate_interval = pd.interval_range(start=0, end=5, freq=0.5)
Fandango_freq_table = fandango_compare['Fandango_Ratingvalue'].value_counts(bins=rate_interval).sort_index()
Fandango_freq_table


# In[43]:


# Metacritics frequency table
Metacritics_freq_table = fandango_compare['Metacritic_user_nom'].value_counts(bins=rate_interval).sort_index()
Metacritics_freq_table


# In[44]:


# Imdb frequency table 
Imdb_freq_table = fandango_compare['IMDB_norm'].value_counts(bins=rate_interval).sort_index()
Imdb_freq_table


# In[45]:


# Rotten Tomatoes frequency table 
RT_freq_table = fandango_compare['RT_norm_round'].value_counts(bins=rate_interval).sort_index()
RT_freq_table


# These data show that only 13 movies are rated 3 and less in Fandango while the number of movies with rating inferior or equal to 3 are 30, 46 and 74 for imdb, metacritics and RT, respectively.

# In[46]:


#We are going to visualize the difference between Fandango and the other rating
# sites using histograms 
plt.subplot(3,1,1)
fandango_compare['Fandango_Ratingvalue'].plot.hist(histtype='step', label = 'Fandango', legend = True)
fandango_compare['RT_user_norm'].plot.hist(histtype='step', label = 'RT', legend = True, figsize=(10,7))
plt.ylim(0,40)
plt.title('Fandango ratings vs other rating sites')
plt.subplot(3,1,2) 
fandango_compare['Fandango_Ratingvalue'].plot.hist(histtype='step', label = 'Fandango', legend = True)
fandango_compare['Metacritic_user_nom'].plot.hist(histtype='step', label = 'Metacritic', legend = True, figsize=(10,7))
plt.ylim(0,40)
plt.subplot(3,1,3)
fandango_compare['Fandango_Ratingvalue'].plot.hist(histtype='step', label = 'Fandango', legend = True, figsize=(10,7))
fandango_compare['IMDB_norm'].plot.hist(histtype='step', label = 'Imdb', legend = True)
plt.ylim(0,40)
plt.xlabel('rating')
#plt.title('Fandango vs IMDB User Rating ')
plt.subplots_adjust(hspace=0.7)
plt.show()


# * These plot shows a clear difference between user user votes in Fandango and the other movie rating sites. Fandango's rating are higher than the other sites.<br/>
# * Since we analysed the user rating, these data show that the difference in rating existed between Fandango and other rating sites before the rounding operation.

#  # Checking the changes in Fandango's rating in 2016

# In[47]:


# First We are going to idolate movies released in 2015 and 2016.
# We are going to extract the year of release and create the 'year' column
fandango_compare['year'] = fandango_compare['FILM'].apply(lambda x: int(x.split("(")[1].replace(")","")))
fandango_compare.info()


# In[48]:


#We are going to isolate movies released in 2015
fandango_compare_2015 = fandango_compare[fandango_compare['year'] == 2015]
#We are going to isolate movies released in 2016
fandango_compare_2016 = movie_ratings_1617[movie_ratings_1617['year']==2016]


# In[49]:


# We use grouped frequency tables to see the diffrences between fandango ratings
# in 2015 and 2016
fandango_2015=fandango_compare_2015['Fandango_Ratingvalue'].value_counts(bins = rate_interval).sort_index()
fandango_2015


# In[50]:


fandango_2016 = fandango_compare_2016['fandango'].value_counts(bins=rate_interval).sort_index()
fandango_2016


# * By looking at the frequency table we can observe an increase in the number of movies <br/> 
# with ratings of 3 and less.<br/>
# * Another noticableble change in the decrease in the number of movies rated higher than 4.5. <br/> 
# * However to check if Fandango ratings in 2016 has significantly changed we can compare it to ratings from other sites.

# In[51]:


# Let's calculate frequency tables for other sites rating in 2016
# metacritics frequency table
metascore_2016 = fandango_compare_2016['n_metascore'].value_counts(bins=rate_interval).sort_index()
metascore_2016


# In[52]:


#imdb frequency table
imdb_2016 = fandango_compare_2016['n_imdb'].value_counts(bins=rate_interval).sort_index()
imdb_2016


# In[53]:


#tomatometer frequency table
tmeter_2016 = fandango_compare_2016['n_tmeter'].value_counts(bins=rate_interval).sort_index()
tmeter_2016


# These data shows that there are still differences between fandango ratings and <br/>
# and other sites ratings.<br/>
# To confirm that we can use box plot to compare different site ratings.

# In[54]:


# We are isolating user rating data rfom fandango, metacritics, imdb and tomatometer
# We use these data to create a boxplot
compare_16_user_rating = fandango_compare_2016[['fandango','n_metascore','n_imdb','n_tmeter']]
compare_16_user_rating.boxplot()
plt.title('Movies rating 2016')
plt.ylabel('user score')
plt.show()


# This plot shows that in 2016 user rating in fandango are higher than the other sites.

# # Rating of popular movies at Fandango in 2015 and 2016

# In[55]:


# We are going to use kernel density plot to compare Fandango movie rating in 
# 2015 and 2016
fandango_compare_2015['Fandango_Ratingvalue'].plot.kde(label='2015', legend=True)
fandango_compare_2016['fandango'].plot.kde(label='2016', legend=True)
plt.style.use('fivethirtyeight')
plt.xlim(0, 5)
plt.xticks([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
plt.xlabel('rating')
plt.title("Changes in fandango ratings")
plt.show()


# This figure shows that ratings in 2016 have changed and were slightly lower 
# than 2015.<br/>
# These changes confirm the previous observations we had by analysing frequency tables.<br/>
# We can look at some statistical parameter to confim these changes.

# In[56]:


fandango_compare_2015['Fandango_Ratingvalue'].describe()


# In[57]:


fandango_compare_2016['fandango'].describe()


# According to these data there is no significant difference between Fandango ratings <br/>
# in 2015 and 2016. We can verify that by plotting the mean, median and mode of these data.

# In[58]:


#We calculate the mode for 2016
fandango_compare_2016['fandango'].mode()


# In[59]:


#We calculate the mode for 2015
fandango_compare_2015['Fandango_Ratingvalue'].mode()


# In[60]:


fandango_stat = pd.DataFrame({'Fandango user rating statistics': ['mean', 'median', 'mode'],
                             '2016':[fandango_compare_2016['fandango'].mean(), fandango_compare_2016['fandango'].median(), 4.0],
                             '2015':[fandango_compare_2015['Fandango_Ratingvalue'].mean(), fandango_compare_2015['Fandango_Ratingvalue'].median(), 4.1]})
fandango_stat


# In[61]:


fandango_stat.plot(x="Fandango user rating statistics", y=["2015", "2016"], kind="bar")
plt.ylim(0,5)
plt.yticks([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
plt.ylabel('stars')
plt.show()


# This plot does not show significant difference between 2015 and 2016 data. <br/>
# Based on that and our previous observations we can state that there is no significant <br/>
# difference in Fandango user rating between 2015 and 2016.

# In[ ]:




