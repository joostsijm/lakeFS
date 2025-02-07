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
from lakefs_sdk.models.garbage_collection_prepare_response import GarbageCollectionPrepareResponse  # noqa: E501
from lakefs_sdk.rest import ApiException

class TestGarbageCollectionPrepareResponse(unittest.TestCase):
    """GarbageCollectionPrepareResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GarbageCollectionPrepareResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GarbageCollectionPrepareResponse`
        """
        model = lakefs_sdk.models.garbage_collection_prepare_response.GarbageCollectionPrepareResponse()  # noqa: E501
        if include_optional :
            return GarbageCollectionPrepareResponse(
                run_id = '64eaa103-d726-4a33-bcb8-7c0b4abfe09e', 
                gc_commits_location = 's3://my-storage-namespace/_lakefs/retention/commits', 
                gc_addresses_location = 's3://my-storage-namespace/_lakefs/retention/addresses', 
                gc_commits_presigned_url = ''
            )
        else :
            return GarbageCollectionPrepareResponse(
                run_id = '64eaa103-d726-4a33-bcb8-7c0b4abfe09e',
                gc_commits_location = 's3://my-storage-namespace/_lakefs/retention/commits',
                gc_addresses_location = 's3://my-storage-namespace/_lakefs/retention/addresses',
        )
        """

    def testGarbageCollectionPrepareResponse(self):
        """Test GarbageCollectionPrepareResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
