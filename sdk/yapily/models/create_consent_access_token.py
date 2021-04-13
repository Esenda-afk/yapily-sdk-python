# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.330
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class CreateConsentAccessToken(object):
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
        'access_token': 'str',
        'refresh_token': 'str',
        'institution_id': 'str',
        'scope': 'str'
    }

    attribute_map = {
        'access_token': 'accessToken',
        'refresh_token': 'refreshToken',
        'institution_id': 'institutionId',
        'scope': 'scope'
    }

    def __init__(self, access_token=None, refresh_token=None, institution_id=None, scope=None, local_vars_configuration=None):  # noqa: E501
        """CreateConsentAccessToken - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_token = None
        self._refresh_token = None
        self._institution_id = None
        self._scope = None
        self.discriminator = None

        self.access_token = access_token
        self.refresh_token = refresh_token
        self.institution_id = institution_id
        self.scope = scope

    @property
    def access_token(self):
        """Gets the access_token of this CreateConsentAccessToken.  # noqa: E501


        :return: The access_token of this CreateConsentAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this CreateConsentAccessToken.


        :param access_token: The access_token of this CreateConsentAccessToken.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and access_token is None:  # noqa: E501
            raise ValueError("Invalid value for `access_token`, must not be `None`")  # noqa: E501

        self._access_token = access_token

    @property
    def refresh_token(self):
        """Gets the refresh_token of this CreateConsentAccessToken.  # noqa: E501


        :return: The refresh_token of this CreateConsentAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this CreateConsentAccessToken.


        :param refresh_token: The refresh_token of this CreateConsentAccessToken.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and refresh_token is None:  # noqa: E501
            raise ValueError("Invalid value for `refresh_token`, must not be `None`")  # noqa: E501

        self._refresh_token = refresh_token

    @property
    def institution_id(self):
        """Gets the institution_id of this CreateConsentAccessToken.  # noqa: E501


        :return: The institution_id of this CreateConsentAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._institution_id

    @institution_id.setter
    def institution_id(self, institution_id):
        """Sets the institution_id of this CreateConsentAccessToken.


        :param institution_id: The institution_id of this CreateConsentAccessToken.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and institution_id is None:  # noqa: E501
            raise ValueError("Invalid value for `institution_id`, must not be `None`")  # noqa: E501

        self._institution_id = institution_id

    @property
    def scope(self):
        """Gets the scope of this CreateConsentAccessToken.  # noqa: E501


        :return: The scope of this CreateConsentAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this CreateConsentAccessToken.


        :param scope: The scope of this CreateConsentAccessToken.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and scope is None:  # noqa: E501
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501

        self._scope = scope

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
        if not isinstance(other, CreateConsentAccessToken):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateConsentAccessToken):
            return True

        return self.to_dict() != other.to_dict()
