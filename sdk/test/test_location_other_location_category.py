# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.311
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.location_other_location_category import LocationOtherLocationCategory  # noqa: E501
from yapily.rest import ApiException

class TestLocationOtherLocationCategory(unittest.TestCase):
    """LocationOtherLocationCategory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LocationOtherLocationCategory
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.location_other_location_category.LocationOtherLocationCategory()  # noqa: E501
        if include_optional :
            return LocationOtherLocationCategory(
                code = '0', 
                description = '0', 
                name = '0'
            )
        else :
            return LocationOtherLocationCategory(
        )

    def testLocationOtherLocationCategory(self):
        """Test LocationOtherLocationCategory"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
