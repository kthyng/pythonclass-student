'''
Tests for hw1.
'''

import numpy as np


def test_make_array():
    '''Test functionality of function make_array
    '''

    import hw1

    a = hw1.make_array()

    if type(a) is np.ndarray:
        print 'Successfully made an array.'
    else:
        print 'Array not created correctly'

    if a.shape == (1000, 10):
        print 'The array is of the correct shape.'
