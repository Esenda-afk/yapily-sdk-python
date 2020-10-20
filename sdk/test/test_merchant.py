# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.260
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.merchant import Merchant  # noqa: E501
from yapily.rest import ApiException

class TestMerchant(unittest.TestCase):
    """Merchant unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Merchant
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.merchant.Merchant()  # noqa: E501
        if include_optional :
            return Merchant(
                merchant_name = '0', 
                merchant_category_code = '0'
            )
        else :
            return Merchant(
        )

    def testMerchant(self):
        """Test Merchant"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
