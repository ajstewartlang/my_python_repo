#!/usr/bin/env python
# coding: utf-8

# The following will be a group-based activity which you will do in class.
# 
# The data in the file https://raw.githubusercontent.com/ajstewartlang/02_intro_to_python_programming/main/data/ANOVA_class_work.csv are from an experiment with 96 participants. We measured how quickly (in milliseconds) people could pronounce a word that was presented to them. Words were presented either normally (Condition A) or were visually degraded (Condition B). This was a between participants factor of visual quality with 2 levels. Visualise the data and report the key descriptives before then running the appropriate ANOVA.
# 
# Can you turn your code into a function called my_anova() so that you can call it with the command my_anova('https://raw.githubusercontent.com/ajstewartlang/02_intro_to_python_programming/main/data/ANOVA_class_work.csv') and will produce the output of your ANOVA? Hint: you need to pass just the location of your data file to your function, and can keep the code you’ve written above virtually unchanged.

# In[1]:


import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt


# In[2]:


my_data = pd.read_csv('https://raw.githubusercontent.com/ajstewartlang/02_intro_to_python_programming/main/data/ANOVA_class_work.csv')


# In[3]:


my_data.head()


# In[4]:


grouped_data = my_data.groupby(['condition'])
grouped_data.describe()['response_time']


# In[5]:


plt.plot(my_data['condition'], my_data['response_time'], 'bo')
plt.xlabel('Condition')
plt.ylabel('RT (ms.)')
plt.title('Reaction Time by Condition')
plt.xticks([0, 1], ['Normal', 'Degraded'], rotation=45)
plt.margins(.5, .5)
plt.show()


# How might you re-plot the above as a jittered or beeswarm plot?

# In[6]:


import seaborn as sns


# In[9]:


sns.set_theme(style='ticks', context='paper', font_scale=2)
sns.swarmplot(x='condition', y='response_time', data=my_data,size=10)
plt.xticks([0, 1], ['Normal', 'Degraded'], rotation=45)
plt.xlabel("Condition")
plt.ylabel("RT (ms.)")
plt.title("Reaction Time (ms.) by Condition")

plt.savefig("image1.png")

# If you're interested in finding out more about the seaborn library, you can read the paper introducing it [here](https://www.theoj.org/joss-papers/joss.03021/10.21105.joss.03021.pdf) and view the website which includes lots of examples and tutorials [here](https://seaborn.pydata.org/). 

# In[ ]:


my_std = grouped_data['response_time'].std()
my_means = grouped_data['response_time'].mean()
error = [my_std[0], my_std[1]]


# In[15]:


my_means.plot.bar(yerr=error, align='center', alpha=0.5, ecolor='black', capsize=10)
plt.ylabel('RT (ms.)')
plt.xlabel('Condition')
plt.xticks([0, 1], ['Normal', 'Degraded'], rotation=45)
plt.title('Mean Reaction Time and SDs by Condition')
plt.ylim((700, 1200))
plt.show()


# In[6]:


normal = my_data[my_data['condition']=='condition_a']['response_time']
degraded = my_data[my_data['condition']=='condition_b']['response_time']


# In[7]:


stats.f_oneway(normal, degraded)


# In[8]:


import pandas as pd
from scipy import stats

def my_anova(x):
    my_data = pd.read_csv(x)
    
    normal = my_data[my_data['condition']=='condition_a']['response_time']
    degraded = my_data[my_data['condition']=='condition_b']['response_time']
    
    return stats.f_oneway(normal, degraded)


# In[9]:


my_anova('https://raw.githubusercontent.com/ajstewartlang/02_intro_to_python_programming/main/data/ANOVA_class_work.csv')


# Our data file is called ANOVA_data2.csv and can be found here:
# 
# https://raw.githubusercontent.com/ajstewartlang/11_glm_anova_pt1/master/data/ANOVA_data2.csv
# 
# 48 participants responded to a word that differed in how frequent it was. This factor is between participants and we have four levels coded as ‘very low’, ‘low’, ‘high’, and ‘very high’. Our DV is reaction time and is coded as ‘RT’. Subject number is coded as ‘Subject’. We want to know if there is a difference between our conditions (and if so, where that difference lies). Calculate descriptive statistices and conduct the appropriate ANOVA.

# In[1]:


import pandas as pd
from scipy import stats


# In[2]:


def read_my_data(x):
    return pd.read_csv(x)


# In[3]:


data = read_my_data("https://raw.githubusercontent.com/ajstewartlang/11_glm_anova_pt1/master/data/ANOVA_data2.csv")


# In[4]:


very_low = data[data['Condition']=='very low']['RT']
low = data[data['Condition']=='low']['RT']
high = data[data['Condition']=='high']['RT']
very_high = data[data['Condition']=='very high']['RT']


# In[5]:


grouped_data = data.groupby(['Condition'])


# In[6]:


grouped_data.describe()['RT']


# In[37]:


stats.f_oneway(very_low, low, high, very_high)


# In[39]:


stats.ttest_ind(very_low, low)


# In[40]:


stats.ttest_ind(very_low, high)


# In[41]:


stats.ttest_ind(very_low, very_high)


# In[42]:


stats.ttest_ind(low, high)


# In[43]:


stats.ttest_ind(low, very_high)


# In[44]:


stats.ttest_ind(high, very_high)


# In[ ]:




