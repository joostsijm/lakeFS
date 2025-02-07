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
from lakefs_sdk.models.garbage_collection_rules import GarbageCollectionRules  # noqa: E501
from lakefs_sdk.rest import ApiException

class TestGarbageCollectionRules(unittest.TestCase):
    """GarbageCollectionRules unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GarbageCollectionRules
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GarbageCollectionRules`
        """
        model = lakefs_sdk.models.garbage_collection_rules.GarbageCollectionRules()  # noqa: E501
        if include_optional :
            return GarbageCollectionRules(
                default_retention_days = 56, 
                branches = [
                    lakefs_sdk.models.garbage_collection_rule.GarbageCollectionRule(
                        branch_id = '', 
                        retention_days = 56, )
                    ]
            )
        else :
            return GarbageCollectionRules(
                default_retention_days = 56,
                branches = [
                    lakefs_sdk.models.garbage_collection_rule.GarbageCollectionRule(
                        branch_id = '', 
                        retention_days = 56, )
                    ],
        )
        """

    def testGarbageCollectionRules(self):
        """Test GarbageCollectionRules"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
