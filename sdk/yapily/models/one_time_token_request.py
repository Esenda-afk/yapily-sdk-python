# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.269
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class OneTimeTokenRequest(object):
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
        'one_time_token': 'str'
    }

    attribute_map = {
        'one_time_token': 'oneTimeToken'
    }

    def __init__(self, one_time_token=None, local_vars_configuration=None):  # noqa: E501
        """OneTimeTokenRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._one_time_token = None
        self.discriminator = None

        self.one_time_token = one_time_token

    @property
    def one_time_token(self):
        """Gets the one_time_token of this OneTimeTokenRequest.  # noqa: E501


        :return: The one_time_token of this OneTimeTokenRequest.  # noqa: E501
        :rtype: str
        """
        return self._one_time_token

    @one_time_token.setter
    def one_time_token(self, one_time_token):
        """Sets the one_time_token of this OneTimeTokenRequest.


        :param one_time_token: The one_time_token of this OneTimeTokenRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and one_time_token is None:  # noqa: E501
            raise ValueError("Invalid value for `one_time_token`, must not be `None`")  # noqa: E501

        self._one_time_token = one_time_token

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
        if not isinstance(other, OneTimeTokenRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneTimeTokenRequest):
            return True

        return self.to_dict() != other.to_dict()
