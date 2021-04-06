# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.326
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.enrichment import Enrichment  # noqa: E501
from yapily.rest import ApiException

class TestEnrichment(unittest.TestCase):
    """Enrichment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Enrichment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.enrichment.Enrichment()  # noqa: E501
        if include_optional :
            return Enrichment(
                categorisation = yapily.models.categorisation.Categorisation(
                    category = yapily.models.category.Category(
                        label = '0', 
                        id = '0', ), ), 
                transaction_hash = yapily.models.transaction_hash.TransactionHash(
                    hash = '0', )
            )
        else :
            return Enrichment(
        )

    def testEnrichment(self):
        """Test Enrichment"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
