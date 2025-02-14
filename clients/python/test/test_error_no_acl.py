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
from lakefs_sdk.models.error_no_acl import ErrorNoACL  # noqa: E501
from lakefs_sdk.rest import ApiException

class TestErrorNoACL(unittest.TestCase):
    """ErrorNoACL unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ErrorNoACL
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ErrorNoACL`
        """
        model = lakefs_sdk.models.error_no_acl.ErrorNoACL()  # noqa: E501
        if include_optional :
            return ErrorNoACL(
                message = '', 
                no_acl = True
            )
        else :
            return ErrorNoACL(
                message = '',
        )
        """

    def testErrorNoACL(self):
        """Test ErrorNoACL"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
