# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.95
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import yapily
from yapily.api.applications_api import ApplicationsApi  # noqa: E501
from yapily.rest import ApiException


class TestApplicationsApi(unittest.TestCase):
    """ApplicationsApi unit test stubs"""

    def setUp(self):
        self.api = yapily.api.applications_api.ApplicationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_application_me_using_get(self):
        """Test case for get_application_me_using_get

        Returns the details of the application that owns the request credentials  # noqa: E501
        """
        pass

    def test_get_jwks_using_get(self):
        """Test case for get_jwks_using_get

        JSON Web Key Set (JWKS) for authenticated application  # noqa: E501
        """
        pass

    def test_revoke_tokens_using_post(self):
        """Test case for revoke_tokens_using_post

        Revoke existing access tokens for application, which will also generate a new public key discoverable via /jwks  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
