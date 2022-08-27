#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """subclass"""

    @parameterized.expand([
        [{"a": 1}, ("a",)],
        [{"a": {"b": 2}}, ("a",)],
        [{"a": {"b": 2}}, ("a", "b")]
        ])
    def test_access_nested_map(self, a, b):
        """test that the method returns what it is supposed to"""
        self.assertEqual(a, b)
