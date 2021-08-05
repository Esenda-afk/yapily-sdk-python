# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.396
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class InternationalPaymentRequest(object):
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
        'currency_of_transfer': 'str',
        'exchange_rate_information': 'ExchangeRateInformation',
        'purpose': 'str',
        'priority': 'str',
        'charge_bearer': 'str'
    }

    attribute_map = {
        'currency_of_transfer': 'currencyOfTransfer',
        'exchange_rate_information': 'exchangeRateInformation',
        'purpose': 'purpose',
        'priority': 'priority',
        'charge_bearer': 'chargeBearer'
    }

    def __init__(self, currency_of_transfer=None, exchange_rate_information=None, purpose=None, priority=None, charge_bearer=None, local_vars_configuration=None):  # noqa: E501
        """InternationalPaymentRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._currency_of_transfer = None
        self._exchange_rate_information = None
        self._purpose = None
        self._priority = None
        self._charge_bearer = None
        self.discriminator = None

        self.currency_of_transfer = currency_of_transfer
        if exchange_rate_information is not None:
            self.exchange_rate_information = exchange_rate_information
        if purpose is not None:
            self.purpose = purpose
        if priority is not None:
            self.priority = priority
        if charge_bearer is not None:
            self.charge_bearer = charge_bearer

    @property
    def currency_of_transfer(self):
        """Gets the currency_of_transfer of this InternationalPaymentRequest.  # noqa: E501


        :return: The currency_of_transfer of this InternationalPaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency_of_transfer

    @currency_of_transfer.setter
    def currency_of_transfer(self, currency_of_transfer):
        """Sets the currency_of_transfer of this InternationalPaymentRequest.


        :param currency_of_transfer: The currency_of_transfer of this InternationalPaymentRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency_of_transfer is None:  # noqa: E501
            raise ValueError("Invalid value for `currency_of_transfer`, must not be `None`")  # noqa: E501

        self._currency_of_transfer = currency_of_transfer

    @property
    def exchange_rate_information(self):
        """Gets the exchange_rate_information of this InternationalPaymentRequest.  # noqa: E501


        :return: The exchange_rate_information of this InternationalPaymentRequest.  # noqa: E501
        :rtype: ExchangeRateInformation
        """
        return self._exchange_rate_information

    @exchange_rate_information.setter
    def exchange_rate_information(self, exchange_rate_information):
        """Sets the exchange_rate_information of this InternationalPaymentRequest.


        :param exchange_rate_information: The exchange_rate_information of this InternationalPaymentRequest.  # noqa: E501
        :type: ExchangeRateInformation
        """

        self._exchange_rate_information = exchange_rate_information

    @property
    def purpose(self):
        """Gets the purpose of this InternationalPaymentRequest.  # noqa: E501


        :return: The purpose of this InternationalPaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """Sets the purpose of this InternationalPaymentRequest.


        :param purpose: The purpose of this InternationalPaymentRequest.  # noqa: E501
        :type: str
        """

        self._purpose = purpose

    @property
    def priority(self):
        """Gets the priority of this InternationalPaymentRequest.  # noqa: E501


        :return: The priority of this InternationalPaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this InternationalPaymentRequest.


        :param priority: The priority of this InternationalPaymentRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["NORMAL", "URGENT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and priority not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `priority` ({0}), must be one of {1}"  # noqa: E501
                .format(priority, allowed_values)
            )

        self._priority = priority

    @property
    def charge_bearer(self):
        """Gets the charge_bearer of this InternationalPaymentRequest.  # noqa: E501


        :return: The charge_bearer of this InternationalPaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._charge_bearer

    @charge_bearer.setter
    def charge_bearer(self, charge_bearer):
        """Sets the charge_bearer of this InternationalPaymentRequest.


        :param charge_bearer: The charge_bearer of this InternationalPaymentRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEBT", "CRED", "SHAR", "SLEV"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and charge_bearer not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `charge_bearer` ({0}), must be one of {1}"  # noqa: E501
                .format(charge_bearer, allowed_values)
            )

        self._charge_bearer = charge_bearer

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
        if not isinstance(other, InternationalPaymentRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InternationalPaymentRequest):
            return True

        return self.to_dict() != other.to_dict()
