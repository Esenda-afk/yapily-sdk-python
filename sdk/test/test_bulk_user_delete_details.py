# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.350
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.bulk_user_delete_details import BulkUserDeleteDetails  # noqa: E501
from yapily.rest import ApiException

class TestBulkUserDeleteDetails(unittest.TestCase):
    """BulkUserDeleteDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BulkUserDeleteDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.bulk_user_delete_details.BulkUserDeleteDetails()  # noqa: E501
        if include_optional :
            return BulkUserDeleteDetails(
                id = '0', 
                invalid_application_user_ids = [
                    '0'
                    ], 
                invalid_user_uuids = [
                    '0'
                    ], 
                status = 'IN_PROGRESS', 
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                users = [
                    yapily.models.user_delete_response.UserDeleteResponse(
                        id = '0', 
                        delete_status = 'SUCCESS', 
                        creation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        user_consents = [
                            yapily.models.consent_delete_response.ConsentDeleteResponse(
                                id = '0', 
                                delete_status = 'SUCCESS', 
                                institution_id = '0', 
                                institution_consent_id = '0', 
                                creation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], )
                    ], 
                links = {
                    'key' : '0'
                    }
            )
        else :
            return BulkUserDeleteDetails(
        )

    def testBulkUserDeleteDetails(self):
        """Test BulkUserDeleteDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
