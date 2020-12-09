# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.287
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.pre_authorisation_request import PreAuthorisationRequest  # noqa: E501
from yapily.rest import ApiException

class TestPreAuthorisationRequest(unittest.TestCase):
    """PreAuthorisationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PreAuthorisationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.pre_authorisation_request.PreAuthorisationRequest()  # noqa: E501
        if include_optional :
            return PreAuthorisationRequest(
                scope = '0', 
                user_uuid = '0', 
                application_user_id = '0', 
                forward_parameters = [
                    '0'
                    ], 
                institution_id = '0', 
                callback = '0', 
                one_time_token = False
            )
        else :
            return PreAuthorisationRequest(
                institution_id = '0',
                callback = '0',
                one_time_token = False,
        )

    def testPreAuthorisationRequest(self):
        """Test PreAuthorisationRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
