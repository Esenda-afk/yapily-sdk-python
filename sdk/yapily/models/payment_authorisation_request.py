# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.333
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class PaymentAuthorisationRequest(object):
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
        'user_uuid': 'str',
        'application_user_id': 'str',
        'forward_parameters': 'list[str]',
        'institution_id': 'str',
        'callback': 'str',
        'one_time_token': 'bool',
        'total_max_amount': 'float',
        'total_max_amount_frequency': 'str',
        'max_amount_per_request': 'float',
        'starts_at': 'datetime',
        'expires_at': 'datetime',
        'allow_overdraft': 'bool',
        'payment_request': 'PaymentRequest'
    }

    attribute_map = {
        'user_uuid': 'userUuid',
        'application_user_id': 'applicationUserId',
        'forward_parameters': 'forwardParameters',
        'institution_id': 'institutionId',
        'callback': 'callback',
        'one_time_token': 'oneTimeToken',
        'total_max_amount': 'totalMaxAmount',
        'total_max_amount_frequency': 'totalMaxAmountFrequency',
        'max_amount_per_request': 'maxAmountPerRequest',
        'starts_at': 'startsAt',
        'expires_at': 'expiresAt',
        'allow_overdraft': 'allowOverdraft',
        'payment_request': 'paymentRequest'
    }

    def __init__(self, user_uuid=None, application_user_id=None, forward_parameters=None, institution_id=None, callback=None, one_time_token=None, total_max_amount=None, total_max_amount_frequency=None, max_amount_per_request=None, starts_at=None, expires_at=None, allow_overdraft=None, payment_request=None, local_vars_configuration=None):  # noqa: E501
        """PaymentAuthorisationRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_uuid = None
        self._application_user_id = None
        self._forward_parameters = None
        self._institution_id = None
        self._callback = None
        self._one_time_token = None
        self._total_max_amount = None
        self._total_max_amount_frequency = None
        self._max_amount_per_request = None
        self._starts_at = None
        self._expires_at = None
        self._allow_overdraft = None
        self._payment_request = None
        self.discriminator = None

        if user_uuid is not None:
            self.user_uuid = user_uuid
        if application_user_id is not None:
            self.application_user_id = application_user_id
        if forward_parameters is not None:
            self.forward_parameters = forward_parameters
        self.institution_id = institution_id
        self.callback = callback
        self.one_time_token = one_time_token
        if total_max_amount is not None:
            self.total_max_amount = total_max_amount
        if total_max_amount_frequency is not None:
            self.total_max_amount_frequency = total_max_amount_frequency
        if max_amount_per_request is not None:
            self.max_amount_per_request = max_amount_per_request
        if starts_at is not None:
            self.starts_at = starts_at
        if expires_at is not None:
            self.expires_at = expires_at
        if allow_overdraft is not None:
            self.allow_overdraft = allow_overdraft
        self.payment_request = payment_request

    @property
    def user_uuid(self):
        """Gets the user_uuid of this PaymentAuthorisationRequest.  # noqa: E501

        Uuid of the application user who will authorise access to their data. Either the userUuid or applicationUserId must be provided.  # noqa: E501

        :return: The user_uuid of this PaymentAuthorisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this PaymentAuthorisationRequest.

        Uuid of the application user who will authorise access to their data. Either the userUuid or applicationUserId must be provided.  # noqa: E501

        :param user_uuid: The user_uuid of this PaymentAuthorisationRequest.  # noqa: E501
        :type: str
        """

        self._user_uuid = user_uuid

    @property
    def application_user_id(self):
        """Gets the application_user_id of this PaymentAuthorisationRequest.  # noqa: E501

        Descriptive identifier for the application user.Either the userUuid or applicationUserId must be provided.  # noqa: E501

        :return: The application_user_id of this PaymentAuthorisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._application_user_id

    @application_user_id.setter
    def application_user_id(self, application_user_id):
        """Sets the application_user_id of this PaymentAuthorisationRequest.

        Descriptive identifier for the application user.Either the userUuid or applicationUserId must be provided.  # noqa: E501

        :param application_user_id: The application_user_id of this PaymentAuthorisationRequest.  # noqa: E501
        :type: str
        """

        self._application_user_id = application_user_id

    @property
    def forward_parameters(self):
        """Gets the forward_parameters of this PaymentAuthorisationRequest.  # noqa: E501


        :return: The forward_parameters of this PaymentAuthorisationRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._forward_parameters

    @forward_parameters.setter
    def forward_parameters(self, forward_parameters):
        """Sets the forward_parameters of this PaymentAuthorisationRequest.


        :param forward_parameters: The forward_parameters of this PaymentAuthorisationRequest.  # noqa: E501
        :type: list[str]
        """

        self._forward_parameters = forward_parameters

    @property
    def institution_id(self):
        """Gets the institution_id of this PaymentAuthorisationRequest.  # noqa: E501


        :return: The institution_id of this PaymentAuthorisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._institution_id

    @institution_id.setter
    def institution_id(self, institution_id):
        """Sets the institution_id of this PaymentAuthorisationRequest.


        :param institution_id: The institution_id of this PaymentAuthorisationRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and institution_id is None:  # noqa: E501
            raise ValueError("Invalid value for `institution_id`, must not be `None`")  # noqa: E501

        self._institution_id = institution_id

    @property
    def callback(self):
        """Gets the callback of this PaymentAuthorisationRequest.  # noqa: E501


        :return: The callback of this PaymentAuthorisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._callback

    @callback.setter
    def callback(self, callback):
        """Sets the callback of this PaymentAuthorisationRequest.


        :param callback: The callback of this PaymentAuthorisationRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and callback is None:  # noqa: E501
            raise ValueError("Invalid value for `callback`, must not be `None`")  # noqa: E501

        self._callback = callback

    @property
    def one_time_token(self):
        """Gets the one_time_token of this PaymentAuthorisationRequest.  # noqa: E501


        :return: The one_time_token of this PaymentAuthorisationRequest.  # noqa: E501
        :rtype: bool
        """
        return self._one_time_token

    @one_time_token.setter
    def one_time_token(self, one_time_token):
        """Sets the one_time_token of this PaymentAuthorisationRequest.


        :param one_time_token: The one_time_token of this PaymentAuthorisationRequest.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and one_time_token is None:  # noqa: E501
            raise ValueError("Invalid value for `one_time_token`, must not be `None`")  # noqa: E501

        self._one_time_token = one_time_token

    @property
    def total_max_amount(self):
        """Gets the total_max_amount of this PaymentAuthorisationRequest.  # noqa: E501


        :return: The total_max_amount of this PaymentAuthorisationRequest.  # noqa: E501
        :rtype: float
        """
        return self._total_max_amount

    @total_max_amount.setter
    def total_max_amount(self, total_max_amount):
        """Sets the total_max_amount of this PaymentAuthorisationRequest.


        :param total_max_amount: The total_max_amount of this PaymentAuthorisationRequest.  # noqa: E501
        :type: float
        """

        self._total_max_amount = total_max_amount

    @property
    def total_max_amount_frequency(self):
        """Gets the total_max_amount_frequency of this PaymentAuthorisationRequest.  # noqa: E501


        :return: The total_max_amount_frequency of this PaymentAuthorisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._total_max_amount_frequency

    @total_max_amount_frequency.setter
    def total_max_amount_frequency(self, total_max_amount_frequency):
        """Sets the total_max_amount_frequency of this PaymentAuthorisationRequest.


        :param total_max_amount_frequency: The total_max_amount_frequency of this PaymentAuthorisationRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["DAILY", "WEEKLY", "MONTHLY", "YEARLY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and total_max_amount_frequency not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `total_max_amount_frequency` ({0}), must be one of {1}"  # noqa: E501
                .format(total_max_amount_frequency, allowed_values)
            )

        self._total_max_amount_frequency = total_max_amount_frequency

    @property
    def max_amount_per_request(self):
        """Gets the max_amount_per_request of this PaymentAuthorisationRequest.  # noqa: E501


        :return: The max_amount_per_request of this PaymentAuthorisationRequest.  # noqa: E501
        :rtype: float
        """
        return self._max_amount_per_request

    @max_amount_per_request.setter
    def max_amount_per_request(self, max_amount_per_request):
        """Sets the max_amount_per_request of this PaymentAuthorisationRequest.


        :param max_amount_per_request: The max_amount_per_request of this PaymentAuthorisationRequest.  # noqa: E501
        :type: float
        """

        self._max_amount_per_request = max_amount_per_request

    @property
    def starts_at(self):
        """Gets the starts_at of this PaymentAuthorisationRequest.  # noqa: E501


        :return: The starts_at of this PaymentAuthorisationRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._starts_at

    @starts_at.setter
    def starts_at(self, starts_at):
        """Sets the starts_at of this PaymentAuthorisationRequest.


        :param starts_at: The starts_at of this PaymentAuthorisationRequest.  # noqa: E501
        :type: datetime
        """

        self._starts_at = starts_at

    @property
    def expires_at(self):
        """Gets the expires_at of this PaymentAuthorisationRequest.  # noqa: E501


        :return: The expires_at of this PaymentAuthorisationRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this PaymentAuthorisationRequest.


        :param expires_at: The expires_at of this PaymentAuthorisationRequest.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

    @property
    def allow_overdraft(self):
        """Gets the allow_overdraft of this PaymentAuthorisationRequest.  # noqa: E501


        :return: The allow_overdraft of this PaymentAuthorisationRequest.  # noqa: E501
        :rtype: bool
        """
        return self._allow_overdraft

    @allow_overdraft.setter
    def allow_overdraft(self, allow_overdraft):
        """Sets the allow_overdraft of this PaymentAuthorisationRequest.


        :param allow_overdraft: The allow_overdraft of this PaymentAuthorisationRequest.  # noqa: E501
        :type: bool
        """

        self._allow_overdraft = allow_overdraft

    @property
    def payment_request(self):
        """Gets the payment_request of this PaymentAuthorisationRequest.  # noqa: E501


        :return: The payment_request of this PaymentAuthorisationRequest.  # noqa: E501
        :rtype: PaymentRequest
        """
        return self._payment_request

    @payment_request.setter
    def payment_request(self, payment_request):
        """Sets the payment_request of this PaymentAuthorisationRequest.


        :param payment_request: The payment_request of this PaymentAuthorisationRequest.  # noqa: E501
        :type: PaymentRequest
        """
        if self.local_vars_configuration.client_side_validation and payment_request is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_request`, must not be `None`")  # noqa: E501

        self._payment_request = payment_request

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
        if not isinstance(other, PaymentAuthorisationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentAuthorisationRequest):
            return True

        return self.to_dict() != other.to_dict()
