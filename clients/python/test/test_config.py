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
from lakefs_sdk.models.config import Config  # noqa: E501
from lakefs_sdk.rest import ApiException

class TestConfig(unittest.TestCase):
    """Config unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Config
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Config`
        """
        model = lakefs_sdk.models.config.Config()  # noqa: E501
        if include_optional :
            return Config(
                version_config = lakefs_sdk.models.version_config.VersionConfig(
                    version = '', 
                    latest_version = '', 
                    upgrade_recommended = True, 
                    upgrade_url = '', ), 
                storage_config = lakefs_sdk.models.storage_config.StorageConfig(
                    blockstore_type = '', 
                    blockstore_namespace_example = '', 
                    blockstore_namespace_validity_regex = '', 
                    default_namespace_prefix = '', 
                    pre_sign_support = True, 
                    pre_sign_support_ui = True, 
                    import_support = True, 
                    import_validity_regex = '', 
                    pre_sign_multipart_upload = True, 
                    blockstore_id = '', 
                    blockstore_description = '', 
                    blockstore_extras = {
                        'key' : ''
                        }, ), 
                storage_config_list = [
                    lakefs_sdk.models.storage_config.StorageConfig(
                        blockstore_type = '', 
                        blockstore_namespace_example = '', 
                        blockstore_namespace_validity_regex = '', 
                        default_namespace_prefix = '', 
                        pre_sign_support = True, 
                        pre_sign_support_ui = True, 
                        import_support = True, 
                        import_validity_regex = '', 
                        pre_sign_multipart_upload = True, 
                        blockstore_id = '', 
                        blockstore_description = '', 
                        blockstore_extras = {
                            'key' : ''
                            }, )
                    ]
            )
        else :
            return Config(
        )
        """

    def testConfig(self):
        """Test Config"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
