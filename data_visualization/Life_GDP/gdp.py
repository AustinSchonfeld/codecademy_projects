import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#import data
data = pd.read_csv('all_data.csv')
print(data.head())

#clean and tidy data
data.rename(columns = {'Life expectancy at birth (years)':'Life_Expectancy'}, inplace = True)
data.GDP = round(data.GDP / 1000000000, 2)

#check data types and confirm that changes were made
print(data.head())
print(data.dtypes)

#create new data with life expectancy averages
average_life = data.groupby(['Country']).mean().reset_index()
average_life = average_life[['Country','Life_Expectancy']]
#plot the data
Countries = ['Zimbabwe', 'China', 'Mexico', 'USA', 'Chile', 'Germany']
sns.barplot(data = average_life, x = 'Country', y = 'Life_Expectancy', order = average_life.sort_values('Life_Expectancy').Country)
plt.xticks(rotation = 45, labels = Countries, ticks = range(len(Countries)))
plt.tight_layout()
plt.savefig('Life_Bar.png')
plt.clf()

#plot each country's life expectancy over time
sns.lineplot(data = data, x = 'Year', y = 'Life_Expectancy', hue = 'Country')
plt.savefig('life_over_time.png')
plt.clf()
#life expectancy over time doesn't say much, let's plot life vs GDP
sns.scatterplot(data = data, x = 'Life_Expectancy', y = 'GDP', hue = 'Country')
plt.savefig('Life_vs_GDP.png')
plt.clf()

#this is a test comment