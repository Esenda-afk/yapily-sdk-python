# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.213
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yapily
from yapily.models.overdraft_overdraft_tier_band_set import OverdraftOverdraftTierBandSet  # noqa: E501
from yapily.rest import ApiException

class TestOverdraftOverdraftTierBandSet(unittest.TestCase):
    """OverdraftOverdraftTierBandSet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OverdraftOverdraftTierBandSet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yapily.models.overdraft_overdraft_tier_band_set.OverdraftOverdraftTierBandSet()  # noqa: E501
        if include_optional :
            return OverdraftOverdraftTierBandSet(
                authorised_indicator = True, 
                buffer_amount = '0', 
                identification = '0', 
                minimum_arranged_overdraft_amount = '0', 
                notes = [
                    '0'
                    ], 
                overdraft_fees_charges = [
                    yapily.models.overdraft_overdraft_fees_charges1.OverdraftOverdraftFeesCharges1(
                        overdraft_fee_charge_cap = [
                            yapily.models.overdraft_overdraft_fee_charge_cap.OverdraftOverdraftFeeChargeCap(
                                capping_period = 'Day', 
                                fee_cap_amount = '0', 
                                fee_cap_occurrence = 1.337, 
                                fee_type = [
                                    'ArrangedOverdraft'
                                    ], 
                                min_max_type = 'Minimum', 
                                notes = [
                                    '0'
                                    ], 
                                other_fee_type = [
                                    yapily.models.overdraft_other_fee_type.OverdraftOtherFeeType(
                                        code = '0', 
                                        description = '0', 
                                        name = '0', )
                                    ], 
                                overdraft_control_indicator = True, )
                            ], 
                        overdraft_fee_charge_detail = [
                            yapily.models.overdraft_overdraft_fee_charge_detail.OverdraftOverdraftFeeChargeDetail(
                                application_frequency = 'AccountClosing', 
                                calculation_frequency = 'AccountClosing', 
                                fee_amount = '0', 
                                fee_rate = '0', 
                                fee_rate_type = 'LinkedBaseRate', 
                                incremental_borrowing_amount = '0', 
                                other_application_frequency = yapily.models.other_application_frequency.OtherApplicationFrequency(
                                    code = '0', 
                                    description = '0', 
                                    name = '0', ), 
                                other_calculation_frequency = yapily.models.other_calculation_frequency.OtherCalculationFrequency(
                                    code = '0', 
                                    description = '0', 
                                    name = '0', ), 
                                other_fee_rate_type = yapily.models.other_fee_rate_type.OtherFeeRateType(
                                    code = '0', 
                                    description = '0', 
                                    name = '0', ), 
                                overdraft_control_indicator = True, )
                            ], )
                    ], 
                overdraft_tier_band = [
                    yapily.models.overdraft_overdraft_tier_band.OverdraftOverdraftTierBand(
                        bank_guaranteed_indicator = True, 
                        ear = '0', 
                        identification = '0', 
                        notes = [
                            '0'
                            ], 
                        overdraft_fees_charges = [
                            yapily.models.overdraft_overdraft_fees_charges.OverdraftOverdraftFeesCharges(
                                overdraft_fee_charge_cap = [
                                    yapily.models.overdraft_overdraft_fee_charge_cap.OverdraftOverdraftFeeChargeCap(
                                        capping_period = 'Day', 
                                        fee_cap_amount = '0', 
                                        fee_cap_occurrence = 1.337, 
                                        fee_type = [
                                            'ArrangedOverdraft'
                                            ], 
                                        min_max_type = 'Minimum', 
                                        other_fee_type = [
                                            yapily.models.overdraft_other_fee_type.OverdraftOtherFeeType(
                                                code = '0', 
                                                description = '0', 
                                                name = '0', )
                                            ], 
                                        overdraft_control_indicator = True, )
                                    ], 
                                overdraft_fee_charge_detail = [
                                    yapily.models.overdraft_overdraft_fee_charge_detail.OverdraftOverdraftFeeChargeDetail(
                                        application_frequency = 'AccountClosing', 
                                        calculation_frequency = 'AccountClosing', 
                                        fee_amount = '0', 
                                        fee_rate = '0', 
                                        fee_rate_type = 'LinkedBaseRate', 
                                        incremental_borrowing_amount = '0', 
                                        other_application_frequency = yapily.models.other_application_frequency.OtherApplicationFrequency(
                                            code = '0', 
                                            description = '0', 
                                            name = '0', ), 
                                        other_calculation_frequency = yapily.models.other_calculation_frequency.OtherCalculationFrequency(
                                            code = '0', 
                                            description = '0', 
                                            name = '0', ), 
                                        other_fee_rate_type = yapily.models.other_fee_rate_type.OtherFeeRateType(
                                            code = '0', 
                                            description = '0', 
                                            name = '0', ), 
                                        overdraft_control_indicator = True, )
                                    ], )
                            ], 
                        overdraft_interest_charging_coverage = 'Tiered', 
                        tier_value_max = '0', 
                        tier_value_min = '0', )
                    ], 
                overdraft_type = 'Committed', 
                tier_band_method = 'Tiered'
            )
        else :
            return OverdraftOverdraftTierBandSet(
        )

    def testOverdraftOverdraftTierBandSet(self):
        """Test OverdraftOverdraftTierBandSet"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
