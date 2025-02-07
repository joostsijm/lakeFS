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
from lakefs_sdk.models.repository_dump_status import RepositoryDumpStatus  # noqa: E501
from lakefs_sdk.rest import ApiException

class TestRepositoryDumpStatus(unittest.TestCase):
    """RepositoryDumpStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RepositoryDumpStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RepositoryDumpStatus`
        """
        model = lakefs_sdk.models.repository_dump_status.RepositoryDumpStatus()  # noqa: E501
        if include_optional :
            return RepositoryDumpStatus(
                id = '', 
                done = True, 
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                error = '', 
                refs = lakefs_sdk.models.refs_dump.RefsDump(
                    commits_meta_range_id = '', 
                    tags_meta_range_id = '', 
                    branches_meta_range_id = '', )
            )
        else :
            return RepositoryDumpStatus(
                id = '',
                done = True,
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testRepositoryDumpStatus(self):
        """Test RepositoryDumpStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
