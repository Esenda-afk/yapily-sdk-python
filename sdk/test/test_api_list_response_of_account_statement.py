# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.272
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.api_list_response_of_account_statement import ApiListResponseOfAccountStatement  # noqa: E501
from yapily.rest import ApiException

class TestApiListResponseOfAccountStatement(unittest.TestCase):
    """ApiListResponseOfAccountStatement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiListResponseOfAccountStatement
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.api_list_response_of_account_statement.ApiListResponseOfAccountStatement()  # noqa: E501
        if include_optional :
            return ApiListResponseOfAccountStatement(
                meta = yapily.models.response_list_meta.ResponseListMeta(
                    tracing_id = '0', 
                    count = 56, 
                    pagination = yapily.models.pagination.Pagination(
                        next = yapily.models.next.Next(
                            before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            cursor = '0', 
                            from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            limit = 56, ), 
                        self = yapily.models.filter_and_sort.FilterAndSort(
                            before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            cursor = '0', 
                            from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            limit = 56, 
                            offset = 56, 
                            sort = 'date', ), 
                        total_count = 56, ), ), 
                data = [
                    yapily.models.account_statement.AccountStatement(
                        id = '0', 
                        start_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        creation_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ], 
                links = {
                    'key' : '0'
                    }
            )
        else :
            return ApiListResponseOfAccountStatement(
        )

    def testApiListResponseOfAccountStatement(self):
        """Test ApiListResponseOfAccountStatement"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
