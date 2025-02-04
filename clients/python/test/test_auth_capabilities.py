# coding: utf-8

"""
    lakeFS API

    lakeFS HTTP API

    The version of the OpenAPI document: 1.0.0
    Contact: services@treeverse.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from lakefs_sdk.models.auth_capabilities import AuthCapabilities

class TestAuthCapabilities(unittest.TestCase):
    """AuthCapabilities unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthCapabilities:
        """Test AuthCapabilities
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthCapabilities`
        """
        model = AuthCapabilities()
        if include_optional:
            return AuthCapabilities(
                invite_user = True,
                forgot_password = True
            )
        else:
            return AuthCapabilities(
        )
        """

    def testAuthCapabilities(self):
        """Test AuthCapabilities"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
