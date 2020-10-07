# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.252
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class OverdraftOverdraftTierBandSet(object):
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
        'authorised_indicator': 'bool',
        'buffer_amount': 'str',
        'identification': 'str',
        'minimum_arranged_overdraft_amount': 'str',
        'notes': 'list[str]',
        'overdraft_fees_charges': 'list[OverdraftOverdraftFeesCharges1]',
        'overdraft_tier_band': 'list[OverdraftOverdraftTierBand]',
        'overdraft_type': 'str',
        'tier_band_method': 'str'
    }

    attribute_map = {
        'authorised_indicator': 'AuthorisedIndicator',
        'buffer_amount': 'BufferAmount',
        'identification': 'Identification',
        'minimum_arranged_overdraft_amount': 'MinimumArrangedOverdraftAmount',
        'notes': 'Notes',
        'overdraft_fees_charges': 'OverdraftFeesCharges',
        'overdraft_tier_band': 'OverdraftTierBand',
        'overdraft_type': 'OverdraftType',
        'tier_band_method': 'TierBandMethod'
    }

    def __init__(self, authorised_indicator=None, buffer_amount=None, identification=None, minimum_arranged_overdraft_amount=None, notes=None, overdraft_fees_charges=None, overdraft_tier_band=None, overdraft_type=None, tier_band_method=None, local_vars_configuration=None):  # noqa: E501
        """OverdraftOverdraftTierBandSet - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._authorised_indicator = None
        self._buffer_amount = None
        self._identification = None
        self._minimum_arranged_overdraft_amount = None
        self._notes = None
        self._overdraft_fees_charges = None
        self._overdraft_tier_band = None
        self._overdraft_type = None
        self._tier_band_method = None
        self.discriminator = None

        if authorised_indicator is not None:
            self.authorised_indicator = authorised_indicator
        if buffer_amount is not None:
            self.buffer_amount = buffer_amount
        if identification is not None:
            self.identification = identification
        if minimum_arranged_overdraft_amount is not None:
            self.minimum_arranged_overdraft_amount = minimum_arranged_overdraft_amount
        if notes is not None:
            self.notes = notes
        if overdraft_fees_charges is not None:
            self.overdraft_fees_charges = overdraft_fees_charges
        if overdraft_tier_band is not None:
            self.overdraft_tier_band = overdraft_tier_band
        if overdraft_type is not None:
            self.overdraft_type = overdraft_type
        if tier_band_method is not None:
            self.tier_band_method = tier_band_method

    @property
    def authorised_indicator(self):
        """Gets the authorised_indicator of this OverdraftOverdraftTierBandSet.  # noqa: E501


        :return: The authorised_indicator of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :rtype: bool
        """
        return self._authorised_indicator

    @authorised_indicator.setter
    def authorised_indicator(self, authorised_indicator):
        """Sets the authorised_indicator of this OverdraftOverdraftTierBandSet.


        :param authorised_indicator: The authorised_indicator of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :type: bool
        """

        self._authorised_indicator = authorised_indicator

    @property
    def buffer_amount(self):
        """Gets the buffer_amount of this OverdraftOverdraftTierBandSet.  # noqa: E501


        :return: The buffer_amount of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :rtype: str
        """
        return self._buffer_amount

    @buffer_amount.setter
    def buffer_amount(self, buffer_amount):
        """Sets the buffer_amount of this OverdraftOverdraftTierBandSet.


        :param buffer_amount: The buffer_amount of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :type: str
        """

        self._buffer_amount = buffer_amount

    @property
    def identification(self):
        """Gets the identification of this OverdraftOverdraftTierBandSet.  # noqa: E501


        :return: The identification of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :rtype: str
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """Sets the identification of this OverdraftOverdraftTierBandSet.


        :param identification: The identification of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :type: str
        """

        self._identification = identification

    @property
    def minimum_arranged_overdraft_amount(self):
        """Gets the minimum_arranged_overdraft_amount of this OverdraftOverdraftTierBandSet.  # noqa: E501


        :return: The minimum_arranged_overdraft_amount of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :rtype: str
        """
        return self._minimum_arranged_overdraft_amount

    @minimum_arranged_overdraft_amount.setter
    def minimum_arranged_overdraft_amount(self, minimum_arranged_overdraft_amount):
        """Sets the minimum_arranged_overdraft_amount of this OverdraftOverdraftTierBandSet.


        :param minimum_arranged_overdraft_amount: The minimum_arranged_overdraft_amount of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :type: str
        """

        self._minimum_arranged_overdraft_amount = minimum_arranged_overdraft_amount

    @property
    def notes(self):
        """Gets the notes of this OverdraftOverdraftTierBandSet.  # noqa: E501


        :return: The notes of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :rtype: list[str]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this OverdraftOverdraftTierBandSet.


        :param notes: The notes of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :type: list[str]
        """

        self._notes = notes

    @property
    def overdraft_fees_charges(self):
        """Gets the overdraft_fees_charges of this OverdraftOverdraftTierBandSet.  # noqa: E501


        :return: The overdraft_fees_charges of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :rtype: list[OverdraftOverdraftFeesCharges1]
        """
        return self._overdraft_fees_charges

    @overdraft_fees_charges.setter
    def overdraft_fees_charges(self, overdraft_fees_charges):
        """Sets the overdraft_fees_charges of this OverdraftOverdraftTierBandSet.


        :param overdraft_fees_charges: The overdraft_fees_charges of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :type: list[OverdraftOverdraftFeesCharges1]
        """

        self._overdraft_fees_charges = overdraft_fees_charges

    @property
    def overdraft_tier_band(self):
        """Gets the overdraft_tier_band of this OverdraftOverdraftTierBandSet.  # noqa: E501


        :return: The overdraft_tier_band of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :rtype: list[OverdraftOverdraftTierBand]
        """
        return self._overdraft_tier_band

    @overdraft_tier_band.setter
    def overdraft_tier_band(self, overdraft_tier_band):
        """Sets the overdraft_tier_band of this OverdraftOverdraftTierBandSet.


        :param overdraft_tier_band: The overdraft_tier_band of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :type: list[OverdraftOverdraftTierBand]
        """

        self._overdraft_tier_band = overdraft_tier_band

    @property
    def overdraft_type(self):
        """Gets the overdraft_type of this OverdraftOverdraftTierBandSet.  # noqa: E501


        :return: The overdraft_type of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :rtype: str
        """
        return self._overdraft_type

    @overdraft_type.setter
    def overdraft_type(self, overdraft_type):
        """Sets the overdraft_type of this OverdraftOverdraftTierBandSet.


        :param overdraft_type: The overdraft_type of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :type: str
        """
        allowed_values = ["Committed", "OnDemand", "Other"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and overdraft_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `overdraft_type` ({0}), must be one of {1}"  # noqa: E501
                .format(overdraft_type, allowed_values)
            )

        self._overdraft_type = overdraft_type

    @property
    def tier_band_method(self):
        """Gets the tier_band_method of this OverdraftOverdraftTierBandSet.  # noqa: E501


        :return: The tier_band_method of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :rtype: str
        """
        return self._tier_band_method

    @tier_band_method.setter
    def tier_band_method(self, tier_band_method):
        """Sets the tier_band_method of this OverdraftOverdraftTierBandSet.


        :param tier_band_method: The tier_band_method of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :type: str
        """
        allowed_values = ["Tiered", "Whole"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and tier_band_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `tier_band_method` ({0}), must be one of {1}"  # noqa: E501
                .format(tier_band_method, allowed_values)
            )

        self._tier_band_method = tier_band_method

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
        if not isinstance(other, OverdraftOverdraftTierBandSet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OverdraftOverdraftTierBandSet):
            return True

        return self.to_dict() != other.to_dict()
