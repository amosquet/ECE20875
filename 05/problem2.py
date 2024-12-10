import numpy as np
import math as m
import scipy.stats as stats
from scipy.stats import norm
from scipy.stats import t
from scipy.stats import ttest_1samp


myFile = open('city_vehicle_survey.txt')
data1 = myFile.readlines()
data1 = [float(x) for x in data1]
myFile.close()


# # code for question 2
print('Problem 2 Answers:')
# # code below this line

H0 = 5 #null hypothesis
alpha1 = 0.05 #significance level 1
alpha2 = 0.1 #significance level 2

n = len(data1) #sample size. 10% condition is satisfied as n < 10% of the population, Central Limit Theorem is satisfied as n > 30
avg = np.mean(data1)
std = np.std(data1, ddof=1) #compute standard deviation
se = std / m.sqrt(n)

t_statistic, p_value = ttest_1samp(data1, H0) #one sample t-test for population mean, two-sided test (default)
# print(t_test.df) #printing degrees of freedom for debugging

#I have also included the code for z-test to prove that the results are the same as the sample size is large enough
# z = (H0 - avg) / se
# p_value =  2 * stats.norm.cdf(-abs(z))

# Print results
print(f"Sample size: {n}")
print(f"Sample mean: {avg:.4f}")
print(f"Standard error: {se:.4f}")
print(f"T-statistic: {t_statistic:.4f}")
# print(f"Z-statistic {z:.4f}")
print(f"P-value: {p_value:.4f}")

print('')
if p_value <= alpha1:
    print('Reject the null hypothesis at',alpha1,'significance level')
    print('The observed value is statistically significant')
else:
    print('Fail to reject the null hypothesis at',alpha1,'significance level')

if p_value <= alpha2:
    print('Reject the null hypothesis at',alpha2,'significance level')
    print('The observed value is statistically significant')
else:
    print('Fail to reject the null hypothesis at',alpha2,'significance level')


print('')
# code for question 3
print('Problem 3 Answers:')
# code below this line

alpha = 0.05
H0 = 5
H1 = 5.5
std = np.std(data1, ddof=1)
se3 = std / m.sqrt(n)
z_c = norm.ppf(1 - alpha / 2)
t_c = t.ppf(1 - alpha / 2, n - 1)

nMin = (std * z_c / (H1 - H0)) ** 2
nMin = m.ceil(nMin)
# print('Critical value:', z_c)

nMin = (std * t_c / (H1 - H0)) ** 2
nMin = m.ceil(nMin)

print('Standard Error:', se3)
print('Minimum sample size:', nMin)


print('')
# code for question 4 and 5
print('Problem 5 Answers:')
# code below this line

#(different sample sizes)
data2 = open('vehicle_data_1.txt') #Emission programs
data3 = open('vehicle_data_2.txt') #Without emission programs
data2 = data2.readlines()
data3 = data3.readlines()
data2 = [float(x) for x in data2]
data3 = [float(y) for y in data3]

#sample sizes
n1 = len(data2)
n2 = len(data3)

#sample means
avg1 = np.mean(data2)
avg2 = np.mean(data3)

#sample standard deviations
std1 = np.std(data2, ddof=1)
std2 = np.std(data3, ddof=1)

# Standard error
se = m.sqrt(std1**2/n1 + std2**2/n2)
# Z-score
z1 = (avg1 - avg2) / se
# P-value
p_value1 = 2 * stats.norm.cdf(-abs(z1))

# Significance levels
alpha1 = 0.05
alpha2 = 0.10

print('Emission Programs:')
print('Sample size:', n1)
print('Sample mean:', avg1)
print('')
print('Without Emission Programs:')
print('Sample size:', n2)
print('Sample mean:', avg2)

print('Standard error:', se)
print('Z-score:', z1)
print('P-value:', p_value1)

print('')
if p_value1 <= alpha1:
    print('Reject the null hypothesis at', alpha1, 'significance level')
    print('The observed value is statistically significant')
else:
    print('Fail to reject the null hypothesis at', alpha1, 'significance level')

if p_value1 <= alpha2:
    print('Reject the null hypothesis at', alpha2, 'significance level')
    print('The observed value is statistically significant')
else:
    print('Fail to reject the null hypothesis at', alpha2, 'significance level')