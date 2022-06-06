"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.  # noqa: E501

    The version of the OpenAPI document: 2.2.0
    Contact: support@yapily.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import yapily
from yapily.model.amount import Amount
from yapily.model.exchange_rate_information_response import ExchangeRateInformationResponse
from yapily.model.frequency_response import FrequencyResponse
from yapily.model.payee import Payee
from yapily.model.payer import Payer
from yapily.model.payment_charge_details import PaymentChargeDetails
from yapily.model.payment_status import PaymentStatus
from yapily.model.payment_status_details import PaymentStatusDetails
from yapily.model.priority_code_enum import PriorityCodeEnum
from yapily.model.refund_account import RefundAccount
globals()['Amount'] = Amount
globals()['ExchangeRateInformationResponse'] = ExchangeRateInformationResponse
globals()['FrequencyResponse'] = FrequencyResponse
globals()['Payee'] = Payee
globals()['Payer'] = Payer
globals()['PaymentChargeDetails'] = PaymentChargeDetails
globals()['PaymentStatus'] = PaymentStatus
globals()['PaymentStatusDetails'] = PaymentStatusDetails
globals()['PriorityCodeEnum'] = PriorityCodeEnum
globals()['RefundAccount'] = RefundAccount
from yapily.model.payment_response import PaymentResponse


class TestPaymentResponse(unittest.TestCase):
    """PaymentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentResponse(self):
        """Test PaymentResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaymentResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
