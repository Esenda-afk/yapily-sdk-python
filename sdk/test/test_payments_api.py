# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.28
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import yapily
from yapily.api.payments_api import PaymentsApi  # noqa: E501
from yapily.rest import ApiException


class TestPaymentsApi(unittest.TestCase):
    """PaymentsApi unit test stubs"""

    def setUp(self):
        self.api = yapily.api.payments_api.PaymentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_payment_using_post(self):
        """Test case for create_payment_using_post

        Create a new single payment  # noqa: E501
        """
        pass

    def test_get_payment_status_using_get(self):
        """Test case for get_payment_status_using_get

        Get status of a payment  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()