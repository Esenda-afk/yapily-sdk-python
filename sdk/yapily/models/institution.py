# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.398
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class Institution(object):
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
        'name': 'str',
        'full_name': 'str',
        'countries': 'list[Country]',
        'environment_type': 'str',
        'credentials_type': 'str',
        'media': 'list[Media]',
        'features': 'list[str]',
        'monitoring': 'dict(str, MonitoringFeatureStatus)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'full_name': 'fullName',
        'countries': 'countries',
        'environment_type': 'environmentType',
        'credentials_type': 'credentialsType',
        'media': 'media',
        'features': 'features',
        'monitoring': 'monitoring'
    }

    def __init__(self, id=None, name=None, full_name=None, countries=None, environment_type=None, credentials_type=None, media=None, features=None, monitoring=None, local_vars_configuration=None):  # noqa: E501
        """Institution - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._full_name = None
        self._countries = None
        self._environment_type = None
        self._credentials_type = None
        self._media = None
        self._features = None
        self._monitoring = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if full_name is not None:
            self.full_name = full_name
        if countries is not None:
            self.countries = countries
        if environment_type is not None:
            self.environment_type = environment_type
        if credentials_type is not None:
            self.credentials_type = credentials_type
        if media is not None:
            self.media = media
        if features is not None:
            self.features = features
        if monitoring is not None:
            self.monitoring = monitoring

    @property
    def id(self):
        """Gets the id of this Institution.  # noqa: E501


        :return: The id of this Institution.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Institution.


        :param id: The id of this Institution.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Institution.  # noqa: E501


        :return: The name of this Institution.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Institution.


        :param name: The name of this Institution.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def full_name(self):
        """Gets the full_name of this Institution.  # noqa: E501


        :return: The full_name of this Institution.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this Institution.


        :param full_name: The full_name of this Institution.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def countries(self):
        """Gets the countries of this Institution.  # noqa: E501


        :return: The countries of this Institution.  # noqa: E501
        :rtype: list[Country]
        """
        return self._countries

    @countries.setter
    def countries(self, countries):
        """Sets the countries of this Institution.


        :param countries: The countries of this Institution.  # noqa: E501
        :type: list[Country]
        """

        self._countries = countries

    @property
    def environment_type(self):
        """Gets the environment_type of this Institution.  # noqa: E501


        :return: The environment_type of this Institution.  # noqa: E501
        :rtype: str
        """
        return self._environment_type

    @environment_type.setter
    def environment_type(self, environment_type):
        """Sets the environment_type of this Institution.


        :param environment_type: The environment_type of this Institution.  # noqa: E501
        :type: str
        """
        allowed_values = ["SANDBOX", "MOCK", "LIVE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and environment_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `environment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(environment_type, allowed_values)
            )

        self._environment_type = environment_type

    @property
    def credentials_type(self):
        """Gets the credentials_type of this Institution.  # noqa: E501


        :return: The credentials_type of this Institution.  # noqa: E501
        :rtype: str
        """
        return self._credentials_type

    @credentials_type.setter
    def credentials_type(self, credentials_type):
        """Sets the credentials_type of this Institution.


        :param credentials_type: The credentials_type of this Institution.  # noqa: E501
        :type: str
        """
        allowed_values = ["OAUTH1", "OAUTH2", "OAUTH2_NOSECRET", "OAUTH2_SIGNATURE", "OPEN_BANKING", "OPEN_BANKING_UK_MANUAL", "OPEN_BANKING_UK_AUTO", "OPEN_BANKING_IBM", "OPEN_BANKING_AUTO", "OPEN_BANKING_AUTO_EMAIL", "OPEN_BANKING_MANUAL", "OPEN_BANKING_WITH_TPP_ID_AND_SECRET", "API_KEY", "OPEN_BANKING_NO_KEY", "OPEN_BANKING_NO_TRANSPORT", "TOKEN_IO"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and credentials_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `credentials_type` ({0}), must be one of {1}"  # noqa: E501
                .format(credentials_type, allowed_values)
            )

        self._credentials_type = credentials_type

    @property
    def media(self):
        """Gets the media of this Institution.  # noqa: E501


        :return: The media of this Institution.  # noqa: E501
        :rtype: list[Media]
        """
        return self._media

    @media.setter
    def media(self, media):
        """Sets the media of this Institution.


        :param media: The media of this Institution.  # noqa: E501
        :type: list[Media]
        """

        self._media = media

    @property
    def features(self):
        """Gets the features of this Institution.  # noqa: E501


        :return: The features of this Institution.  # noqa: E501
        :rtype: list[str]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this Institution.


        :param features: The features of this Institution.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["INITIATE_PRE_AUTHORISATION", "INITIATE_PRE_AUTHORISATION_ACCOUNTS", "INITIATE_PRE_AUTHORISATION_PAYMENTS", "INITIATE_ACCOUNT_REQUEST", "INITIATE_EMBEDDED_ACCOUNT_REQUEST", "ACCOUNT_REQUEST_DETAILS", "ACCOUNTS", "ACCOUNT", "ACCOUNT_TRANSACTIONS", "ACCOUNT_STATEMENTS", "ACCOUNT_STATEMENT", "ACCOUNT_STATEMENT_FILE", "ACCOUNT_SCHEDULED_PAYMENTS", "ACCOUNT_DIRECT_DEBITS", "ACCOUNT_PERIODIC_PAYMENTS", "ACCOUNT_TRANSACTIONS_WITH_MERCHANT", "IDENTITY", "ACCOUNTS_WITHOUT_BALANCE", "ACCOUNT_WITHOUT_BALANCE", "ACCOUNT_BALANCES", "ACCOUNT_BENEFICIARIES", "INITIATE_SINGLE_PAYMENT_SORTCODE", "EXISTING_PAYMENT_INITIATION_DETAILS", "CREATE_SINGLE_PAYMENT_SORTCODE", "EXISTING_PAYMENTS_DETAILS", "INITIATE_DOMESTIC_SINGLE_PAYMENT", "INITIATE_EMBEDDED_DOMESTIC_SINGLE_PAYMENT", "CREATE_DOMESTIC_SINGLE_PAYMENT", "INITIATE_DOMESTIC_SINGLE_INSTANT_PAYMENT", "CREATE_DOMESTIC_SINGLE_INSTANT_PAYMENT", "INITIATE_DOMESTIC_VARIABLE_RECURRING_PAYMENT", "CREATE_DOMESTIC_VARIABLE_RECURRING_PAYMENT", "INITIATE_DOMESTIC_SCHEDULED_PAYMENT", "CREATE_DOMESTIC_SCHEDULED_PAYMENT", "INITIATE_DOMESTIC_PERIODIC_PAYMENT", "CREATE_DOMESTIC_PERIODIC_PAYMENT", "PERIODIC_PAYMENT_FREQUENCY_EXTENDED", "INITIATE_INTERNATIONAL_VARIABLE_RECURRING_PAYMENT", "CREATE_INTERNATIONAL_VARIABLE_RECURRING_PAYMENT", "INITIATE_INTERNATIONAL_SCHEDULED_PAYMENT", "CREATE_INTERNATIONAL_SCHEDULED_PAYMENT", "INITIATE_INTERNATIONAL_PERIODIC_PAYMENT", "CREATE_INTERNATIONAL_PERIODIC_PAYMENT", "INITIATE_INTERNATIONAL_SINGLE_PAYMENT", "CREATE_INTERNATIONAL_SINGLE_PAYMENT", "INITIATE_BULK_PAYMENT", "CREATE_BULK_PAYMENT", "TRANSFER", "OPEN_DATA_PERSONAL_CURRENT_ACCOUNTS", "OPEN_DATA_ATMS", "READ_DOMESTIC_SINGLE_REFUND", "READ_DOMESTIC_SCHEDULED_REFUND", "READ_DOMESTIC_PERIODIC_PAYMENT_REFUND", "READ_INTERNATIONAL_SINGLE_REFUND", "READ_INTERNATIONAL_SCHEDULED_REFUND"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(features).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `features` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(features) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._features = features

    @property
    def monitoring(self):
        """Gets the monitoring of this Institution.  # noqa: E501


        :return: The monitoring of this Institution.  # noqa: E501
        :rtype: dict(str, MonitoringFeatureStatus)
        """
        return self._monitoring

    @monitoring.setter
    def monitoring(self, monitoring):
        """Sets the monitoring of this Institution.


        :param monitoring: The monitoring of this Institution.  # noqa: E501
        :type: dict(str, MonitoringFeatureStatus)
        """

        self._monitoring = monitoring

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
        if not isinstance(other, Institution):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Institution):
            return True

        return self.to_dict() != other.to_dict()
