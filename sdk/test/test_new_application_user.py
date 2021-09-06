# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 1.64.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.new_application_user import NewApplicationUser  # noqa: E501
from yapily.rest import ApiException

class TestNewApplicationUser(unittest.TestCase):
    """NewApplicationUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NewApplicationUser
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.new_application_user.NewApplicationUser()  # noqa: E501
        if include_optional :
            return NewApplicationUser(
                application_user_id = '0', 
                reference_id = '0'
            )
        else :
            return NewApplicationUser(
        )

    def testNewApplicationUser(self):
        """Test NewApplicationUser"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
