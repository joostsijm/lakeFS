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

from lakefs_sdk.models.upload_part import UploadPart

class TestUploadPart(unittest.TestCase):
    """UploadPart unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UploadPart:
        """Test UploadPart
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UploadPart`
        """
        model = UploadPart()
        if include_optional:
            return UploadPart(
                part_number = 56,
                etag = ''
            )
        else:
            return UploadPart(
                part_number = 56,
                etag = '',
        )
        """

    def testUploadPart(self):
        """Test UploadPart"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
