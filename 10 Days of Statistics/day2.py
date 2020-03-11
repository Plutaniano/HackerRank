##Challenge 1
# 6*6 = 36 is the size of the set of all possible combinations
# For the sum of both dices to be more than 9, there are only a few possible combinations. They are:
# [5,5]
# [6,6]
# [5,6] and [6,5]
# [4,6] and [6,4]
# Tottaling a sum of 6 possible dice combinations.
# (36-6)/36 = 5/6

##Challenge 2
# There are a limited number of possible dice combinations that sum up to 6. They are:
# [1,5] and [5,1]
# [2,4] and [4,2]
# [3,3], but it doesnt count because the dice are equal
# So the chance of the sum of 2 dices being equal to 6 is 4/36.
# 4/36 = 1/9

##Challenge 3
# Urns are [X,Y,Z] and R is for red and B is for black.
# The possible combinations of 2 red balls and 1 black ball are:
# [R, R, B], [R, B, R] and [B, R, R]
# Considering the ratio of balls in each urn:
# The chance of drawing [R, R, B] is [4/7, 5/9, 1/2]
# The chance of drawing [R, B, R] is [4/7, 4/9, 1/2]
# The chance of drawing [B, R, R] is [3/7, 5/9, 1/2]
# Multiplying the "elements" of each draw and then summing them up we get: 17/42