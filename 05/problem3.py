import math as m
import numpy as np
import scipy.stats as stats

#import or paste dataset here
data = np.array([135, 140, 130, 145, 150, 138, 142, 137, 136, 148, 141, 139, 143, 147, 149, 134, 133, 146, 144, 132])


# code for Question 1
print('Problem 1 Answers:')
# code below this line

#construct 90% confidence interval for the data. report the sample mean, standard error, standard statistic, and confidence interval
n = len(data)
alpha = 0.10 #significance level
confidence = 0.90

avg = np.mean(data)
std = np.std(data, ddof=1) #compute standard deviation
se = std / m.sqrt(n) #compute standard error
t = stats.t.ppf(1 - alpha / 2, df=n-1) # compute t-score
ci = stats.t.interval(confidence, df=n-1, loc=avg, scale=se) # compute confidence interval
ci = float(ci[0]), float(ci[1]) # convert to float

print('Sample mean:', avg)
print('Sample standard deviation:', std)
print('Standard error:', se)
print('')
print('data for confidence interval:', confidence)
print('Standard statistic (t):', t)
print('Confidence interval:', ci)


print('')
# code for Question 2
print('Problem 2 Answers:')
# code below this line

#construct 95% confidence interval for the data. report the sample mean, standard error, standard statistic, and confidence interval
alpha = 0.05 #significance level
confidence = 0.95

t = stats.t.ppf(1 - alpha / 2, df=n-1) # ompute t-score
ci = stats.t.interval(confidence, df=n-1, loc=avg, scale=se) #compute confidence interval
ci = float(ci[0]), float(ci[1]) #convert to float

print('Sample mean:', avg)
print('Sample standard deviation:', std)
print('Standard error:', se)
print('')
print('data for confidence interval:', confidence)
print('Standard statistic (t):', t)
print('Confidence interval:', ci)


print('')
# code for Question 3
print('Problem 3 Answers:')
# code below this line

#repeat question 2 but with a population standard deviation of 5
std = 5 #population standard deviation that is known
se = std / m.sqrt(n) #compute standard error
z = stats.norm.ppf(1 - alpha / 2) #compute z-score

#compute confidence interval
ci = stats.norm.interval(confidence, loc=avg, scale=se)
ci = float(ci[0]), float(ci[1])  #convert to float

print('Sample mean:', avg)
print('Sample standard deviation:', std)
print('Standard error:', se)
print('')
print('data for confidence interval:', confidence)
print('Standard statistic (z):', z)
print('Confidence interval:', ci)