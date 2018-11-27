# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.46
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PaymentResponse(object):
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
        'id': 'str',
        'status': 'str',
        'created_at': 'datetime',
        'reference': 'str',
        'amount': 'float',
        'currency': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'created_at': 'createdAt',
        'reference': 'reference',
        'amount': 'amount',
        'currency': 'currency'
    }

    def __init__(self, id=None, status=None, created_at=None, reference=None, amount=None, currency=None):  # noqa: E501
        """PaymentResponse - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._status = None
        self._created_at = None
        self._reference = None
        self._amount = None
        self._currency = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if reference is not None:
            self.reference = reference
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency

    @property
    def id(self):
        """Gets the id of this PaymentResponse.  # noqa: E501


        :return: The id of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentResponse.


        :param id: The id of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this PaymentResponse.  # noqa: E501


        :return: The status of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PaymentResponse.


        :param status: The status of this PaymentResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["PENDING", "FAILED", "DECLINED", "COMPLETED", "EXPIRED", "UNKNOWN"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this PaymentResponse.  # noqa: E501


        :return: The created_at of this PaymentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PaymentResponse.


        :param created_at: The created_at of this PaymentResponse.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def reference(self):
        """Gets the reference of this PaymentResponse.  # noqa: E501


        :return: The reference of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this PaymentResponse.


        :param reference: The reference of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def amount(self):
        """Gets the amount of this PaymentResponse.  # noqa: E501


        :return: The amount of this PaymentResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentResponse.


        :param amount: The amount of this PaymentResponse.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this PaymentResponse.  # noqa: E501


        :return: The currency of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PaymentResponse.


        :param currency: The currency of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._currency = currency

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
        if not isinstance(other, PaymentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
