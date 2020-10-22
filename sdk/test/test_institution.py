# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.262
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.institution import Institution  # noqa: E501
from yapily.rest import ApiException

class TestInstitution(unittest.TestCase):
    """Institution unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Institution
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.institution.Institution()  # noqa: E501
        if include_optional :
            return Institution(
                id = '0', 
                name = '0', 
                full_name = '0', 
                countries = [
                    yapily.models.country.Country(
                        country_code2 = '0', 
                        display_name = '0', )
                    ], 
                environment_type = 'SANDBOX', 
                credentials_type = 'OAUTH1', 
                media = [
                    yapily.models.media.Media(
                        source = '0', 
                        type = '0', )
                    ], 
                features = [
                    'INITIATE_PRE_AUTHORISATION'
                    ], 
                monitoring = {
                    'key' : yapily.models.monitoring_feature_status.MonitoringFeatureStatus(
                        last_tested = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        span = '0', 
                        status = 'Up', )
                    }
            )
        else :
            return Institution(
        )

    def testInstitution(self):
        """Test Institution"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
