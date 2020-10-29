# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.265
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.geo_location1 import GeoLocation1  # noqa: E501
from yapily.rest import ApiException

class TestGeoLocation1(unittest.TestCase):
    """GeoLocation1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GeoLocation1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.geo_location1.GeoLocation1()  # noqa: E501
        if include_optional :
            return GeoLocation1(
                geographic_coordinates = yapily.models.geographic_coordinates1.GeographicCoordinates1(
                    latitude = '0', 
                    longitude = '0', )
            )
        else :
            return GeoLocation1(
        )

    def testGeoLocation1(self):
        """Test GeoLocation1"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
