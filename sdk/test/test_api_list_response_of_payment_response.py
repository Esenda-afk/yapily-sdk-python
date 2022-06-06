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
from yapily.model.filtered_client_payload_list_payment_response import FilteredClientPayloadListPaymentResponse
from yapily.model.payment_response import PaymentResponse
from yapily.model.raw_response import RawResponse
from yapily.model.response_forwarded_data import ResponseForwardedData
from yapily.model.response_list_meta import ResponseListMeta
globals()['FilteredClientPayloadListPaymentResponse'] = FilteredClientPayloadListPaymentResponse
globals()['PaymentResponse'] = PaymentResponse
globals()['RawResponse'] = RawResponse
globals()['ResponseForwardedData'] = ResponseForwardedData
globals()['ResponseListMeta'] = ResponseListMeta
from yapily.model.api_list_response_of_payment_response import ApiListResponseOfPaymentResponse


class TestApiListResponseOfPaymentResponse(unittest.TestCase):
    """ApiListResponseOfPaymentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApiListResponseOfPaymentResponse(self):
        """Test ApiListResponseOfPaymentResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApiListResponseOfPaymentResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
