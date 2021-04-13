# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.330
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.transaction import Transaction  # noqa: E501
from yapily.rest import ApiException

class TestTransaction(unittest.TestCase):
    """Transaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Transaction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.transaction.Transaction()  # noqa: E501
        if include_optional :
            return Transaction(
                id = '0', 
                date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                booking_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                value_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                status = 'BOOKED', 
                amount = 1.337, 
                currency = '0', 
                transaction_amount = yapily.models.transaction_amount.TransactionAmount(
                    amount = 1.337, 
                    currency = '0', ), 
                gross_amount = yapily.models.amount.Amount(
                    amount = 1.337, 
                    currency = '0', ), 
                currency_exchange = yapily.models.currency_exchange.CurrencyExchange(
                    source_currency = '0', 
                    target_currency = '0', 
                    unit_currency = '0', 
                    exchange_rate = 1.337, ), 
                charge_details = yapily.models.charge_details.ChargeDetails(
                    charge_amount = yapily.models.amount.Amount(
                        amount = 1.337, 
                        currency = '0', ), ), 
                reference = '0', 
                statement_references = [
                    yapily.models.statement_reference.StatementReference(
                        value = '0', )
                    ], 
                description = '0', 
                transaction_information = [
                    '0'
                    ], 
                address_details = yapily.models.address_details.AddressDetails(
                    address_line = '0', ), 
                iso_bank_transaction_code = yapily.models.iso_bank_transaction_code.IsoBankTransactionCode(
                    domain_code = yapily.models.iso_code_details.IsoCodeDetails(
                        code = '0', 
                        name = '0', ), 
                    family_code = yapily.models.iso_code_details.IsoCodeDetails(
                        code = '0', 
                        name = '0', ), 
                    sub_family_code = yapily.models.iso_code_details.IsoCodeDetails(
                        code = '0', 
                        name = '0', ), ), 
                proprietary_bank_transaction_code = yapily.models.proprietary_bank_transaction_code.ProprietaryBankTransactionCode(
                    code = '0', 
                    issuer = '0', ), 
                balance = yapily.models.balance.Balance(
                    type = 'CLOSING_AVAILABLE', 
                    balance_amount = yapily.models.amount.Amount(
                        amount = 1.337, 
                        currency = '0', ), ), 
                payee_details = yapily.models.payee.Payee(
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
                        ], 
                    merchant_id = '0', 
                    merchant_category_code = '0', ), 
                payer_details = yapily.models.payer.Payer(
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
                        ], ), 
                merchant = yapily.models.merchant.Merchant(
                    merchant_name = '0', 
                    merchant_category_code = '0', ), 
                enrichment = yapily.models.enrichment.Enrichment(
                    categorisation = yapily.models.categorisation.Categorisation(
                        category = yapily.models.category.Category(
                            label = '0', 
                            id = '0', ), ), 
                    transaction_hash = yapily.models.transaction_hash.TransactionHash(
                        hash = '0', ), ), 
                supplementary_data = yapily.models.supplementary_data.supplementaryData()
            )
        else :
            return Transaction(
        )

    def testTransaction(self):
        """Test Transaction"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
