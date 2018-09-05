# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.32
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SortCodePaymentRequest(object):
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
        'sender_account_id': 'str',
        'name': 'str',
        'amount': 'float',
        'currency': 'str',
        'reference': 'str',
        'country': 'str',
        'payment_reference_id': 'str',
        'account_number': 'str',
        'sort_code': 'str'
    }

    attribute_map = {
        'sender_account_id': 'senderAccountId',
        'name': 'name',
        'amount': 'amount',
        'currency': 'currency',
        'reference': 'reference',
        'country': 'country',
        'payment_reference_id': 'paymentReferenceId',
        'account_number': 'accountNumber',
        'sort_code': 'sortCode'
    }

    def __init__(self, sender_account_id=None, name=None, amount=None, currency=None, reference=None, country=None, payment_reference_id=None, account_number=None, sort_code=None):  # noqa: E501
        """SortCodePaymentRequest - a model defined in Swagger"""  # noqa: E501

        self._sender_account_id = None
        self._name = None
        self._amount = None
        self._currency = None
        self._reference = None
        self._country = None
        self._payment_reference_id = None
        self._account_number = None
        self._sort_code = None
        self.discriminator = None

        if sender_account_id is not None:
            self.sender_account_id = sender_account_id
        if name is not None:
            self.name = name
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if reference is not None:
            self.reference = reference
        if country is not None:
            self.country = country
        if payment_reference_id is not None:
            self.payment_reference_id = payment_reference_id
        if account_number is not None:
            self.account_number = account_number
        if sort_code is not None:
            self.sort_code = sort_code

    @property
    def sender_account_id(self):
        """Gets the sender_account_id of this SortCodePaymentRequest.  # noqa: E501


        :return: The sender_account_id of this SortCodePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._sender_account_id

    @sender_account_id.setter
    def sender_account_id(self, sender_account_id):
        """Sets the sender_account_id of this SortCodePaymentRequest.


        :param sender_account_id: The sender_account_id of this SortCodePaymentRequest.  # noqa: E501
        :type: str
        """

        self._sender_account_id = sender_account_id

    @property
    def name(self):
        """Gets the name of this SortCodePaymentRequest.  # noqa: E501


        :return: The name of this SortCodePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SortCodePaymentRequest.


        :param name: The name of this SortCodePaymentRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def amount(self):
        """Gets the amount of this SortCodePaymentRequest.  # noqa: E501


        :return: The amount of this SortCodePaymentRequest.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SortCodePaymentRequest.


        :param amount: The amount of this SortCodePaymentRequest.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this SortCodePaymentRequest.  # noqa: E501


        :return: The currency of this SortCodePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this SortCodePaymentRequest.


        :param currency: The currency of this SortCodePaymentRequest.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def reference(self):
        """Gets the reference of this SortCodePaymentRequest.  # noqa: E501


        :return: The reference of this SortCodePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this SortCodePaymentRequest.


        :param reference: The reference of this SortCodePaymentRequest.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def country(self):
        """Gets the country of this SortCodePaymentRequest.  # noqa: E501


        :return: The country of this SortCodePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this SortCodePaymentRequest.


        :param country: The country of this SortCodePaymentRequest.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def payment_reference_id(self):
        """Gets the payment_reference_id of this SortCodePaymentRequest.  # noqa: E501


        :return: The payment_reference_id of this SortCodePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._payment_reference_id

    @payment_reference_id.setter
    def payment_reference_id(self, payment_reference_id):
        """Sets the payment_reference_id of this SortCodePaymentRequest.


        :param payment_reference_id: The payment_reference_id of this SortCodePaymentRequest.  # noqa: E501
        :type: str
        """

        self._payment_reference_id = payment_reference_id

    @property
    def account_number(self):
        """Gets the account_number of this SortCodePaymentRequest.  # noqa: E501


        :return: The account_number of this SortCodePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this SortCodePaymentRequest.


        :param account_number: The account_number of this SortCodePaymentRequest.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def sort_code(self):
        """Gets the sort_code of this SortCodePaymentRequest.  # noqa: E501


        :return: The sort_code of this SortCodePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_code

    @sort_code.setter
    def sort_code(self, sort_code):
        """Sets the sort_code of this SortCodePaymentRequest.


        :param sort_code: The sort_code of this SortCodePaymentRequest.  # noqa: E501
        :type: str
        """

        self._sort_code = sort_code

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
        if not isinstance(other, SortCodePaymentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
