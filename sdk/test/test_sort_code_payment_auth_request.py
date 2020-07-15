# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.210
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.sort_code_payment_auth_request import SortCodePaymentAuthRequest  # noqa: E501
from yapily.rest import ApiException

class TestSortCodePaymentAuthRequest(unittest.TestCase):
    """SortCodePaymentAuthRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SortCodePaymentAuthRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.sort_code_payment_auth_request.SortCodePaymentAuthRequest()  # noqa: E501
        if include_optional :
            return SortCodePaymentAuthRequest(
                user_uuid = '0', 
                application_user_id = '0', 
                forward_parameters = [
                    '0'
                    ], 
                institution_id = '0', 
                callback = '0', 
                one_time_token = False, 
                payment_request = yapily.models.sort_code_payment_request.SortCodePaymentRequest(
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
                            sub_department = '0', ), ), )
            )
        else :
            return SortCodePaymentAuthRequest(
                institution_id = '0',
                callback = '0',
                one_time_token = False,
                payment_request = yapily.models.sort_code_payment_request.SortCodePaymentRequest(
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
                            sub_department = '0', ), ), ),
        )

    def testSortCodePaymentAuthRequest(self):
        """Test SortCodePaymentAuthRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
