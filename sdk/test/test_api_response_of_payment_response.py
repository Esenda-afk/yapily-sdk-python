# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.298
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.api_response_of_payment_response import ApiResponseOfPaymentResponse  # noqa: E501
from yapily.rest import ApiException

class TestApiResponseOfPaymentResponse(unittest.TestCase):
    """ApiResponseOfPaymentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiResponseOfPaymentResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.api_response_of_payment_response.ApiResponseOfPaymentResponse()  # noqa: E501
        if include_optional :
            return ApiResponseOfPaymentResponse(
                meta = yapily.models.response_meta.ResponseMeta(
                    tracing_id = '0', ), 
                data = yapily.models.payment_response.PaymentResponse(
                    id = '0', 
                    institution_consent_id = '0', 
                    payment_idempotency_id = '0', 
                    payment_lifecycle_id = '0', 
                    status = 'PENDING', 
                    status_details = yapily.models.payment_status_details.PaymentStatusDetails(
                        status = 'PENDING', 
                        status_reason = '0', 
                        status_reason_description = '0', 
                        status_update_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        multi_authorisation_status = yapily.models.multi_authorisation.MultiAuthorisation(
                            status = '0', 
                            number_of_authorisation_required = 56, 
                            number_of_authorisation_received = 56, 
                            last_updated_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            expiration_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), ), 
                    payer = yapily.models.payer.Payer(
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
                    payee_details = yapily.models.payee.Payee(
                        name = '0', 
                        account_identifications = [
                            yapily.models.account_identification.AccountIdentification(
                                type = 'SORT_CODE', 
                                identification = '0', )
                            ], 
                        merchant_id = '0', 
                        merchant_category_code = '0', ), 
                    reference = '0', 
                    amount = 1.337, 
                    currency = '0', 
                    amount_details = yapily.models.amount.Amount(
                        amount = 1.337, 
                        currency = '0', ), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    first_payment_amount = yapily.models.amount.Amount(
                        amount = 1.337, 
                        currency = '0', ), 
                    first_payment_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    next_payment_amount = yapily.models.amount.Amount(
                        amount = 1.337, 
                        currency = '0', ), 
                    next_payment_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    final_payment_amount = yapily.models.amount.Amount(
                        amount = 1.337, 
                        currency = '0', ), 
                    final_payment_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    number_of_payments = 56, 
                    previous_payment_amount = yapily.models.amount.Amount(
                        amount = 1.337, 
                        currency = '0', ), 
                    previous_payment_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    charge_details = [
                        yapily.models.charge_details.ChargeDetails(
                            charge_amount = yapily.models.amount.Amount(
                                amount = 1.337, 
                                currency = '0', ), )
                        ], 
                    scheduled_payment_type = '0', 
                    scheduled_payment_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    frequency = yapily.models.frequency_response.FrequencyResponse(
                        execution_day = 56, 
                        frequency_type = 'DAILY', 
                        interval_month = 56, 
                        interval_week = 56, ), 
                    currency_of_transfer = '0', 
                    purpose = '0', 
                    priority = 'NORMAL', 
                    exchange_rate = yapily.models.exchange_rate_information_response.ExchangeRateInformationResponse(
                        exchange_rate_expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        foreign_exchange_contract_reference = '0', 
                        rate = 1.337, 
                        rate_type = 'ACTUAL', 
                        unit_currency = '0', ), 
                    refund_account = yapily.models.refund_account.RefundAccount(
                        name = '0', ), 
                    bulk_amount_sum = 1.337, ), 
                links = {
                    'key' : '0'
                    }
            )
        else :
            return ApiResponseOfPaymentResponse(
        )

    def testApiResponseOfPaymentResponse(self):
        """Test ApiResponseOfPaymentResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
