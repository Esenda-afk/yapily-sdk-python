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
from yapily.model.authorisation_status import AuthorisationStatus
from yapily.model.exchange_rate_information_response import ExchangeRateInformationResponse
from yapily.model.feature_enum import FeatureEnum
from yapily.model.payment_charge_details import PaymentChargeDetails
from yapily.model.sca_method import ScaMethod
globals()['AuthorisationStatus'] = AuthorisationStatus
globals()['ExchangeRateInformationResponse'] = ExchangeRateInformationResponse
globals()['FeatureEnum'] = FeatureEnum
globals()['PaymentChargeDetails'] = PaymentChargeDetails
globals()['ScaMethod'] = ScaMethod
from yapily.model.payment_embedded_authorisation_request_response import PaymentEmbeddedAuthorisationRequestResponse


class TestPaymentEmbeddedAuthorisationRequestResponse(unittest.TestCase):
    """PaymentEmbeddedAuthorisationRequestResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentEmbeddedAuthorisationRequestResponse(self):
        """Test PaymentEmbeddedAuthorisationRequestResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaymentEmbeddedAuthorisationRequestResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
