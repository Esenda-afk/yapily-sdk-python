# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.373
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import yapily
from yapily.api.transactions_api import TransactionsApi  # noqa: E501
from yapily.rest import ApiException


class TestTransactionsApi(unittest.TestCase):
    """TransactionsApi unit test stubs"""

    def setUp(self):
        self.api = yapily.api.transactions_api.TransactionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_transactions_using_get(self):
        """Test case for get_transactions_using_get

        Get account transactions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
