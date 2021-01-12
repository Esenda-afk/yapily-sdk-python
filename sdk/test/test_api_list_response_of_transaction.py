# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.300
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.api_list_response_of_transaction import ApiListResponseOfTransaction  # noqa: E501
from yapily.rest import ApiException

class TestApiListResponseOfTransaction(unittest.TestCase):
    """ApiListResponseOfTransaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiListResponseOfTransaction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.api_list_response_of_transaction.ApiListResponseOfTransaction()  # noqa: E501
        if include_optional :
            return ApiListResponseOfTransaction(
                meta = yapily.models.response_list_meta.ResponseListMeta(
                    tracing_id = '0', 
                    count = 56, 
                    pagination = yapily.models.pagination.Pagination(
                        next = yapily.models.next.Next(
                            before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            cursor = '0', 
                            from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            limit = 56, ), 
                        self = yapily.models.filter_and_sort.FilterAndSort(
                            before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            cursor = '0', 
                            from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            limit = 56, 
                            offset = 56, 
                            sort = 'date', ), 
                        total_count = 56, ), ), 
                data = [
                    yapily.models.transaction.Transaction(
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
                        supplementary_data = yapily.models.supplementary_data.supplementaryData(), )
                    ], 
                links = {
                    'key' : '0'
                    }
            )
        else :
            return ApiListResponseOfTransaction(
        )

    def testApiListResponseOfTransaction(self):
        """Test ApiListResponseOfTransaction"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
