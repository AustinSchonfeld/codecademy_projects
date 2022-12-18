import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt

#import data
flight = pd.read_csv("flight.csv")
print(flight.head())

#find high, low, and mean coach prices
highcoach = flight.coach_price.max()
lowcoach = flight.coach_price.min()
avgcoach = flight.coach_price.mean()

#find high, low, and mean coach prices for 8 hr flights
high8hr = flight.coach_price[flight.hours == 8].max()
low8hr = flight.coach_price[flight.hours == 8].min()
mean8hr = flight.coach_price[flight.hours == 8].mean()

#plot the 8hr coach prices
sns.histplot(flight.coach_price[flight.hours == 8])
plt.xlabel('Cost')
plt.title('Cost of Coach for 8 Hr Flights')
plt.savefig('8hr_coach_prices.png')
plt.clf()

#plot delay frequencies
sns.histplot(flight.delay[flight.delay <= 60])
plt.savefig('delay_frequencies')
plt.clf()

#compare coach and first class prices using a small subset of the data

sns.lmplot(data = flight.sample(frac=0.01, replace = True, random_state = 1), x = "coach_price", y = "firstclass_price", lowess = True)
plt.savefig('coach_vs_first.png')
plt.clf()

#find the relationship between coach prices and inflight features, which features are associated with increases in price?
#This will require 3 different histograms

sns.histplot(data = flight, x = flight.coach_price, hue = flight.inflight_meal)
plt.savefig('inflight_meal_hist.png')
plt.clf()

sns.histplot(data = flight, x = flight.coach_price, hue = flight.inflight_entertainment)
plt.savefig('inflight_entertainment_hist.png')
plt.clf()

sns.histplot(data = flight, x = flight.coach_price, hue = flight.inflight_wifi)
plt.savefig('inflight_wifi_hist.png')
plt.clf()

#what is the relationship between passengers and flight length

sns.stripplot(data = flight.sample(frac=0.05, replace = True, random_state = 1), y = 'passengers', x = 'hours')
plt.savefig('passengers_vs_hours.png')
plt.clf()

#what is the difference between coach and first class on weekends compared to weekdays

sns.scatterplot(data = flight.sample(frac=0.01, replace = True, random_state = 1), x = "coach_price", y = "firstclass_price", hue = 'weekend')
plt.title('Ticket Prices on Weekdays vs Weekends')
plt.xlabel('Coach Prices')
plt.ylabel('First Class Prices')
plt.savefig('weekday_vs_weekend.png', bbox_inches = 'tight')
plt.clf()