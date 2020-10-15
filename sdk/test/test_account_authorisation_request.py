# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.256
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.account_authorisation_request import AccountAuthorisationRequest  # noqa: E501
from yapily.rest import ApiException

class TestAccountAuthorisationRequest(unittest.TestCase):
    """AccountAuthorisationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AccountAuthorisationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.account_authorisation_request.AccountAuthorisationRequest()  # noqa: E501
        if include_optional :
            return AccountAuthorisationRequest(
                user_uuid = '0', 
                application_user_id = '0', 
                forward_parameters = [
                    '0'
                    ], 
                institution_id = '0', 
                callback = '0', 
                one_time_token = False, 
                account_request = yapily.models.account_request.AccountRequest(
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
                            account_id = '0', )
                        ], 
                    account_identifiers_for_balance = [
                        yapily.models.account_info.AccountInfo(
                            account_id = '0', )
                        ], 
                    feature_scope = [
                        'INITIATE_PRE_AUTHORISATION'
                        ], )
            )
        else :
            return AccountAuthorisationRequest(
                institution_id = '0',
                callback = '0',
                one_time_token = False,
        )

    def testAccountAuthorisationRequest(self):
        """Test AccountAuthorisationRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
