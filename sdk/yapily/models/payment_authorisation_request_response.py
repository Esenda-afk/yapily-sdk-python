# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.283
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class PaymentAuthorisationRequestResponse(object):
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
        'id': 'str',
        'user_uuid': 'str',
        'application_user_id': 'str',
        'reference_id': 'str',
        'institution_id': 'str',
        'status': 'str',
        'created_at': 'datetime',
        'transaction_from': 'datetime',
        'transaction_to': 'datetime',
        'expires_at': 'datetime',
        'time_to_expire_in_millis': 'int',
        'time_to_expire': 'str',
        'feature_scope': 'list[str]',
        'charges': 'list[ChargeDetails]',
        'exchange_rate_information': 'ExchangeRateInformationResponse',
        'consent_token': 'str',
        'authorisation_url': 'str',
        'state': 'str',
        'qr_code_url': 'str',
        'authorized_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'user_uuid': 'userUuid',
        'application_user_id': 'applicationUserId',
        'reference_id': 'referenceId',
        'institution_id': 'institutionId',
        'status': 'status',
        'created_at': 'createdAt',
        'transaction_from': 'transactionFrom',
        'transaction_to': 'transactionTo',
        'expires_at': 'expiresAt',
        'time_to_expire_in_millis': 'timeToExpireInMillis',
        'time_to_expire': 'timeToExpire',
        'feature_scope': 'featureScope',
        'charges': 'charges',
        'exchange_rate_information': 'exchangeRateInformation',
        'consent_token': 'consentToken',
        'authorisation_url': 'authorisationUrl',
        'state': 'state',
        'qr_code_url': 'qrCodeUrl',
        'authorized_at': 'authorizedAt'
    }

    def __init__(self, id=None, user_uuid=None, application_user_id=None, reference_id=None, institution_id=None, status=None, created_at=None, transaction_from=None, transaction_to=None, expires_at=None, time_to_expire_in_millis=None, time_to_expire=None, feature_scope=None, charges=None, exchange_rate_information=None, consent_token=None, authorisation_url=None, state=None, qr_code_url=None, authorized_at=None, local_vars_configuration=None):  # noqa: E501
        """PaymentAuthorisationRequestResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._user_uuid = None
        self._application_user_id = None
        self._reference_id = None
        self._institution_id = None
        self._status = None
        self._created_at = None
        self._transaction_from = None
        self._transaction_to = None
        self._expires_at = None
        self._time_to_expire_in_millis = None
        self._time_to_expire = None
        self._feature_scope = None
        self._charges = None
        self._exchange_rate_information = None
        self._consent_token = None
        self._authorisation_url = None
        self._state = None
        self._qr_code_url = None
        self._authorized_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user_uuid is not None:
            self.user_uuid = user_uuid
        if application_user_id is not None:
            self.application_user_id = application_user_id
        if reference_id is not None:
            self.reference_id = reference_id
        if institution_id is not None:
            self.institution_id = institution_id
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if transaction_from is not None:
            self.transaction_from = transaction_from
        if transaction_to is not None:
            self.transaction_to = transaction_to
        if expires_at is not None:
            self.expires_at = expires_at
        if time_to_expire_in_millis is not None:
            self.time_to_expire_in_millis = time_to_expire_in_millis
        if time_to_expire is not None:
            self.time_to_expire = time_to_expire
        if feature_scope is not None:
            self.feature_scope = feature_scope
        if charges is not None:
            self.charges = charges
        if exchange_rate_information is not None:
            self.exchange_rate_information = exchange_rate_information
        if consent_token is not None:
            self.consent_token = consent_token
        if authorisation_url is not None:
            self.authorisation_url = authorisation_url
        if state is not None:
            self.state = state
        if qr_code_url is not None:
            self.qr_code_url = qr_code_url
        if authorized_at is not None:
            self.authorized_at = authorized_at

    @property
    def id(self):
        """Gets the id of this PaymentAuthorisationRequestResponse.  # noqa: E501


        :return: The id of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentAuthorisationRequestResponse.


        :param id: The id of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def user_uuid(self):
        """Gets the user_uuid of this PaymentAuthorisationRequestResponse.  # noqa: E501


        :return: The user_uuid of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this PaymentAuthorisationRequestResponse.


        :param user_uuid: The user_uuid of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :type: str
        """

        self._user_uuid = user_uuid

    @property
    def application_user_id(self):
        """Gets the application_user_id of this PaymentAuthorisationRequestResponse.  # noqa: E501


        :return: The application_user_id of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._application_user_id

    @application_user_id.setter
    def application_user_id(self, application_user_id):
        """Sets the application_user_id of this PaymentAuthorisationRequestResponse.


        :param application_user_id: The application_user_id of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :type: str
        """

        self._application_user_id = application_user_id

    @property
    def reference_id(self):
        """Gets the reference_id of this PaymentAuthorisationRequestResponse.  # noqa: E501


        :return: The reference_id of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """Sets the reference_id of this PaymentAuthorisationRequestResponse.


        :param reference_id: The reference_id of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :type: str
        """

        self._reference_id = reference_id

    @property
    def institution_id(self):
        """Gets the institution_id of this PaymentAuthorisationRequestResponse.  # noqa: E501


        :return: The institution_id of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._institution_id

    @institution_id.setter
    def institution_id(self, institution_id):
        """Sets the institution_id of this PaymentAuthorisationRequestResponse.


        :param institution_id: The institution_id of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :type: str
        """

        self._institution_id = institution_id

    @property
    def status(self):
        """Gets the status of this PaymentAuthorisationRequestResponse.  # noqa: E501


        :return: The status of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PaymentAuthorisationRequestResponse.


        :param status: The status of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["AWAITING_AUTHORIZATION", "AWAITING_FURTHER_AUTHORIZATION", "AWAITING_RE_AUTHORIZATION", "AUTHORIZED", "CONSUMED", "REJECTED", "REVOKED", "FAILED", "EXPIRED", "UNKNOWN", "INVALID", "AWAITING_PRE_AUTHORIZATION", "PRE_AUTHORIZED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this PaymentAuthorisationRequestResponse.  # noqa: E501


        :return: The created_at of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PaymentAuthorisationRequestResponse.


        :param created_at: The created_at of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def transaction_from(self):
        """Gets the transaction_from of this PaymentAuthorisationRequestResponse.  # noqa: E501


        :return: The transaction_from of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._transaction_from

    @transaction_from.setter
    def transaction_from(self, transaction_from):
        """Sets the transaction_from of this PaymentAuthorisationRequestResponse.


        :param transaction_from: The transaction_from of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :type: datetime
        """

        self._transaction_from = transaction_from

    @property
    def transaction_to(self):
        """Gets the transaction_to of this PaymentAuthorisationRequestResponse.  # noqa: E501


        :return: The transaction_to of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._transaction_to

    @transaction_to.setter
    def transaction_to(self, transaction_to):
        """Sets the transaction_to of this PaymentAuthorisationRequestResponse.


        :param transaction_to: The transaction_to of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :type: datetime
        """

        self._transaction_to = transaction_to

    @property
    def expires_at(self):
        """Gets the expires_at of this PaymentAuthorisationRequestResponse.  # noqa: E501


        :return: The expires_at of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this PaymentAuthorisationRequestResponse.


        :param expires_at: The expires_at of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

    @property
    def time_to_expire_in_millis(self):
        """Gets the time_to_expire_in_millis of this PaymentAuthorisationRequestResponse.  # noqa: E501

        Deprecated. Use `timeToExpire` instead.  # noqa: E501

        :return: The time_to_expire_in_millis of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :rtype: int
        """
        return self._time_to_expire_in_millis

    @time_to_expire_in_millis.setter
    def time_to_expire_in_millis(self, time_to_expire_in_millis):
        """Sets the time_to_expire_in_millis of this PaymentAuthorisationRequestResponse.

        Deprecated. Use `timeToExpire` instead.  # noqa: E501

        :param time_to_expire_in_millis: The time_to_expire_in_millis of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :type: int
        """

        self._time_to_expire_in_millis = time_to_expire_in_millis

    @property
    def time_to_expire(self):
        """Gets the time_to_expire of this PaymentAuthorisationRequestResponse.  # noqa: E501

        ISO 8601 duration  # noqa: E501

        :return: The time_to_expire of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._time_to_expire

    @time_to_expire.setter
    def time_to_expire(self, time_to_expire):
        """Sets the time_to_expire of this PaymentAuthorisationRequestResponse.

        ISO 8601 duration  # noqa: E501

        :param time_to_expire: The time_to_expire of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :type: str
        """

        self._time_to_expire = time_to_expire

    @property
    def feature_scope(self):
        """Gets the feature_scope of this PaymentAuthorisationRequestResponse.  # noqa: E501


        :return: The feature_scope of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._feature_scope

    @feature_scope.setter
    def feature_scope(self, feature_scope):
        """Sets the feature_scope of this PaymentAuthorisationRequestResponse.


        :param feature_scope: The feature_scope of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["INITIATE_PRE_AUTHORISATION", "INITIATE_ACCOUNT_REQUEST", "ACCOUNT_REQUEST_DETAILS", "ACCOUNTS", "ACCOUNT", "ACCOUNT_TRANSACTIONS", "ACCOUNT_STATEMENTS", "ACCOUNT_STATEMENT", "ACCOUNT_STATEMENT_FILE", "ACCOUNT_SCHEDULED_PAYMENTS", "ACCOUNT_DIRECT_DEBITS", "ACCOUNT_PERIODIC_PAYMENTS", "ACCOUNT_TRANSACTIONS_WITH_MERCHANT", "IDENTITY", "ACCOUNTS_WITHOUT_BALANCE", "ACCOUNT_WITHOUT_BALANCE", "ACCOUNT_BALANCES", "INITIATE_SINGLE_PAYMENT_SORTCODE", "EXISTING_PAYMENT_INITIATION_DETAILS", "CREATE_SINGLE_PAYMENT_SORTCODE", "EXISTING_PAYMENTS_DETAILS", "INITIATE_DOMESTIC_SINGLE_PAYMENT", "CREATE_DOMESTIC_SINGLE_PAYMENT", "INITIATE_DOMESTIC_SINGLE_INSTANT_PAYMENT", "CREATE_DOMESTIC_SINGLE_INSTANT_PAYMENT", "INITIATE_DOMESTIC_VARIABLE_RECURRING_PAYMENT", "CREATE_DOMESTIC_VARIABLE_RECURRING_PAYMENT", "INITIATE_DOMESTIC_SCHEDULED_PAYMENT", "CREATE_DOMESTIC_SCHEDULED_PAYMENT", "INITIATE_DOMESTIC_PERIODIC_PAYMENT", "CREATE_DOMESTIC_PERIODIC_PAYMENT", "PERIODIC_PAYMENT_FREQUENCY_EXTENDED", "INITIATE_INTERNATIONAL_VARIABLE_RECURRING_PAYMENT", "CREATE_INTERNATIONAL_VARIABLE_RECURRING_PAYMENT", "INITIATE_INTERNATIONAL_SCHEDULED_PAYMENT", "CREATE_INTERNATIONAL_SCHEDULED_PAYMENT", "INITIATE_INTERNATIONAL_PERIODIC_PAYMENT", "CREATE_INTERNATIONAL_PERIODIC_PAYMENT", "INITIATE_INTERNATIONAL_SINGLE_PAYMENT", "CREATE_INTERNATIONAL_SINGLE_PAYMENT", "INITIATE_BULK_PAYMENT", "CREATE_BULK_PAYMENT", "TRANSFER", "OPEN_DATA_PERSONAL_CURRENT_ACCOUNTS", "OPEN_DATA_ATMS", "READ_DOMESTIC_SINGLE_REFUND", "READ_DOMESTIC_SCHEDULED_REFUND", "READ_DOMESTIC_PERIODIC_PAYMENT_REFUND", "READ_INTERNATIONAL_SINGLE_REFUND", "READ_INTERNATIONAL_SCHEDULED_REFUND"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(feature_scope).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `feature_scope` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(feature_scope) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._feature_scope = feature_scope

    @property
    def charges(self):
        """Gets the charges of this PaymentAuthorisationRequestResponse.  # noqa: E501


        :return: The charges of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :rtype: list[ChargeDetails]
        """
        return self._charges

    @charges.setter
    def charges(self, charges):
        """Sets the charges of this PaymentAuthorisationRequestResponse.


        :param charges: The charges of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :type: list[ChargeDetails]
        """

        self._charges = charges

    @property
    def exchange_rate_information(self):
        """Gets the exchange_rate_information of this PaymentAuthorisationRequestResponse.  # noqa: E501


        :return: The exchange_rate_information of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :rtype: ExchangeRateInformationResponse
        """
        return self._exchange_rate_information

    @exchange_rate_information.setter
    def exchange_rate_information(self, exchange_rate_information):
        """Sets the exchange_rate_information of this PaymentAuthorisationRequestResponse.


        :param exchange_rate_information: The exchange_rate_information of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :type: ExchangeRateInformationResponse
        """

        self._exchange_rate_information = exchange_rate_information

    @property
    def consent_token(self):
        """Gets the consent_token of this PaymentAuthorisationRequestResponse.  # noqa: E501


        :return: The consent_token of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._consent_token

    @consent_token.setter
    def consent_token(self, consent_token):
        """Sets the consent_token of this PaymentAuthorisationRequestResponse.


        :param consent_token: The consent_token of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :type: str
        """

        self._consent_token = consent_token

    @property
    def authorisation_url(self):
        """Gets the authorisation_url of this PaymentAuthorisationRequestResponse.  # noqa: E501


        :return: The authorisation_url of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._authorisation_url

    @authorisation_url.setter
    def authorisation_url(self, authorisation_url):
        """Sets the authorisation_url of this PaymentAuthorisationRequestResponse.


        :param authorisation_url: The authorisation_url of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :type: str
        """

        self._authorisation_url = authorisation_url

    @property
    def state(self):
        """Gets the state of this PaymentAuthorisationRequestResponse.  # noqa: E501


        :return: The state of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PaymentAuthorisationRequestResponse.


        :param state: The state of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def qr_code_url(self):
        """Gets the qr_code_url of this PaymentAuthorisationRequestResponse.  # noqa: E501


        :return: The qr_code_url of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, qr_code_url):
        """Sets the qr_code_url of this PaymentAuthorisationRequestResponse.


        :param qr_code_url: The qr_code_url of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :type: str
        """

        self._qr_code_url = qr_code_url

    @property
    def authorized_at(self):
        """Gets the authorized_at of this PaymentAuthorisationRequestResponse.  # noqa: E501


        :return: The authorized_at of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._authorized_at

    @authorized_at.setter
    def authorized_at(self, authorized_at):
        """Sets the authorized_at of this PaymentAuthorisationRequestResponse.


        :param authorized_at: The authorized_at of this PaymentAuthorisationRequestResponse.  # noqa: E501
        :type: datetime
        """

        self._authorized_at = authorized_at

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
        if not isinstance(other, PaymentAuthorisationRequestResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentAuthorisationRequestResponse):
            return True

        return self.to_dict() != other.to_dict()
