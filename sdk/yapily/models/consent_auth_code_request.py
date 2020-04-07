# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.178
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ConsentAuthCodeRequest(object):
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
        'auth_code': 'str',
        'auth_state': 'str'
    }

    attribute_map = {
        'auth_code': 'authCode',
        'auth_state': 'authState'
    }

    def __init__(self, auth_code=None, auth_state=None):  # noqa: E501
        """ConsentAuthCodeRequest - a model defined in Swagger"""  # noqa: E501

        self._auth_code = None
        self._auth_state = None
        self.discriminator = None

        self.auth_code = auth_code
        self.auth_state = auth_state

    @property
    def auth_code(self):
        """Gets the auth_code of this ConsentAuthCodeRequest.  # noqa: E501


        :return: The auth_code of this ConsentAuthCodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._auth_code

    @auth_code.setter
    def auth_code(self, auth_code):
        """Sets the auth_code of this ConsentAuthCodeRequest.


        :param auth_code: The auth_code of this ConsentAuthCodeRequest.  # noqa: E501
        :type: str
        """
        if auth_code is None:
            raise ValueError("Invalid value for `auth_code`, must not be `None`")  # noqa: E501

        self._auth_code = auth_code

    @property
    def auth_state(self):
        """Gets the auth_state of this ConsentAuthCodeRequest.  # noqa: E501


        :return: The auth_state of this ConsentAuthCodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._auth_state

    @auth_state.setter
    def auth_state(self, auth_state):
        """Sets the auth_state of this ConsentAuthCodeRequest.


        :param auth_state: The auth_state of this ConsentAuthCodeRequest.  # noqa: E501
        :type: str
        """
        if auth_state is None:
            raise ValueError("Invalid value for `auth_state`, must not be `None`")  # noqa: E501

        self._auth_state = auth_state

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
        if not isinstance(other, ConsentAuthCodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
