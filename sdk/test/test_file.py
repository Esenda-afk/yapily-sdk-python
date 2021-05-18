# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.344
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.file import File  # noqa: E501
from yapily.rest import ApiException

class TestFile(unittest.TestCase):
    """File unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test File
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.file.File()  # noqa: E501
        if include_optional :
            return File(
                absolute = True, 
                absolute_file = null, 
                absolute_path = '0', 
                canonical_file = null, 
                canonical_path = '0', 
                directory = True, 
                file = True, 
                free_space = 56, 
                hidden = True, 
                name = '0', 
                parent = '0', 
                parent_file = null, 
                path = '0', 
                total_space = 56, 
                usable_space = 56
            )
        else :
            return File(
        )

    def testFile(self):
        """Test File"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
