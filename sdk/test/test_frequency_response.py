# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.252
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.frequency_response import FrequencyResponse  # noqa: E501
from yapily.rest import ApiException

class TestFrequencyResponse(unittest.TestCase):
    """FrequencyResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FrequencyResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.frequency_response.FrequencyResponse()  # noqa: E501
        if include_optional :
            return FrequencyResponse(
                execution_day = 56, 
                frequency_type = 'DAILY', 
                interval_month = 56, 
                interval_week = 56
            )
        else :
            return FrequencyResponse(
        )

    def testFrequencyResponse(self):
        """Test FrequencyResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
