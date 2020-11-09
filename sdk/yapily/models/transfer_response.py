# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.271
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class TransferResponse(object):
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
        'from_account_id': 'str',
        'to_account_id': 'str',
        'status': 'str',
        'created_at': 'datetime',
        'reference': 'str',
        'balance': 'float',
        'currency': 'str'
    }

    attribute_map = {
        'from_account_id': 'fromAccountId',
        'to_account_id': 'toAccountId',
        'status': 'status',
        'created_at': 'createdAt',
        'reference': 'reference',
        'balance': 'balance',
        'currency': 'currency'
    }

    def __init__(self, from_account_id=None, to_account_id=None, status=None, created_at=None, reference=None, balance=None, currency=None, local_vars_configuration=None):  # noqa: E501
        """TransferResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._from_account_id = None
        self._to_account_id = None
        self._status = None
        self._created_at = None
        self._reference = None
        self._balance = None
        self._currency = None
        self.discriminator = None

        if from_account_id is not None:
            self.from_account_id = from_account_id
        if to_account_id is not None:
            self.to_account_id = to_account_id
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if reference is not None:
            self.reference = reference
        if balance is not None:
            self.balance = balance
        if currency is not None:
            self.currency = currency

    @property
    def from_account_id(self):
        """Gets the from_account_id of this TransferResponse.  # noqa: E501


        :return: The from_account_id of this TransferResponse.  # noqa: E501
        :rtype: str
        """
        return self._from_account_id

    @from_account_id.setter
    def from_account_id(self, from_account_id):
        """Sets the from_account_id of this TransferResponse.


        :param from_account_id: The from_account_id of this TransferResponse.  # noqa: E501
        :type: str
        """

        self._from_account_id = from_account_id

    @property
    def to_account_id(self):
        """Gets the to_account_id of this TransferResponse.  # noqa: E501


        :return: The to_account_id of this TransferResponse.  # noqa: E501
        :rtype: str
        """
        return self._to_account_id

    @to_account_id.setter
    def to_account_id(self, to_account_id):
        """Sets the to_account_id of this TransferResponse.


        :param to_account_id: The to_account_id of this TransferResponse.  # noqa: E501
        :type: str
        """

        self._to_account_id = to_account_id

    @property
    def status(self):
        """Gets the status of this TransferResponse.  # noqa: E501


        :return: The status of this TransferResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TransferResponse.


        :param status: The status of this TransferResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["PENDING", "FAILED", "DECLINED", "COMPLETED", "UNKNOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this TransferResponse.  # noqa: E501


        :return: The created_at of this TransferResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TransferResponse.


        :param created_at: The created_at of this TransferResponse.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def reference(self):
        """Gets the reference of this TransferResponse.  # noqa: E501


        :return: The reference of this TransferResponse.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this TransferResponse.


        :param reference: The reference of this TransferResponse.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def balance(self):
        """Gets the balance of this TransferResponse.  # noqa: E501


        :return: The balance of this TransferResponse.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this TransferResponse.


        :param balance: The balance of this TransferResponse.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def currency(self):
        """Gets the currency of this TransferResponse.  # noqa: E501


        :return: The currency of this TransferResponse.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this TransferResponse.


        :param currency: The currency of this TransferResponse.  # noqa: E501
        :type: str
        """

        self._currency = currency

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
        if not isinstance(other, TransferResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransferResponse):
            return True

        return self.to_dict() != other.to_dict()
