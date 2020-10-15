# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.256
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.filter_and_sort import FilterAndSort  # noqa: E501
from yapily.rest import ApiException

class TestFilterAndSort(unittest.TestCase):
    """FilterAndSort unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FilterAndSort
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.filter_and_sort.FilterAndSort()  # noqa: E501
        if include_optional :
            return FilterAndSort(
                before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                cursor = '0', 
                _from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                limit = 56, 
                offset = 56, 
                sort = 'date'
            )
        else :
            return FilterAndSort(
        )

    def testFilterAndSort(self):
        """Test FilterAndSort"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
