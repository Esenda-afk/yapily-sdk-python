# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.277
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.balances import Balances  # noqa: E501
from yapily.rest import ApiException

class TestBalances(unittest.TestCase):
    """Balances unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Balances
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.balances.Balances()  # noqa: E501
        if include_optional :
            return Balances(
                main_balance_amount = yapily.models.amount.Amount(
                    amount = 1.337, 
                    currency = '0', ), 
                balances = [
                    yapily.models.account_balance.AccountBalance(
                        type = 'CLOSING_AVAILABLE', 
                        date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        balance_amount = yapily.models.amount.Amount(
                            amount = 1.337, 
                            currency = '0', ), 
                        credit_line_included = False, 
                        credit_lines = [
                            yapily.models.credit_line.CreditLine(
                                type = 'AVAILABLE', 
                                credit_line_amount = yapily.models.amount.Amount(
                                    amount = 1.337, 
                                    currency = '0', ), )
                            ], )
                    ]
            )
        else :
            return Balances(
        )

    def testBalances(self):
        """Test Balances"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
