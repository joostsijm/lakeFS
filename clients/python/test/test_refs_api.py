# coding: utf-8

"""
    lakeFS API

    lakeFS HTTP API

    The version of the OpenAPI document: 1.0.0
    Contact: services@treeverse.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from lakefs_sdk.api.refs_api import RefsApi


class TestRefsApi(unittest.TestCase):
    """RefsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RefsApi()

    def tearDown(self) -> None:
        pass

    def test_diff_refs(self) -> None:
        """Test case for diff_refs

        diff references
        """
        pass

    def test_find_merge_base(self) -> None:
        """Test case for find_merge_base

        find the merge base for 2 references
        """
        pass

    def test_log_commits(self) -> None:
        """Test case for log_commits

        get commit log from ref. If both objects and prefixes are empty, return all commits.
        """
        pass

    def test_merge_into_branch(self) -> None:
        """Test case for merge_into_branch

        merge references
        """
        pass


if __name__ == '__main__':
    unittest.main()
