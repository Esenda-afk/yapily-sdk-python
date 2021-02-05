# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.306
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.inline_response2001_other_accessibility import InlineResponse2001OtherAccessibility  # noqa: E501
from yapily.rest import ApiException

class TestInlineResponse2001OtherAccessibility(unittest.TestCase):
    """InlineResponse2001OtherAccessibility unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2001OtherAccessibility
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.inline_response2001_other_accessibility.InlineResponse2001OtherAccessibility()  # noqa: E501
        if include_optional :
            return InlineResponse2001OtherAccessibility(
                code = '0', 
                description = '0', 
                name = '0'
            )
        else :
            return InlineResponse2001OtherAccessibility(
        )

    def testInlineResponse2001OtherAccessibility(self):
        """Test InlineResponse2001OtherAccessibility"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
