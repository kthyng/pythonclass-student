'''
hw1
'''

import numpy as np


def make_array():
    '''Make and return an array of ones with size (1000,10)
    '''

    a = np.ones((1000, 10))

    return list(a)


def array_mean(a):
    '''Return the mean of the input array
    '''

    return a.mean()

