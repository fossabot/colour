#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Defines unit tests for :mod:`colour.utilities.common` module.
"""

from __future__ import division, unicode_literals

import numpy as np
import unittest

from colour.utilities import (
    batch,
    is_iterable,
    is_string,
    is_numeric,
    is_integer,
    filter_kwargs)

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013 - 2015 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['TestBatch',
           'TestIsIterable',
           'TestIsString',
           'TestIsNumeric',
           'TestIsInteger',
           'TestFilterKwargs']


class TestBatch(unittest.TestCase):
    """
    Defines :func:`colour.utilities.common.batch` definition unit tests
    methods.
    """

    def test_batch(self):
        """
        Tests :func:`colour.utilities.common.batch` definition.
        """

        self.assertListEqual(
            list(batch(tuple(range(10)))),
            [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9,)])

        self.assertListEqual(
            list(batch(tuple(range(10)), 5)),
            [(0, 1, 2, 3, 4), (5, 6, 7, 8, 9)])

        self.assertListEqual(
            list(batch(tuple(range(10)), 1)),
            [(0,), (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,)])


class TestIsIterable(unittest.TestCase):
    """
    Defines :func:`colour.utilities.common.is_iterable` definition unit tests
    methods.
    """

    def test_is_iterable(self):
        """
        Tests :func:`colour.utilities.common.is_iterable` definition.
        """

        self.assertTrue(is_iterable(''))

        self.assertTrue(is_iterable(()))

        self.assertTrue(is_iterable([]))

        self.assertTrue(is_iterable(dict()))

        self.assertTrue(is_iterable(np.array([])))

        self.assertFalse(is_iterable(1))

        self.assertFalse(is_iterable(2))


class TestIsString(unittest.TestCase):
    """
    Defines :func:`colour.utilities.common.is_string` definition unit tests
    methods.
    """

    def test_is_string(self):
        """
        Tests :func:`colour.utilities.common.is_string` definition.
        """

        self.assertTrue(is_string(str('Hello World!')))

        self.assertTrue(is_string('Hello World!'))

        self.assertTrue(is_string(r'Hello World!'))

        self.assertFalse(is_string(1))

        self.assertFalse(is_string([1]))

        self.assertFalse(is_string({1: None}))


class TestIsNumeric(unittest.TestCase):
    """
    Defines :func:`colour.utilities.common.is_numeric` definition unit tests
    methods.
    """

    def test_is_numeric(self):
        """
        Tests :func:`colour.utilities.common.is_numeric` definition.
        """

        self.assertTrue(is_numeric(1))

        self.assertTrue(is_numeric(1))

        self.assertTrue(is_numeric(complex(1)))

        self.assertFalse(is_numeric((1,)))

        self.assertFalse(is_numeric([1]))

        self.assertFalse(is_numeric('1'))


class TestIsInteger(unittest.TestCase):
    """
    Defines :func:`colour.utilities.common.is_integer` definition units
    tests methods.
    """

    def test_is_integer(self):
        """
        Tests :func:`colour.utilities.common.is_integer` definition.
        """

        self.assertTrue(is_integer(1))

        self.assertTrue(is_integer(1.001))

        self.assertFalse(is_integer(1.01))


class TestFilterKwargs(unittest.TestCase):
    """
    Defines :func:`colour.utilities.common.filter_kwargs` definition units
    tests methods.
    """

    def test_filter_kwargs(self):
        """
        Tests :func:`colour.utilities.common.filter_kwargs` definition.
        """

        def func_a(a):
            """
            :def:`filter_kwargs` unit tests :def:`func_a`.
            """
            return a

        def func_b(a, b=0):
            """
            :def:`filter_kwargs` unit tests :def:`func_b`.
            """

            return a, b

        def func_c(a, b=0, c=0):
            """
            :def:`filter_kwargs` unit tests :def:`func_c`.
            """

            return a, b, c

        self.assertEqual(
            1,
            func_a(1, **filter_kwargs(func_a, b=2, c=3)))

        self.assertTupleEqual(
            (1, 2),
            func_b(1, **filter_kwargs(func_b, b=2, c=3)))

        self.assertTupleEqual(
            (1, 2, 3),
            func_c(1, **filter_kwargs(func_c, b=2, c=3)))


if __name__ == '__main__':
    unittest.main()
