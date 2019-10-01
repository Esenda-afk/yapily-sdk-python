# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.146
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from yapily.models.account_identification import AccountIdentification  # noqa: F401,E501
from yapily.models.amount import Amount  # noqa: F401,E501
from yapily.models.payee import Payee  # noqa: F401,E501


class PaymentRequest(object):
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
        'payment_idempotency_id': 'str',
        'payer_account_identifications': 'list[AccountIdentification]',
        'amount': 'Amount',
        'reference': 'str',
        'context_type': 'str',
        'type': 'str',
        'payment_date_time': 'datetime',
        'payee': 'Payee'
    }

    attribute_map = {
        'payment_idempotency_id': 'paymentIdempotencyId',
        'payer_account_identifications': 'payerAccountIdentifications',
        'amount': 'amount',
        'reference': 'reference',
        'context_type': 'contextType',
        'type': 'type',
        'payment_date_time': 'paymentDateTime',
        'payee': 'payee'
    }

    def __init__(self, payment_idempotency_id=None, payer_account_identifications=None, amount=None, reference=None, context_type=None, type=None, payment_date_time=None, payee=None):  # noqa: E501
        """PaymentRequest - a model defined in Swagger"""  # noqa: E501

        self._payment_idempotency_id = None
        self._payer_account_identifications = None
        self._amount = None
        self._reference = None
        self._context_type = None
        self._type = None
        self._payment_date_time = None
        self._payee = None
        self.discriminator = None

        self.payment_idempotency_id = payment_idempotency_id
        if payer_account_identifications is not None:
            self.payer_account_identifications = payer_account_identifications
        if amount is not None:
            self.amount = amount
        if reference is not None:
            self.reference = reference
        if context_type is not None:
            self.context_type = context_type
        if type is not None:
            self.type = type
        if payment_date_time is not None:
            self.payment_date_time = payment_date_time
        self.payee = payee

    @property
    def payment_idempotency_id(self):
        """Gets the payment_idempotency_id of this PaymentRequest.  # noqa: E501


        :return: The payment_idempotency_id of this PaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._payment_idempotency_id

    @payment_idempotency_id.setter
    def payment_idempotency_id(self, payment_idempotency_id):
        """Sets the payment_idempotency_id of this PaymentRequest.


        :param payment_idempotency_id: The payment_idempotency_id of this PaymentRequest.  # noqa: E501
        :type: str
        """
        if payment_idempotency_id is None:
            raise ValueError("Invalid value for `payment_idempotency_id`, must not be `None`")  # noqa: E501

        self._payment_idempotency_id = payment_idempotency_id

    @property
    def payer_account_identifications(self):
        """Gets the payer_account_identifications of this PaymentRequest.  # noqa: E501


        :return: The payer_account_identifications of this PaymentRequest.  # noqa: E501
        :rtype: list[AccountIdentification]
        """
        return self._payer_account_identifications

    @payer_account_identifications.setter
    def payer_account_identifications(self, payer_account_identifications):
        """Sets the payer_account_identifications of this PaymentRequest.


        :param payer_account_identifications: The payer_account_identifications of this PaymentRequest.  # noqa: E501
        :type: list[AccountIdentification]
        """

        self._payer_account_identifications = payer_account_identifications

    @property
    def amount(self):
        """Gets the amount of this PaymentRequest.  # noqa: E501


        :return: The amount of this PaymentRequest.  # noqa: E501
        :rtype: Amount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentRequest.


        :param amount: The amount of this PaymentRequest.  # noqa: E501
        :type: Amount
        """

        self._amount = amount

    @property
    def reference(self):
        """Gets the reference of this PaymentRequest.  # noqa: E501


        :return: The reference of this PaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this PaymentRequest.


        :param reference: The reference of this PaymentRequest.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def context_type(self):
        """Gets the context_type of this PaymentRequest.  # noqa: E501


        :return: The context_type of this PaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._context_type

    @context_type.setter
    def context_type(self, context_type):
        """Sets the context_type of this PaymentRequest.


        :param context_type: The context_type of this PaymentRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["BILL", "GOODS", "SERVICES", "OTHER", "PERSON_TO_PERSON"]  # noqa: E501
        if context_type not in allowed_values:
            raise ValueError(
                "Invalid value for `context_type` ({0}), must be one of {1}"  # noqa: E501
                .format(context_type, allowed_values)
            )

        self._context_type = context_type

    @property
    def type(self):
        """Gets the type of this PaymentRequest.  # noqa: E501


        :return: The type of this PaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PaymentRequest.


        :param type: The type of this PaymentRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["DOMESTIC_PAYMENT", "DOMESTIC_VARIABLE_RECURRING_PAYMENT", "DOMESTIC_SCHEDULED_PAYMENT"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def payment_date_time(self):
        """Gets the payment_date_time of this PaymentRequest.  # noqa: E501


        :return: The payment_date_time of this PaymentRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._payment_date_time

    @payment_date_time.setter
    def payment_date_time(self, payment_date_time):
        """Sets the payment_date_time of this PaymentRequest.


        :param payment_date_time: The payment_date_time of this PaymentRequest.  # noqa: E501
        :type: datetime
        """

        self._payment_date_time = payment_date_time

    @property
    def payee(self):
        """Gets the payee of this PaymentRequest.  # noqa: E501


        :return: The payee of this PaymentRequest.  # noqa: E501
        :rtype: Payee
        """
        return self._payee

    @payee.setter
    def payee(self, payee):
        """Sets the payee of this PaymentRequest.


        :param payee: The payee of this PaymentRequest.  # noqa: E501
        :type: Payee
        """
        if payee is None:
            raise ValueError("Invalid value for `payee`, must not be `None`")  # noqa: E501

        self._payee = payee

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
        if not isinstance(other, PaymentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
