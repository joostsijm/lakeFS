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
from lakefs_sdk.api.external_api import ExternalApi  # noqa: E501
from lakefs_sdk.rest import ApiException


class TestExternalApi(unittest.TestCase):
    """ExternalApi unit test stubs"""

    def setUp(self):
        self.api = lakefs_sdk.api.external_api.ExternalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_user_external_principal(self):
        """Test case for create_user_external_principal

        attach external principal to user  # noqa: E501
        """
        pass

    def test_delete_user_external_principal(self):
        """Test case for delete_user_external_principal

        delete external principal from user  # noqa: E501
        """
        pass

    def test_external_principal_login(self):
        """Test case for external_principal_login

        perform a login using an external authenticator  # noqa: E501
        """
        pass

    def test_get_external_principal(self):
        """Test case for get_external_principal

        describe external principal by id  # noqa: E501
        """
        pass

    def test_list_user_external_principals(self):
        """Test case for list_user_external_principals

        list user external policies attached to a user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
