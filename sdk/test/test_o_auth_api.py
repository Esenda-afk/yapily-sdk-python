# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.107
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import yapily
from yapily.api.o_auth_api import OAuthApi  # noqa: E501
from yapily.rest import ApiException


class TestOAuthApi(unittest.TestCase):
    """OAuthApi unit test stubs"""

    def setUp(self):
        self.api = yapily.api.o_auth_api.OAuthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_oauth_token(self):
        """Test case for oauth_token

        Retrieve Access Token  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
