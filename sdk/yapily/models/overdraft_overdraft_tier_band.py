# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.314
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class OverdraftOverdraftTierBand(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'bank_guaranteed_indicator': 'bool',
        'ear': 'str',
        'identification': 'str',
        'notes': 'list[str]',
        'overdraft_fees_charges': 'list[OverdraftOverdraftFeesCharges]',
        'overdraft_interest_charging_coverage': 'str',
        'tier_value_max': 'str',
        'tier_value_min': 'str'
    }

    attribute_map = {
        'bank_guaranteed_indicator': 'BankGuaranteedIndicator',
        'ear': 'EAR',
        'identification': 'Identification',
        'notes': 'Notes',
        'overdraft_fees_charges': 'OverdraftFeesCharges',
        'overdraft_interest_charging_coverage': 'OverdraftInterestChargingCoverage',
        'tier_value_max': 'TierValueMax',
        'tier_value_min': 'TierValueMin'
    }

    def __init__(self, bank_guaranteed_indicator=None, ear=None, identification=None, notes=None, overdraft_fees_charges=None, overdraft_interest_charging_coverage=None, tier_value_max=None, tier_value_min=None, local_vars_configuration=None):  # noqa: E501
        """OverdraftOverdraftTierBand - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bank_guaranteed_indicator = None
        self._ear = None
        self._identification = None
        self._notes = None
        self._overdraft_fees_charges = None
        self._overdraft_interest_charging_coverage = None
        self._tier_value_max = None
        self._tier_value_min = None
        self.discriminator = None

        if bank_guaranteed_indicator is not None:
            self.bank_guaranteed_indicator = bank_guaranteed_indicator
        if ear is not None:
            self.ear = ear
        if identification is not None:
            self.identification = identification
        if notes is not None:
            self.notes = notes
        if overdraft_fees_charges is not None:
            self.overdraft_fees_charges = overdraft_fees_charges
        if overdraft_interest_charging_coverage is not None:
            self.overdraft_interest_charging_coverage = overdraft_interest_charging_coverage
        if tier_value_max is not None:
            self.tier_value_max = tier_value_max
        if tier_value_min is not None:
            self.tier_value_min = tier_value_min

    @property
    def bank_guaranteed_indicator(self):
        """Gets the bank_guaranteed_indicator of this OverdraftOverdraftTierBand.  # noqa: E501


        :return: The bank_guaranteed_indicator of this OverdraftOverdraftTierBand.  # noqa: E501
        :rtype: bool
        """
        return self._bank_guaranteed_indicator

    @bank_guaranteed_indicator.setter
    def bank_guaranteed_indicator(self, bank_guaranteed_indicator):
        """Sets the bank_guaranteed_indicator of this OverdraftOverdraftTierBand.


        :param bank_guaranteed_indicator: The bank_guaranteed_indicator of this OverdraftOverdraftTierBand.  # noqa: E501
        :type: bool
        """

        self._bank_guaranteed_indicator = bank_guaranteed_indicator

    @property
    def ear(self):
        """Gets the ear of this OverdraftOverdraftTierBand.  # noqa: E501


        :return: The ear of this OverdraftOverdraftTierBand.  # noqa: E501
        :rtype: str
        """
        return self._ear

    @ear.setter
    def ear(self, ear):
        """Sets the ear of this OverdraftOverdraftTierBand.


        :param ear: The ear of this OverdraftOverdraftTierBand.  # noqa: E501
        :type: str
        """

        self._ear = ear

    @property
    def identification(self):
        """Gets the identification of this OverdraftOverdraftTierBand.  # noqa: E501


        :return: The identification of this OverdraftOverdraftTierBand.  # noqa: E501
        :rtype: str
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """Sets the identification of this OverdraftOverdraftTierBand.


        :param identification: The identification of this OverdraftOverdraftTierBand.  # noqa: E501
        :type: str
        """

        self._identification = identification

    @property
    def notes(self):
        """Gets the notes of this OverdraftOverdraftTierBand.  # noqa: E501


        :return: The notes of this OverdraftOverdraftTierBand.  # noqa: E501
        :rtype: list[str]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this OverdraftOverdraftTierBand.


        :param notes: The notes of this OverdraftOverdraftTierBand.  # noqa: E501
        :type: list[str]
        """

        self._notes = notes

    @property
    def overdraft_fees_charges(self):
        """Gets the overdraft_fees_charges of this OverdraftOverdraftTierBand.  # noqa: E501


        :return: The overdraft_fees_charges of this OverdraftOverdraftTierBand.  # noqa: E501
        :rtype: list[OverdraftOverdraftFeesCharges]
        """
        return self._overdraft_fees_charges

    @overdraft_fees_charges.setter
    def overdraft_fees_charges(self, overdraft_fees_charges):
        """Sets the overdraft_fees_charges of this OverdraftOverdraftTierBand.


        :param overdraft_fees_charges: The overdraft_fees_charges of this OverdraftOverdraftTierBand.  # noqa: E501
        :type: list[OverdraftOverdraftFeesCharges]
        """

        self._overdraft_fees_charges = overdraft_fees_charges

    @property
    def overdraft_interest_charging_coverage(self):
        """Gets the overdraft_interest_charging_coverage of this OverdraftOverdraftTierBand.  # noqa: E501


        :return: The overdraft_interest_charging_coverage of this OverdraftOverdraftTierBand.  # noqa: E501
        :rtype: str
        """
        return self._overdraft_interest_charging_coverage

    @overdraft_interest_charging_coverage.setter
    def overdraft_interest_charging_coverage(self, overdraft_interest_charging_coverage):
        """Sets the overdraft_interest_charging_coverage of this OverdraftOverdraftTierBand.


        :param overdraft_interest_charging_coverage: The overdraft_interest_charging_coverage of this OverdraftOverdraftTierBand.  # noqa: E501
        :type: str
        """
        allowed_values = ["Tiered", "Whole"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and overdraft_interest_charging_coverage not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `overdraft_interest_charging_coverage` ({0}), must be one of {1}"  # noqa: E501
                .format(overdraft_interest_charging_coverage, allowed_values)
            )

        self._overdraft_interest_charging_coverage = overdraft_interest_charging_coverage

    @property
    def tier_value_max(self):
        """Gets the tier_value_max of this OverdraftOverdraftTierBand.  # noqa: E501


        :return: The tier_value_max of this OverdraftOverdraftTierBand.  # noqa: E501
        :rtype: str
        """
        return self._tier_value_max

    @tier_value_max.setter
    def tier_value_max(self, tier_value_max):
        """Sets the tier_value_max of this OverdraftOverdraftTierBand.


        :param tier_value_max: The tier_value_max of this OverdraftOverdraftTierBand.  # noqa: E501
        :type: str
        """

        self._tier_value_max = tier_value_max

    @property
    def tier_value_min(self):
        """Gets the tier_value_min of this OverdraftOverdraftTierBand.  # noqa: E501


        :return: The tier_value_min of this OverdraftOverdraftTierBand.  # noqa: E501
        :rtype: str
        """
        return self._tier_value_min

    @tier_value_min.setter
    def tier_value_min(self, tier_value_min):
        """Sets the tier_value_min of this OverdraftOverdraftTierBand.


        :param tier_value_min: The tier_value_min of this OverdraftOverdraftTierBand.  # noqa: E501
        :type: str
        """

        self._tier_value_min = tier_value_min

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OverdraftOverdraftTierBand):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OverdraftOverdraftTierBand):
            return True

        return self.to_dict() != other.to_dict()
