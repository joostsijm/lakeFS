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

from lakefs_sdk.models.tag_creation import TagCreation

class TestTagCreation(unittest.TestCase):
    """TagCreation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TagCreation:
        """Test TagCreation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TagCreation`
        """
        model = TagCreation()
        if include_optional:
            return TagCreation(
                id = '',
                ref = '',
                force = True
            )
        else:
            return TagCreation(
                id = '',
                ref = '',
        )
        """

    def testTagCreation(self):
        """Test TagCreation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
