# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.344
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class CreditInterestCreditInterestEligibility(object):
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
        'amount': 'str',
        'description': 'str',
        'indicator': 'bool',
        'name': 'str',
        'notes': 'list[str]',
        'other_type': 'OtherType',
        'period': 'str',
        'textual': 'str',
        'type': 'str'
    }

    attribute_map = {
        'amount': 'Amount',
        'description': 'Description',
        'indicator': 'Indicator',
        'name': 'Name',
        'notes': 'Notes',
        'other_type': 'OtherType',
        'period': 'Period',
        'textual': 'Textual',
        'type': 'Type'
    }

    def __init__(self, amount=None, description=None, indicator=None, name=None, notes=None, other_type=None, period=None, textual=None, type=None, local_vars_configuration=None):  # noqa: E501
        """CreditInterestCreditInterestEligibility - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amount = None
        self._description = None
        self._indicator = None
        self._name = None
        self._notes = None
        self._other_type = None
        self._period = None
        self._textual = None
        self._type = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if description is not None:
            self.description = description
        if indicator is not None:
            self.indicator = indicator
        if name is not None:
            self.name = name
        if notes is not None:
            self.notes = notes
        if other_type is not None:
            self.other_type = other_type
        if period is not None:
            self.period = period
        if textual is not None:
            self.textual = textual
        if type is not None:
            self.type = type

    @property
    def amount(self):
        """Gets the amount of this CreditInterestCreditInterestEligibility.  # noqa: E501


        :return: The amount of this CreditInterestCreditInterestEligibility.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CreditInterestCreditInterestEligibility.


        :param amount: The amount of this CreditInterestCreditInterestEligibility.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def description(self):
        """Gets the description of this CreditInterestCreditInterestEligibility.  # noqa: E501


        :return: The description of this CreditInterestCreditInterestEligibility.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreditInterestCreditInterestEligibility.


        :param description: The description of this CreditInterestCreditInterestEligibility.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def indicator(self):
        """Gets the indicator of this CreditInterestCreditInterestEligibility.  # noqa: E501


        :return: The indicator of this CreditInterestCreditInterestEligibility.  # noqa: E501
        :rtype: bool
        """
        return self._indicator

    @indicator.setter
    def indicator(self, indicator):
        """Sets the indicator of this CreditInterestCreditInterestEligibility.


        :param indicator: The indicator of this CreditInterestCreditInterestEligibility.  # noqa: E501
        :type: bool
        """

        self._indicator = indicator

    @property
    def name(self):
        """Gets the name of this CreditInterestCreditInterestEligibility.  # noqa: E501


        :return: The name of this CreditInterestCreditInterestEligibility.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreditInterestCreditInterestEligibility.


        :param name: The name of this CreditInterestCreditInterestEligibility.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this CreditInterestCreditInterestEligibility.  # noqa: E501


        :return: The notes of this CreditInterestCreditInterestEligibility.  # noqa: E501
        :rtype: list[str]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this CreditInterestCreditInterestEligibility.


        :param notes: The notes of this CreditInterestCreditInterestEligibility.  # noqa: E501
        :type: list[str]
        """

        self._notes = notes

    @property
    def other_type(self):
        """Gets the other_type of this CreditInterestCreditInterestEligibility.  # noqa: E501


        :return: The other_type of this CreditInterestCreditInterestEligibility.  # noqa: E501
        :rtype: OtherType
        """
        return self._other_type

    @other_type.setter
    def other_type(self, other_type):
        """Sets the other_type of this CreditInterestCreditInterestEligibility.


        :param other_type: The other_type of this CreditInterestCreditInterestEligibility.  # noqa: E501
        :type: OtherType
        """

        self._other_type = other_type

    @property
    def period(self):
        """Gets the period of this CreditInterestCreditInterestEligibility.  # noqa: E501


        :return: The period of this CreditInterestCreditInterestEligibility.  # noqa: E501
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this CreditInterestCreditInterestEligibility.


        :param period: The period of this CreditInterestCreditInterestEligibility.  # noqa: E501
        :type: str
        """
        allowed_values = ["Day", "Half Year", "Month", "Quarter", "Week", "AcademicTerm", "Year"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and period not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `period` ({0}), must be one of {1}"  # noqa: E501
                .format(period, allowed_values)
            )

        self._period = period

    @property
    def textual(self):
        """Gets the textual of this CreditInterestCreditInterestEligibility.  # noqa: E501


        :return: The textual of this CreditInterestCreditInterestEligibility.  # noqa: E501
        :rtype: str
        """
        return self._textual

    @textual.setter
    def textual(self, textual):
        """Sets the textual of this CreditInterestCreditInterestEligibility.


        :param textual: The textual of this CreditInterestCreditInterestEligibility.  # noqa: E501
        :type: str
        """

        self._textual = textual

    @property
    def type(self):
        """Gets the type of this CreditInterestCreditInterestEligibility.  # noqa: E501


        :return: The type of this CreditInterestCreditInterestEligibility.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreditInterestCreditInterestEligibility.


        :param type: The type of this CreditInterestCreditInterestEligibility.  # noqa: E501
        :type: str
        """
        allowed_values = ["DirectDebits", "ExistingCustomers", "MinimumOperatingBalance", "MinimumDeposit", "NewCustomersOnly", "PreviousBankruptcyAllowed", "Other", "StudentsOnly", "SoleStudentAccount", "SoleUkAccount", "SwitchersOnly", "UCASFulltimeTwoYears"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, CreditInterestCreditInterestEligibility):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreditInterestCreditInterestEligibility):
            return True

        return self.to_dict() != other.to_dict()
