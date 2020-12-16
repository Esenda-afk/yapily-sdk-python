# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.292
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class InstitutionError(object):
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
        'error_message': 'str',
        'http_status_code': 'int'
    }

    attribute_map = {
        'error_message': 'errorMessage',
        'http_status_code': 'httpStatusCode'
    }

    def __init__(self, error_message=None, http_status_code=None, local_vars_configuration=None):  # noqa: E501
        """InstitutionError - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._error_message = None
        self._http_status_code = None
        self.discriminator = None

        if error_message is not None:
            self.error_message = error_message
        if http_status_code is not None:
            self.http_status_code = http_status_code

    @property
    def error_message(self):
        """Gets the error_message of this InstitutionError.  # noqa: E501


        :return: The error_message of this InstitutionError.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this InstitutionError.


        :param error_message: The error_message of this InstitutionError.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def http_status_code(self):
        """Gets the http_status_code of this InstitutionError.  # noqa: E501


        :return: The http_status_code of this InstitutionError.  # noqa: E501
        :rtype: int
        """
        return self._http_status_code

    @http_status_code.setter
    def http_status_code(self, http_status_code):
        """Sets the http_status_code of this InstitutionError.


        :param http_status_code: The http_status_code of this InstitutionError.  # noqa: E501
        :type: int
        """

        self._http_status_code = http_status_code

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
        if not isinstance(other, InstitutionError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstitutionError):
            return True

        return self.to_dict() != other.to_dict()
