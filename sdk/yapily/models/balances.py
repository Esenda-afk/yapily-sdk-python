# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.224
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class Balances(object):
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
        'main_balance_amount': 'Amount',
        'balances': 'list[AccountBalance]'
    }

    attribute_map = {
        'main_balance_amount': 'mainBalanceAmount',
        'balances': 'balances'
    }

    def __init__(self, main_balance_amount=None, balances=None, local_vars_configuration=None):  # noqa: E501
        """Balances - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._main_balance_amount = None
        self._balances = None
        self.discriminator = None

        if main_balance_amount is not None:
            self.main_balance_amount = main_balance_amount
        if balances is not None:
            self.balances = balances

    @property
    def main_balance_amount(self):
        """Gets the main_balance_amount of this Balances.  # noqa: E501


        :return: The main_balance_amount of this Balances.  # noqa: E501
        :rtype: Amount
        """
        return self._main_balance_amount

    @main_balance_amount.setter
    def main_balance_amount(self, main_balance_amount):
        """Sets the main_balance_amount of this Balances.


        :param main_balance_amount: The main_balance_amount of this Balances.  # noqa: E501
        :type: Amount
        """

        self._main_balance_amount = main_balance_amount

    @property
    def balances(self):
        """Gets the balances of this Balances.  # noqa: E501


        :return: The balances of this Balances.  # noqa: E501
        :rtype: list[AccountBalance]
        """
        return self._balances

    @balances.setter
    def balances(self, balances):
        """Sets the balances of this Balances.


        :param balances: The balances of this Balances.  # noqa: E501
        :type: list[AccountBalance]
        """

        self._balances = balances

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
        if not isinstance(other, Balances):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Balances):
            return True

        return self.to_dict() != other.to_dict()
