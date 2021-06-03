# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.351
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.api_response_of_transfer_response import ApiResponseOfTransferResponse  # noqa: E501
from yapily.rest import ApiException

class TestApiResponseOfTransferResponse(unittest.TestCase):
    """ApiResponseOfTransferResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiResponseOfTransferResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.api_response_of_transfer_response.ApiResponseOfTransferResponse()  # noqa: E501
        if include_optional :
            return ApiResponseOfTransferResponse(
                meta = yapily.models.response_meta.ResponseMeta(
                    tracing_id = '0', ), 
                data = yapily.models.transfer_response.TransferResponse(
                    from_account_id = '0', 
                    to_account_id = '0', 
                    status = 'PENDING', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    reference = '0', 
                    balance = 1.337, 
                    currency = '0', ), 
                links = {
                    'key' : '0'
                    }
            )
        else :
            return ApiResponseOfTransferResponse(
        )

    def testApiResponseOfTransferResponse(self):
        """Test ApiResponseOfTransferResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
