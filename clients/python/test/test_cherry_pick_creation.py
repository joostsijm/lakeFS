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
from lakefs_sdk.models.cherry_pick_creation import CherryPickCreation  # noqa: E501
from lakefs_sdk.rest import ApiException

class TestCherryPickCreation(unittest.TestCase):
    """CherryPickCreation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CherryPickCreation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CherryPickCreation`
        """
        model = lakefs_sdk.models.cherry_pick_creation.CherryPickCreation()  # noqa: E501
        if include_optional :
            return CherryPickCreation(
                ref = '', 
                parent_number = 56, 
                commit_overrides = lakefs_sdk.models.commit_overrides.CommitOverrides(
                    message = '', 
                    metadata = {
                        'key' : ''
                        }, ), 
                force = True
            )
        else :
            return CherryPickCreation(
                ref = '',
        )
        """

    def testCherryPickCreation(self):
        """Test CherryPickCreation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
