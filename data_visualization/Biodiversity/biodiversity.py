import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

#import the data from two spreadsheets
observations = pd.read_csv('observations.csv')
species = pd.read_csv('species_info.csv')

#check out the data format and info
print(observations.head())
print(species.head())
print(len(observations))
print(len(species))
#all species on the list are present in all 4 parks, but the # of observations are different for each park

#get a list of the park names included in the data
print(observations.park_name.unique())

#drop duplicates
species.drop_duplicates(subset = ['scientific_name'])
observations.drop_duplicates(subset = ['park_name'])

###TASK 1: Create a chart that shows # of unique species per category
#value_counts counts the occurrences of each unique value in a column
category_series = species.category.value_counts()
#to graph the category counts, the indexes and values need to be split
categories = category_series.index
category_counts = category_series.values
categories = categories.tolist()
category_counts = category_counts.tolist()
#graph the data
plt.bar(categories, category_counts, color = 'green')
plt.xticks(rotation = 90)
plt.title('Number of Species in each Category of Plant/Animal')
plt.ylabel('Number of Species')
plt.xlabel('Category')
plt.tight_layout(h_pad = 2)
plt.savefig('category_counts.png')
plt.clf()
#drop plants from the lists
categories.remove('Nonvascular Plant')
categories.remove('Vascular Plant')
category_counts.remove(4470)
category_counts.remove(333)
#plants skew the graph quite a bit, lets do animals only
plt.bar(categories, category_counts, color = ['green', 'blue', 'orange', 'red', 'purple'])
plt.xticks(rotation = 90)
plt.title('Number of Species in each Category of Animal')
plt.ylabel('Number of Species')
plt.xlabel('Category')
plt.tight_layout(h_pad = 2)
plt.savefig('animal_category_counts.png')
plt.clf()

###TASK 2: Create a chart showing the conservation status of each category
#first the NaN values have to be replaced
species.conservation_status.fillna('No Intervention', inplace = True)
#create a new table showing conservation status by category
conservation_status = species.groupby(['category','conservation_status']).scientific_name.count().unstack()
conservation_status.fillna(0, inplace = True)
#reorder the columns by level of concern and drop "no intervention" column
conservation_status = conservation_status[['In Recovery', 'Species of Concern', 'Threatened', 'Endangered']]
print(conservation_status)
#make a graph showing the conservation status vs category
sns.set_context('poster')
sns.set_style('darkgrid')
sns.set_palette('bright')
ax = conservation_status.plot(kind = 'barh', figsize = (15,10), stacked = True)
plt.title('Conservation Status by Category')
plt.xlabel('Number of Species')
plt.ylabel('Species Category')
plt.legend(title = 'Conservation Status')
plt.tight_layout()
plt.savefig('status_category.png')
plt.clf()
