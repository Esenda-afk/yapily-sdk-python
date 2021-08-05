# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.396
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.uri import URI  # noqa: E501
from yapily.rest import ApiException

class TestURI(unittest.TestCase):
    """URI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test URI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.uri.URI()  # noqa: E501
        if include_optional :
            return URI(
                absolute = True, 
                authority = '0', 
                fragment = '0', 
                host = '0', 
                opaque = True, 
                path = '0', 
                port = 56, 
                query = '0', 
                raw_authority = '0', 
                raw_fragment = '0', 
                raw_path = '0', 
                raw_query = '0', 
                raw_scheme_specific_part = '0', 
                raw_user_info = '0', 
                scheme = '0', 
                scheme_specific_part = '0', 
                user_info = '0'
            )
        else :
            return URI(
        )

    def testURI(self):
        """Test URI"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
