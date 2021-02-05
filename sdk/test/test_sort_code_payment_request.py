# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.306
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.sort_code_payment_request import SortCodePaymentRequest  # noqa: E501
from yapily.rest import ApiException

class TestSortCodePaymentRequest(unittest.TestCase):
    """SortCodePaymentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SortCodePaymentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.sort_code_payment_request.SortCodePaymentRequest()  # noqa: E501
        if include_optional :
            return SortCodePaymentRequest(
                sender_account_id = '0', 
                name = '0', 
                amount = 1.337, 
                currency = '0', 
                reference = '0', 
                country = '0', 
                type = 'BILL', 
                account_number = '0', 
                sort_code = '0', 
                merchant_info = yapily.models.merchant_info.MerchantInfo(
                    category_code = '0', 
                    customer_id = '0', 
                    address = yapily.models.address.Address(
                        address_lines = [
                            '0'
                            ], 
                        street_name = '0', 
                        building_number = '0', 
                        post_code = '0', 
                        town_name = '0', 
                        county = [
                            '0'
                            ], 
                        address_type = 'BUSINESS', 
                        country = '0', 
                        department = '0', 
                        sub_department = '0', ), ), 
                read_refund_account = False
            )
        else :
            return SortCodePaymentRequest(
                name = '0',
                amount = 1.337,
                currency = '0',
                reference = '0',
                country = '0',
                account_number = '0',
                sort_code = '0',
        )

    def testSortCodePaymentRequest(self):
        """Test SortCodePaymentRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
