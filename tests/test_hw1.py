'''
Tests for hw1.
'''

import numpy as np

import imp

hw1 = imp.load_source('hw1', 'hw/hw1.py')


def test_make_array():
    '''Test functionality of function make_array
    '''

    a = hw1.make_array()

    assert isinstance(a, np.ndarray), 'output from make_array() should be of type array'

    assert a.shape == (1000, 10), 'output from make_array() should be shape (1000, 10)'


def test_array_mean():
    '''Test functionality of function array_mean
    '''

    a = np.random.randn((1000))  # test for vector
    b = np.random.randn(1000, 100)  # test for array
    c = b.copy()
    c[0, 0] = np.nan

    assert hw1.array_mean(a) == a.mean(), 'array_mean does not work for a vector'
    assert hw1.array_mean(b) == b.mean(), 'array_mean does not work for a 2D array'
    assert hw1.array_mean(c) == np.nanmean(b), 'array_mean does not work for a 2D array with a nan'
