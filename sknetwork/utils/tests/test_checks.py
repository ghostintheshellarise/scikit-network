#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tests for checks.py"""

import unittest

from sknetwork.data import star_wars_villains, rock_paper_scissors, house
from sknetwork.utils.adjacency_formats import *
from sknetwork.utils.checks import has_nonnegative_entries, has_positive_entries,\
    is_proba_array, make_weights, check_engine, check_is_proba, check_weights, check_random_state


# noinspection PyMissingOrEmptyDocstring
class TestFormats(unittest.TestCase):

    def setUp(self):
        self.adjacency = rock_paper_scissors()
        self.dense_mat = np.identity(3)

    def test_non_negative_entries(self):
        self.assertTrue(has_nonnegative_entries(self.adjacency))
        self.assertTrue(has_nonnegative_entries(self.dense_mat))

    def test_positive_entries(self):
        self.assertFalse(has_positive_entries(self.dense_mat))
        with self.assertRaises(TypeError):
            # noinspection PyTypeChecker
            has_positive_entries(self.adjacency)

    def test_proba_array_1d(self):
        self.assertTrue(is_proba_array(np.array([.5, .5])))

    def test_error_proba_array(self):
        with self.assertRaises(TypeError):
            is_proba_array(np.ones((2, 2, 2)))

    def test_error_make_weights(self):
        with self.assertRaises(ValueError):
            make_weights(distribution='junk', adjacency=self.adjacency)

    def test_error_check_engine(self):
        with self.assertRaises(ValueError):
            check_engine('junk')

    def test_error_check_is_proba(self):
        with self.assertRaises(TypeError):
            # noinspection PyTypeChecker
            check_is_proba('junk')
        with self.assertRaises(ValueError):
            check_is_proba(2)

    def test_error_check_weights(self):
        with self.assertRaises(ValueError):
            check_weights(np.zeros(4), self.adjacency)
        with self.assertRaises(TypeError):
            # noinspection PyTypeChecker
            check_weights(2, self.adjacency)
        with self.assertRaises(ValueError):
            check_weights(np.zeros(3), self.adjacency, positive_entries=True)
        with self.assertRaises(ValueError):
            check_weights(-np.ones(3), self.adjacency)

    def test_random_state(self):
        random_state = np.random.RandomState(1)
        self.assertEqual(type(check_random_state(random_state)), np.random.RandomState)

    def test_error_random_state(self):
        with self.assertRaises(TypeError):
            # noinspection PyTypeChecker
            check_random_state('junk')
