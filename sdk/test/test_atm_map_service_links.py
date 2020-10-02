# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.249
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.atm_map_service_links import ATMMapServiceLinks  # noqa: E501
from yapily.rest import ApiException

class TestATMMapServiceLinks(unittest.TestCase):
    """ATMMapServiceLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ATMMapServiceLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.atm_map_service_links.ATMMapServiceLinks()  # noqa: E501
        if include_optional :
            return ATMMapServiceLinks(
                bing_maps_url = '0', 
                google_maps_url = '0', 
                here_maps_url = '0'
            )
        else :
            return ATMMapServiceLinks(
        )

    def testATMMapServiceLinks(self):
        """Test ATMMapServiceLinks"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
