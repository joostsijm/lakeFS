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
from lakefs_sdk.models.hook_run_list import HookRunList  # noqa: E501
from lakefs_sdk.rest import ApiException

class TestHookRunList(unittest.TestCase):
    """HookRunList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test HookRunList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HookRunList`
        """
        model = lakefs_sdk.models.hook_run_list.HookRunList()  # noqa: E501
        if include_optional :
            return HookRunList(
                pagination = lakefs_sdk.models.pagination.Pagination(
                    has_more = True, 
                    next_offset = '', 
                    results = 0, 
                    max_per_page = 0, ), 
                results = [
                    lakefs_sdk.models.hook_run.HookRun(
                        hook_run_id = '', 
                        action = '', 
                        hook_id = '', 
                        start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        status = 'failed', )
                    ]
            )
        else :
            return HookRunList(
                pagination = lakefs_sdk.models.pagination.Pagination(
                    has_more = True, 
                    next_offset = '', 
                    results = 0, 
                    max_per_page = 0, ),
                results = [
                    lakefs_sdk.models.hook_run.HookRun(
                        hook_run_id = '', 
                        action = '', 
                        hook_id = '', 
                        start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        status = 'failed', )
                    ],
        )
        """

    def testHookRunList(self):
        """Test HookRunList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
