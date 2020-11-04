# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.269
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.account_request import AccountRequest  # noqa: E501
from yapily.rest import ApiException

class TestAccountRequest(unittest.TestCase):
    """AccountRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AccountRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.account_request.AccountRequest()  # noqa: E501
        if include_optional :
            return AccountRequest(
                transaction_from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                transaction_to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                account_identifiers = yapily.models.account_info.AccountInfo(
                    account_id = '0', 
                    account_identification = yapily.models.account_identification.AccountIdentification(
                        type = 'SORT_CODE', 
                        identification = '0', ), ), 
                account_identifiers_for_transaction = [
                    yapily.models.account_info.AccountInfo(
                        account_id = '0', 
                        account_identification = yapily.models.account_identification.AccountIdentification(
                            type = 'SORT_CODE', 
                            identification = '0', ), )
                    ], 
                account_identifiers_for_balance = [
                    yapily.models.account_info.AccountInfo(
                        account_id = '0', 
                        account_identification = yapily.models.account_identification.AccountIdentification(
                            type = 'SORT_CODE', 
                            identification = '0', ), )
                    ], 
                feature_scope = [
                    'INITIATE_PRE_AUTHORISATION'
                    ]
            )
        else :
            return AccountRequest(
        )

    def testAccountRequest(self):
        """Test AccountRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
