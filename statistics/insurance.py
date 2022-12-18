import pandas as pd 
### RECOMMENDATIONS:
### - Separate words in variables with underscores, e.g. rawdata -> raw_data


#This project is an exercise in performing basic data analysis of spreadsheet data.

#import data
rawdata = pd.read_csv('insurance.csv')

#select all the men
men = rawdata.loc[rawdata['sex'] == 'male']

#select only the number of children for each man
menchildren = men['children']

#####Task One: finding the probability of picking a man that has exactly 2 children from the list

#use conditional probability formula
#first find probability of picking man from list
manprob = len(men)/len(rawdata)
#then find prob of a man on the list having 2 kids
twokidprob = len(men[men['children'] == 2]) / len(rawdata)
#use complete formula
mantwokidprob = twokidprob/manprob
twokidrounded = round(mantwokidprob, 2)
print(twokidrounded)
#probability = 18%

#####Task Two: break down regions into percentages

def regionpercentage(region):
    area = rawdata.loc[rawdata['region'] == region]
    portion = round(len(area)/len(rawdata), 2)
    return portion

#southwest region = 24%
print(regionpercentage('southwest'))

#southeast region = 27%
print(regionpercentage('southeast'))

#northeast region = 24%
print(regionpercentage('northeast'))

#northwest region = 24%
print(regionpercentage('northwest'))

#####Task Three: Find age ranges percentages

#find min and max
print(rawdata.age.min())
print(rawdata.age.max())

#create function for finding percentage
def agerange(low, high):
    agelist = rawdata.loc[(rawdata.age >= low) & (rawdata.age <= high)]
    portion = round(len(agelist)/len(rawdata), 2)
    return portion
#Range 18 - 30
print(agerange(18,30))
#Range 31 - 50
print(agerange(31,50))
# Range 51+
print(agerange(51,99))

#####Task Four: Gather basic stats data of each category

#create function to calculate stats and format the data
def statsdata(category):
    mode = rawdata[category].mode()
    median = rawdata[category].median()
    min = rawdata[category].min()
    max = rawdata[category].max()
    std = rawdata[category].std()
    ### Change each line to something closer to this:
    ### f"{category.upper()} information\n"
    return ("{} information".format(category).upper() + "\n"
    "----------------------" + "\n"
    "Mode: {}".format(mode[0]) + "\n" 
    "Median: {}".format(median) + "\n"
    "Min: {}".format(min) + "\n"
    "Max: {}".format(max) + "\n"
    "Std: {}".format(std) + "\n"
    "----------------------")
#print the data for numerical categories
print(statsdata('age'))
print(statsdata('bmi'))
print(statsdata('children'))
print(statsdata('charges'))


