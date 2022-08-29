#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from parameterized import parameterized
from utils import (access_nested_map, get_json, memoize)
import requests
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """class TestAccessNestedMap"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test that the method returns what it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
        ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """test that KeyError is raised using assertRaises context manager"""
        with self.assertRaises(KeyError) as raises:
            access_nested_map(nested_map, path)
            self.assertEqual(f"KeyError('{expected}')", repr(raises.exception))


"""class TestGetJson(unittest.TestCase):"""
    """class TestGetJson"""

    """@mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_json(self, url, payload):"""
        """test that utils.get_json returns the expected result"""
        """result = get_json('http://example.com')
        self.assert_called_once(result, {"payload": True})
        result = get_json('http://holberton.io')
        self.assert_called_once(result, {"payload": False})"""


class TestMemoize(unittest.TestCase):
    """class TestMemoize"""

    @patch('test_memoize.TestClass.a_method', 1)
    @patch('test_memoize.TestClass.a_property', 2)
    def test_memoize(self, call):
        """test_memoize method"""
        class TestClass:
            """class TestClass"""

            def a_method(self):
                """a_method method"""
                return (42)

            @memoize
            def a_property(self):
                """a_property method"""
                return (self.a_method())

        with patch.object('TestClass', a_method) as mock:
            tests = TestClass()
            tests.a_property()
            tests.a_property()
            mock.assert_called_once()
