# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.249
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.core_product import CoreProduct  # noqa: E501
from yapily.rest import ApiException

class TestCoreProduct(unittest.TestCase):
    """CoreProduct unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CoreProduct
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.core_product.CoreProduct()  # noqa: E501
        if include_optional :
            return CoreProduct(
                monthly_maximum_charge = '0', 
                product_description = '0', 
                product_url = '0', 
                sales_access_channels = [
                    'Branch'
                    ], 
                servicing_access_channels = [
                    'ATM'
                    ], 
                tcs_and_cs_url = '0'
            )
        else :
            return CoreProduct(
        )

    def testCoreProduct(self):
        """Test CoreProduct"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
