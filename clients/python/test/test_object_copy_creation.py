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
from lakefs_sdk.models.object_copy_creation import ObjectCopyCreation  # noqa: E501
from lakefs_sdk.rest import ApiException

class TestObjectCopyCreation(unittest.TestCase):
    """ObjectCopyCreation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ObjectCopyCreation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObjectCopyCreation`
        """
        model = lakefs_sdk.models.object_copy_creation.ObjectCopyCreation()  # noqa: E501
        if include_optional :
            return ObjectCopyCreation(
                src_path = '', 
                src_ref = '', 
                force = True
            )
        else :
            return ObjectCopyCreation(
                src_path = '',
        )
        """

    def testObjectCopyCreation(self):
        """Test ObjectCopyCreation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
