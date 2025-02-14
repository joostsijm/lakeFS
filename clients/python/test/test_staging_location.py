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
from lakefs_sdk.models.staging_location import StagingLocation  # noqa: E501
from lakefs_sdk.rest import ApiException

class TestStagingLocation(unittest.TestCase):
    """StagingLocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StagingLocation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StagingLocation`
        """
        model = lakefs_sdk.models.staging_location.StagingLocation()  # noqa: E501
        if include_optional :
            return StagingLocation(
                physical_address = '', 
                presigned_url = '', 
                presigned_url_expiry = 56
            )
        else :
            return StagingLocation(
        )
        """

    def testStagingLocation(self):
        """Test StagingLocation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
