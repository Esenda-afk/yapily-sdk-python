# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.35
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from yapily.models.overdraft_other_fee_type import OverdraftOtherFeeType  # noqa: F401,E501


class OverdraftOverdraftFeeChargeCap(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'capping_period': 'str',
        'fee_cap_amount': 'str',
        'fee_cap_occurrence': 'float',
        'fee_min_max_type': 'str',
        'fee_type': 'list[str]',
        'notes': 'list[str]',
        'other_fee_type': 'list[OverdraftOtherFeeType]',
        'overdraft_control_indicator': 'bool'
    }

    attribute_map = {
        'capping_period': 'CappingPeriod',
        'fee_cap_amount': 'FeeCapAmount',
        'fee_cap_occurrence': 'FeeCapOccurrence',
        'fee_min_max_type': 'FeeMinMaxType',
        'fee_type': 'FeeType',
        'notes': 'Notes',
        'other_fee_type': 'OtherFeeType',
        'overdraft_control_indicator': 'OverdraftControlIndicator'
    }

    def __init__(self, capping_period=None, fee_cap_amount=None, fee_cap_occurrence=None, fee_min_max_type=None, fee_type=None, notes=None, other_fee_type=None, overdraft_control_indicator=None):  # noqa: E501
        """OverdraftOverdraftFeeChargeCap - a model defined in Swagger"""  # noqa: E501

        self._capping_period = None
        self._fee_cap_amount = None
        self._fee_cap_occurrence = None
        self._fee_min_max_type = None
        self._fee_type = None
        self._notes = None
        self._other_fee_type = None
        self._overdraft_control_indicator = None
        self.discriminator = None

        if capping_period is not None:
            self.capping_period = capping_period
        if fee_cap_amount is not None:
            self.fee_cap_amount = fee_cap_amount
        if fee_cap_occurrence is not None:
            self.fee_cap_occurrence = fee_cap_occurrence
        if fee_min_max_type is not None:
            self.fee_min_max_type = fee_min_max_type
        if fee_type is not None:
            self.fee_type = fee_type
        if notes is not None:
            self.notes = notes
        if other_fee_type is not None:
            self.other_fee_type = other_fee_type
        if overdraft_control_indicator is not None:
            self.overdraft_control_indicator = overdraft_control_indicator

    @property
    def capping_period(self):
        """Gets the capping_period of this OverdraftOverdraftFeeChargeCap.  # noqa: E501


        :return: The capping_period of this OverdraftOverdraftFeeChargeCap.  # noqa: E501
        :rtype: str
        """
        return self._capping_period

    @capping_period.setter
    def capping_period(self, capping_period):
        """Sets the capping_period of this OverdraftOverdraftFeeChargeCap.


        :param capping_period: The capping_period of this OverdraftOverdraftFeeChargeCap.  # noqa: E501
        :type: str
        """
        allowed_values = ["Day", "Half Year", "Month", "Quarter", "Week", "Year"]  # noqa: E501
        if capping_period not in allowed_values:
            raise ValueError(
                "Invalid value for `capping_period` ({0}), must be one of {1}"  # noqa: E501
                .format(capping_period, allowed_values)
            )

        self._capping_period = capping_period

    @property
    def fee_cap_amount(self):
        """Gets the fee_cap_amount of this OverdraftOverdraftFeeChargeCap.  # noqa: E501


        :return: The fee_cap_amount of this OverdraftOverdraftFeeChargeCap.  # noqa: E501
        :rtype: str
        """
        return self._fee_cap_amount

    @fee_cap_amount.setter
    def fee_cap_amount(self, fee_cap_amount):
        """Sets the fee_cap_amount of this OverdraftOverdraftFeeChargeCap.


        :param fee_cap_amount: The fee_cap_amount of this OverdraftOverdraftFeeChargeCap.  # noqa: E501
        :type: str
        """

        self._fee_cap_amount = fee_cap_amount

    @property
    def fee_cap_occurrence(self):
        """Gets the fee_cap_occurrence of this OverdraftOverdraftFeeChargeCap.  # noqa: E501


        :return: The fee_cap_occurrence of this OverdraftOverdraftFeeChargeCap.  # noqa: E501
        :rtype: float
        """
        return self._fee_cap_occurrence

    @fee_cap_occurrence.setter
    def fee_cap_occurrence(self, fee_cap_occurrence):
        """Sets the fee_cap_occurrence of this OverdraftOverdraftFeeChargeCap.


        :param fee_cap_occurrence: The fee_cap_occurrence of this OverdraftOverdraftFeeChargeCap.  # noqa: E501
        :type: float
        """

        self._fee_cap_occurrence = fee_cap_occurrence

    @property
    def fee_min_max_type(self):
        """Gets the fee_min_max_type of this OverdraftOverdraftFeeChargeCap.  # noqa: E501


        :return: The fee_min_max_type of this OverdraftOverdraftFeeChargeCap.  # noqa: E501
        :rtype: str
        """
        return self._fee_min_max_type

    @fee_min_max_type.setter
    def fee_min_max_type(self, fee_min_max_type):
        """Sets the fee_min_max_type of this OverdraftOverdraftFeeChargeCap.


        :param fee_min_max_type: The fee_min_max_type of this OverdraftOverdraftFeeChargeCap.  # noqa: E501
        :type: str
        """
        allowed_values = ["Minimum", "Maximum"]  # noqa: E501
        if fee_min_max_type not in allowed_values:
            raise ValueError(
                "Invalid value for `fee_min_max_type` ({0}), must be one of {1}"  # noqa: E501
                .format(fee_min_max_type, allowed_values)
            )

        self._fee_min_max_type = fee_min_max_type

    @property
    def fee_type(self):
        """Gets the fee_type of this OverdraftOverdraftFeeChargeCap.  # noqa: E501


        :return: The fee_type of this OverdraftOverdraftFeeChargeCap.  # noqa: E501
        :rtype: list[str]
        """
        return self._fee_type

    @fee_type.setter
    def fee_type(self, fee_type):
        """Sets the fee_type of this OverdraftOverdraftFeeChargeCap.


        :param fee_type: The fee_type of this OverdraftOverdraftFeeChargeCap.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ArrangedOverdraft", "EmergencyBorrowing", "BorrowingItem", "OverdraftRenewal", "AnnualReview", "OverdraftSetup", "Surcharge", "TempOverdraft", "UnauthorisedBorrowing", "UnauthorisedPaidTrans", "UnauthorisedUnpaidTrans"]  # noqa: E501
        if not set(fee_type).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `fee_type` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(fee_type) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._fee_type = fee_type

    @property
    def notes(self):
        """Gets the notes of this OverdraftOverdraftFeeChargeCap.  # noqa: E501


        :return: The notes of this OverdraftOverdraftFeeChargeCap.  # noqa: E501
        :rtype: list[str]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this OverdraftOverdraftFeeChargeCap.


        :param notes: The notes of this OverdraftOverdraftFeeChargeCap.  # noqa: E501
        :type: list[str]
        """

        self._notes = notes

    @property
    def other_fee_type(self):
        """Gets the other_fee_type of this OverdraftOverdraftFeeChargeCap.  # noqa: E501


        :return: The other_fee_type of this OverdraftOverdraftFeeChargeCap.  # noqa: E501
        :rtype: list[OverdraftOtherFeeType]
        """
        return self._other_fee_type

    @other_fee_type.setter
    def other_fee_type(self, other_fee_type):
        """Sets the other_fee_type of this OverdraftOverdraftFeeChargeCap.


        :param other_fee_type: The other_fee_type of this OverdraftOverdraftFeeChargeCap.  # noqa: E501
        :type: list[OverdraftOtherFeeType]
        """

        self._other_fee_type = other_fee_type

    @property
    def overdraft_control_indicator(self):
        """Gets the overdraft_control_indicator of this OverdraftOverdraftFeeChargeCap.  # noqa: E501


        :return: The overdraft_control_indicator of this OverdraftOverdraftFeeChargeCap.  # noqa: E501
        :rtype: bool
        """
        return self._overdraft_control_indicator

    @overdraft_control_indicator.setter
    def overdraft_control_indicator(self, overdraft_control_indicator):
        """Sets the overdraft_control_indicator of this OverdraftOverdraftFeeChargeCap.


        :param overdraft_control_indicator: The overdraft_control_indicator of this OverdraftOverdraftFeeChargeCap.  # noqa: E501
        :type: bool
        """

        self._overdraft_control_indicator = overdraft_control_indicator

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, OverdraftOverdraftFeeChargeCap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
