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

import lakefs_sdk
from lakefs_sdk.api.health_check_api import HealthCheckApi  # noqa: E501
from lakefs_sdk.rest import ApiException


class TestHealthCheckApi(unittest.TestCase):
    """HealthCheckApi unit test stubs"""

    def setUp(self):
        self.api = lakefs_sdk.api.health_check_api.HealthCheckApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_health_check(self):
        """Test case for health_check

        """
        pass


if __name__ == '__main__':
    unittest.main()
