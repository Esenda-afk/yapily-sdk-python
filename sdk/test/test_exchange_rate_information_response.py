# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.282
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.exchange_rate_information_response import ExchangeRateInformationResponse  # noqa: E501
from yapily.rest import ApiException

class TestExchangeRateInformationResponse(unittest.TestCase):
    """ExchangeRateInformationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExchangeRateInformationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.exchange_rate_information_response.ExchangeRateInformationResponse()  # noqa: E501
        if include_optional :
            return ExchangeRateInformationResponse(
                exchange_rate_expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                foreign_exchange_contract_reference = '0', 
                rate = 1.337, 
                rate_type = 'ACTUAL', 
                unit_currency = '0'
            )
        else :
            return ExchangeRateInformationResponse(
        )

    def testExchangeRateInformationResponse(self):
        """Test ExchangeRateInformationResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
