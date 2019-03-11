# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.94
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TransferRequest(object):
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
        'account_id': 'str',
        'amount': 'float',
        'currency': 'str',
        'reference': 'str',
        'transfer_reference_id': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'amount': 'amount',
        'currency': 'currency',
        'reference': 'reference',
        'transfer_reference_id': 'transferReferenceId'
    }

    def __init__(self, account_id=None, amount=None, currency=None, reference=None, transfer_reference_id=None):  # noqa: E501
        """TransferRequest - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._amount = None
        self._currency = None
        self._reference = None
        self._transfer_reference_id = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if reference is not None:
            self.reference = reference
        if transfer_reference_id is not None:
            self.transfer_reference_id = transfer_reference_id

    @property
    def account_id(self):
        """Gets the account_id of this TransferRequest.  # noqa: E501


        :return: The account_id of this TransferRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this TransferRequest.


        :param account_id: The account_id of this TransferRequest.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def amount(self):
        """Gets the amount of this TransferRequest.  # noqa: E501


        :return: The amount of this TransferRequest.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TransferRequest.


        :param amount: The amount of this TransferRequest.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this TransferRequest.  # noqa: E501


        :return: The currency of this TransferRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this TransferRequest.


        :param currency: The currency of this TransferRequest.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def reference(self):
        """Gets the reference of this TransferRequest.  # noqa: E501


        :return: The reference of this TransferRequest.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this TransferRequest.


        :param reference: The reference of this TransferRequest.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def transfer_reference_id(self):
        """Gets the transfer_reference_id of this TransferRequest.  # noqa: E501


        :return: The transfer_reference_id of this TransferRequest.  # noqa: E501
        :rtype: str
        """
        return self._transfer_reference_id

    @transfer_reference_id.setter
    def transfer_reference_id(self, transfer_reference_id):
        """Sets the transfer_reference_id of this TransferRequest.


        :param transfer_reference_id: The transfer_reference_id of this TransferRequest.  # noqa: E501
        :type: str
        """

        self._transfer_reference_id = transfer_reference_id

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
        if not isinstance(other, TransferRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
