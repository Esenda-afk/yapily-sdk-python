# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.352
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import yapily
from yapily.api.accounts_api import AccountsApi  # noqa: E501
from yapily.rest import ApiException


class TestAccountsApi(unittest.TestCase):
    """AccountsApi unit test stubs"""

    def setUp(self):
        self.api = yapily.api.accounts_api.AccountsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_account_direct_debits_using_get(self):
        """Test case for get_account_direct_debits_using_get

        Get account direct debits  # noqa: E501
        """
        pass

    def test_get_account_periodic_payments_using_get(self):
        """Test case for get_account_periodic_payments_using_get

        Get account payments detail  # noqa: E501
        """
        pass

    def test_get_account_scheduled_payments_using_get(self):
        """Test case for get_account_scheduled_payments_using_get

        Get account scheduled payments  # noqa: E501
        """
        pass

    def test_get_account_using_get(self):
        """Test case for get_account_using_get

        Get account  # noqa: E501
        """
        pass

    def test_get_accounts_using_get(self):
        """Test case for get_accounts_using_get

        Get accounts  # noqa: E501
        """
        pass

    def test_initiate_account_request_using_post(self):
        """Test case for initiate_account_request_using_post

        Initiate a new account request for user to authorize  # noqa: E501
        """
        pass

    def test_re_authorise_account_using_patch(self):
        """Test case for re_authorise_account_using_patch

        Re-authorise account request  # noqa: E501
        """
        pass

    def test_update_pre_authorise_account_consent_using_put(self):
        """Test case for update_pre_authorise_account_consent_using_put

        Update pre authorize consent for user to authorise account  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
