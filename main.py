#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A simple cumulative binomial probability calculator.
This is not for sale and should not be used for commercial purposes.
"""

from math import comb

import matplotlib.pyplot as plt
from scipy.stats import binom

__author__ = "Greentea"
__license__ = "MIT"
__version__ = "1.0.1"
__status__ = "Prototype"


def greater_or_equal_target_probability(number):
    return number >= target_probability

max_rolls = 300
success = 120
prob_of_success = 0.5
target_probability = 0.88

dist = dist = [1 - sum([binom.pmf(fails, roll, 0.5) for fails in range(success)]) for roll in range(success, max_rolls+1)]
filtered_dist = list(filter(greater_or_equal_target_probability, dist))
min_number_of_attempts = list(range(success, max_rolls+1))[-len(filtered_dist):]

plt.bar(min_number_of_attempts, filtered_dist)
print(min_number_of_attempts[0], filtered_dist[0])
