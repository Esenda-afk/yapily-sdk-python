# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.258
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import yapily
from yapily.api.categories_api import CategoriesApi  # noqa: E501
from yapily.rest import ApiException


class TestCategoriesApi(unittest.TestCase):
    """CategoriesApi unit test stubs"""

    def setUp(self):
        self.api = yapily.api.categories_api.CategoriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_categories_using_get(self):
        """Test case for get_categories_using_get

        Retrieves a list of categories returned by the Yapily Categorisation engine for a given locale  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
