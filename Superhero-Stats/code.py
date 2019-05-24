# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data=pd.read_csv(path)
print(data.head(3))

data['Gender'].replace({'-':['Agender']},inplace=True)
gender_count=data['Gender'].value_counts()
gender_count.plot(kind='bar', title="Gender Count")
#Code starts here 




# --------------
#Code starts here
alignment=data['Alignment'].value_counts()
alignment.plot.pie(labels='Character Alignment')


# --------------
#Code starts here
print(data.head())
sc_df=data[['Strength','Combat']]
sc_covariance=sc_df.cov().iloc[0,1]
sc_strength=sc_df['Strength'].std()
sc_combat=sc_df['Combat'].std()
sc_pearson=sc_covariance/(sc_strength*sc_combat).round(2)
print("Pearson value between strength and combat:\n",sc_pearson)

ic_df=data[['Intelligence','Combat']]
ic_covariance=ic_df.cov().iloc[0,1]
ic_intelligence=ic_df['Intelligence'].std()
ic_combat=ic_df['Combat'].std()
ic_pearson=ic_covariance/(ic_intelligence*ic_combat).round(2)
print("Pearson value between intelligence and combat:\n",ic_pearson)


# --------------
#Code starts here
import numpy as np
total_high=data['Total'].quantile(0.99)
super_best=data.loc[(data.Total>total_high)]

super_best_names=super_best['Name'].values.tolist()
#article_read[article_read.country == 'country_2'].groupby(['source', 'topic']).count()

#DataFrame.where(cond, other=nan, inplace=False, axis=None, level=None, errors='raise', try_cast=False, raise_on_error=None
print(total_high)
#print(super_best)
print(super_best_names)
#df.loc[(df.Product == p_id) & (df.Time >= start_time) & (df.Time < end_time)


# --------------
#Code starts here
import matplotlib.pyplot as plt 
#fig, (ax_1, ax_2, ax_3) = plt.subplots(1,2,3, figsize=(20,10))
fig, (ax_1,ax_2,ax_3) = plt.subplots(3,figsize=(20,10))
ax_1.boxplot(super_best['Intelligence'])
ax_1.set_title('Intelligence')
ax_2.boxplot(super_best['Speed'])
ax_2.set_title('Speed')
ax_3.boxplot(super_best['Power'])
ax_3.set_title('Power')


