import scipy.stats as stats
import numpy as np

#This project is an exercise in performing probability calculations given a number of expect product defects on any given day

###Task 1: expected product defects = 7
lam = 7

###Task 2: what is the probability of having exactly 7 defects in a day
print(stats.poisson.pmf(lam, lam))

###Task 3: What is the probability of having 4 or fewer defects in a day
print(stats.poisson.cdf(4, lam))

###Task 4: What is the probability of having more than 9 defects in a day
print(1 - stats.poisson.cdf(9, lam))

###Task 5: create a variable that represents 365 random days of defects
annualdefects = stats.poisson.rvs(lam, size = 365)
print(annualdefects[0:20])

###Task 6: What is the expected number of defects in a year?
print(7*365)

###Task 7: Show the total number of defects in a year from the random set 
print(sum(annualdefects))

#Task 8: Calculate avg defects per day from the random set
print(sum(annualdefects)/len(annualdefects))

#Task 9: Find the max value in the random set
print(annualdefects.max())

#Task 10: Find the probability of having a day with max defects or more
print(1 - stats.poisson.cdf(annualdefects.max(), lam))