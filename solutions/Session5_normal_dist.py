"""
Calculating with the Normal Distribution
"""
# !pip install scipy
from scipy.stats import norm

persons = norm(loc=170, scale=10)

# cumulative distribution function (cdf)
print(persons.cdf(170)) 

# What is the probability to find a person smaller than 145cm?
print(persons.cdf(155))

# What is the probability to find a person taller than 175cm?
print(1-persons.cdf(175))

# What is the probability to find a person measuring between 170 and 185cm?
print(persons.cdf(185) - persons.cdf(170))

# inverse cumulative distribution function
# How tall are the smallest 10% of the population?
print(persons.ppf(0.1))


# we have two persons. One is 155cm tall. The other is 192cm tall and a basketball player. Which of them has the more unusual height?
# NBA basketball players have a height of N(198, 5)
# method: we normalize to compare the numbers better.
# we normalize both to a *standard normal distribution N(0, 1)*
# -> we measure how many sigmas (std.devs) the two persons are away from their mean. This is called the z-score.
# z = (x - mu) / sigma
z1 = (155 - 170) / 10
print(z1)
z2 = (192 - 198) / 5
print(z2)
