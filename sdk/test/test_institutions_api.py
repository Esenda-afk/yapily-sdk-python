# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 1.87.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import yapily
from yapily.api.institutions_api import InstitutionsApi  # noqa: E501
from yapily.rest import ApiException


class TestInstitutionsApi(unittest.TestCase):
    """InstitutionsApi unit test stubs"""

    def setUp(self):
        self.api = yapily.api.institutions_api.InstitutionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_feature_details_using_get(self):
        """Test case for get_feature_details_using_get

        Retrieve details for Yapily's institution features  # noqa: E501
        """
        pass

    def test_get_institution_using_get(self):
        """Test case for get_institution_using_get

        Retrieves details of a specific institution available in Yapily  # noqa: E501
        """
        pass

    def test_get_institutions_using_get(self):
        """Test case for get_institutions_using_get

        Retrieves the list of institutions available in Yapily  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
