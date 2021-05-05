# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.337
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.eligibility_other_eligibility import EligibilityOtherEligibility  # noqa: E501
from yapily.rest import ApiException

class TestEligibilityOtherEligibility(unittest.TestCase):
    """EligibilityOtherEligibility unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EligibilityOtherEligibility
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.eligibility_other_eligibility.EligibilityOtherEligibility()  # noqa: E501
        if include_optional :
            return EligibilityOtherEligibility(
                amount = '0', 
                description = '0', 
                indicator = True, 
                name = '0', 
                notes = [
                    '0'
                    ], 
                other_type = yapily.models.other_type.OtherType(
                    code = '0', 
                    description = '0', 
                    name = '0', ), 
                period = 'Day', 
                textual = '0', 
                type = 'DirectDebits'
            )
        else :
            return EligibilityOtherEligibility(
        )

    def testEligibilityOtherEligibility(self):
        """Test EligibilityOtherEligibility"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
