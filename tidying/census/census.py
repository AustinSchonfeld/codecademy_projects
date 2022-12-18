import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import glob

#create a list of all the file names
files = glob.glob('states*.csv')

#create an empty list to add CSV data to
df_list = []
#loop through the files and read the data into a list
for filename in files:
    data = pd.read_csv(filename)
    df_list.append(data)
#put the list together into a dataframe
all_data = pd.concat(df_list)

#look at data types and column names to determine if changes need to be made
print(all_data.columns)
print(all_data.dtypes)
#print(all_data)

#there's an unecessary column, drop it
all_data = all_data.drop(columns = 'Unnamed: 0')

#use regex to remove dollar sign from Income and then convert it to float
all_data.Income = all_data.Income.replace(['\$|,'], '', regex = True)
all_data.Income = pd.to_numeric(all_data.Income)

#genderpop needs to be split into male and female populations as numerical values
string_split = all_data.GenderPop.str.split('_')
ManPop = string_split.str[0]
ManPop = ManPop.str.replace('M', '')
ManPop = pd.to_numeric(ManPop)
all_data['Male_Population'] = np.int64(ManPop)

FemPop = string_split.str[1]
FemPop = FemPop.str.replace('F', '')
FemPop = pd.to_numeric(FemPop)
#FemPop has some NaN values that are causing problems, replace them with an estimated value
FemPop = FemPop.fillna(all_data.TotalPop - ManPop)
all_data['Female_Population'] = np.int64(FemPop)

#check new columns
print(all_data.head())
print(all_data.dtypes)

#drop GenderPop column as its no longer needed for this
all_data = all_data.drop(columns = 'GenderPop')

#check for duplicates
print(all_data.duplicated())
#drop duplicates and check again
all_data = all_data.drop_duplicates()
print(all_data.duplicated())

#compare % female pop with average income using a scatterplot
plt.scatter((all_data.Female_Population/all_data.TotalPop), all_data.Income)
plt.savefig('Women_vs_Income.png')
plt.clf()

#convert race data into numerical data using a function
def Remove_Percent(race):
    all_data[race] = all_data[race].str.replace('%', '')
    all_data[race] = pd.to_numeric(all_data[race])

Remove_Percent('Hispanic')
Remove_Percent('White')
Remove_Percent('Black')
Remove_Percent('Native')
Remove_Percent('Asian')
Remove_Percent('Pacific')

#convert NaN values in Pacific pop
other = all_data.Hispanic + all_data.White + all_data.Black + all_data.Native + all_data.Asian
all_data.Pacific = all_data.Pacific.fillna(100 - other)

#make graphs for each set of race data using a function
def Make_Hist(race):
    sns.histplot(data = all_data, x = race)
    plt.savefig(race+'.png')
    plt.clf()

#double check data one more time in full and make histograms
print(all_data)
Make_Hist('Hispanic')
Make_Hist('White')
Make_Hist('Black')
Make_Hist('Native')
Make_Hist('Asian')
Make_Hist('Pacific')

#graphs need titles, labels, and some fine tuning to make them more appealing but the data is correct 
