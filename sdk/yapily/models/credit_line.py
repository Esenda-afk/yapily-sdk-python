# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.210
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class CreditLine(object):
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
        'type': 'str',
        'credit_line_amount': 'Amount'
    }

    attribute_map = {
        'type': 'type',
        'credit_line_amount': 'creditLineAmount'
    }

    def __init__(self, type=None, credit_line_amount=None, local_vars_configuration=None):  # noqa: E501
        """CreditLine - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._credit_line_amount = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if credit_line_amount is not None:
            self.credit_line_amount = credit_line_amount

    @property
    def type(self):
        """Gets the type of this CreditLine.  # noqa: E501


        :return: The type of this CreditLine.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreditLine.


        :param type: The type of this CreditLine.  # noqa: E501
        :type: str
        """
        allowed_values = ["AVAILABLE", "CREDIT", "EMERGENCY", "PRE_AGREED", "TEMPORARY", "OTHER", "UNKNOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def credit_line_amount(self):
        """Gets the credit_line_amount of this CreditLine.  # noqa: E501


        :return: The credit_line_amount of this CreditLine.  # noqa: E501
        :rtype: Amount
        """
        return self._credit_line_amount

    @credit_line_amount.setter
    def credit_line_amount(self, credit_line_amount):
        """Sets the credit_line_amount of this CreditLine.


        :param credit_line_amount: The credit_line_amount of this CreditLine.  # noqa: E501
        :type: Amount
        """

        self._credit_line_amount = credit_line_amount

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
        if not isinstance(other, CreditLine):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreditLine):
            return True

        return self.to_dict() != other.to_dict()
