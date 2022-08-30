#!/usr/bin/env python3
"""tests for client.py"""
from client import GithubOrgClient
from utils import (access_nested_map, get_json, memoize)
from unittest.mock import patch
from parameterized import parameterized, parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """class TestGithubOrgClient"""

    @patch('GithubOrgClient.org')
    @parameterized.expand([
        ("google"),
        ("abc")
        ])
    def test_GithubOrgClient(self, name):
        """test that GithubOrgClient.org returns the correct value"""
        self.assertEqual(org(), name)

    def test_public_repos_url(self, payload):
        """Test that the result based on the mocked payload"""
        with mock.patch(
                'GithubOrgClient._public_repos_url', new_callable=PropertyMock
                ) as mock_public_repos_url:
            mock_public_repos_url.return_value = self._public_repos_url()
            mock_public_repos_url.assert_called_once_with()

    @patch('get_json')
    def test_public_repos(self, license, result):
        """test that it return a payload of your choice"""
        with patch('GithubOrgClient._public_repos_url') as mock:
            mock.return_value = _public_repos_url()
            self.assert_called_once(public_repos(license), result)

    @parameterized.expand([
        ("{"license": {"key": "my_license"}}", "my_license", "my_license"),
        ("{"license": {"key": "other_license"}}", "my_license", {
            "key": "other_license"})
        ])
    def test_has_license(self, repo, license_key, expected):
        """unit-test GithubOrgClient.has_license"""
        self.assertEqual(has_license(repo, license_key), expected)
