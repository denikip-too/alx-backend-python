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
    def test_access_nested_map_exception(nested_map, path, expected):
        """test that KeyError is raised using assertRaises context manager"""
        with self.assertRaises(KeyError) as raises:
            self.assertEqua(access_nested_map(nested_map, path), expected)
            raise


class TestGetJson(unittest.TestCase):
    """class TestGetJson"""

    @patch('http://example.com', {"payload": True})
    @patch('http://holberton.io', {"payload": False})
    def test_get_json(self, url, payload):
        """test that utils.get_json returns the expected result"""
        self.assertEqual(get_json(url), payload)
