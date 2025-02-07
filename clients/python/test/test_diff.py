# coding: utf-8

"""
    lakeFS API

    lakeFS HTTP API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: services@treeverse.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import lakefs_sdk
from lakefs_sdk.models.diff import Diff  # noqa: E501
from lakefs_sdk.rest import ApiException

class TestDiff(unittest.TestCase):
    """Diff unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Diff
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Diff`
        """
        model = lakefs_sdk.models.diff.Diff()  # noqa: E501
        if include_optional :
            return Diff(
                type = 'added', 
                path = '', 
                path_type = 'common_prefix', 
                size_bytes = 56
            )
        else :
            return Diff(
                type = 'added',
                path = '',
                path_type = 'common_prefix',
        )
        """

    def testDiff(self):
        """Test Diff"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
