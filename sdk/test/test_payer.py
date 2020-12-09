# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.287
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.payer import Payer  # noqa: E501
from yapily.rest import ApiException

class TestPayer(unittest.TestCase):
    """Payer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Payer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.payer.Payer()  # noqa: E501
        if include_optional :
            return Payer(
                name = '0', 
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
                    sub_department = '0', ), 
                account_identifications = [
                    yapily.models.account_identification.AccountIdentification(
                        type = 'SORT_CODE', 
                        identification = '0', )
                    ]
            )
        else :
            return Payer(
                name = '0',
                account_identifications = [
                    yapily.models.account_identification.AccountIdentification(
                        type = 'SORT_CODE', 
                        identification = '0', )
                    ],
        )

    def testPayer(self):
        """Test Payer"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
