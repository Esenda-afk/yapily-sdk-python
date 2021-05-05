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
from yapily.models.credit_interest_tier_band_set import CreditInterestTierBandSet  # noqa: E501
from yapily.rest import ApiException

class TestCreditInterestTierBandSet(unittest.TestCase):
    """CreditInterestTierBandSet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreditInterestTierBandSet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.credit_interest_tier_band_set.CreditInterestTierBandSet()  # noqa: E501
        if include_optional :
            return CreditInterestTierBandSet(
                calculation_method = 'Compound', 
                credit_interest_eligibility = [
                    yapily.models.credit_interest_credit_interest_eligibility.CreditInterestCreditInterestEligibility(
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
                        type = 'DirectDebits', )
                    ], 
                destination = 'PayAway', 
                notes = [
                    '0'
                    ], 
                tier_band = [
                    yapily.models.credit_interest_tier_band.CreditInterestTierBand(
                        aer = '0', 
                        application_frequency = 'PerAcademicTerm', 
                        bank_interest_rate = '0', 
                        bank_interest_rate_type = 'LinkedBaseRate', 
                        calculation_frequency = 'PerAcademicTerm', 
                        deposit_interest_applied_coverage = 'Tiered', 
                        fixed_variable_interest_rate_type = 'Fixed', 
                        identification = '0', 
                        notes = [
                            '0'
                            ], 
                        other_application_frequency = yapily.models.other_application_frequency.OtherApplicationFrequency(
                            code = '0', 
                            description = '0', 
                            name = '0', ), 
                        other_bank_interest_type = yapily.models.other_bank_interest_type.OtherBankInterestType(
                            code = '0', 
                            description = '0', 
                            name = '0', ), 
                        other_calculation_frequency = yapily.models.other_calculation_frequency.OtherCalculationFrequency(
                            code = '0', 
                            description = '0', 
                            name = '0', ), 
                        tier_value_maximum = '0', 
                        tier_value_minimum = '0', )
                    ], 
                tier_band_method = 'Tiered'
            )
        else :
            return CreditInterestTierBandSet(
        )

    def testCreditInterestTierBandSet(self):
        """Test CreditInterestTierBandSet"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
