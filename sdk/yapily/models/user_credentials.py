# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.310
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class UserCredentials(object):
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
        'corporate_id': 'str',
        'password': 'str'
    }

    attribute_map = {
        'id': 'id',
        'corporate_id': 'corporateId',
        'password': 'password'
    }

    def __init__(self, id=None, corporate_id=None, password=None, local_vars_configuration=None):  # noqa: E501
        """UserCredentials - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._corporate_id = None
        self._password = None
        self.discriminator = None

        self.id = id
        if corporate_id is not None:
            self.corporate_id = corporate_id
        self.password = password

    @property
    def id(self):
        """Gets the id of this UserCredentials.  # noqa: E501


        :return: The id of this UserCredentials.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserCredentials.


        :param id: The id of this UserCredentials.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def corporate_id(self):
        """Gets the corporate_id of this UserCredentials.  # noqa: E501


        :return: The corporate_id of this UserCredentials.  # noqa: E501
        :rtype: str
        """
        return self._corporate_id

    @corporate_id.setter
    def corporate_id(self, corporate_id):
        """Sets the corporate_id of this UserCredentials.


        :param corporate_id: The corporate_id of this UserCredentials.  # noqa: E501
        :type: str
        """

        self._corporate_id = corporate_id

    @property
    def password(self):
        """Gets the password of this UserCredentials.  # noqa: E501


        :return: The password of this UserCredentials.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserCredentials.


        :param password: The password of this UserCredentials.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

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
        if not isinstance(other, UserCredentials):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserCredentials):
            return True

        return self.to_dict() != other.to_dict()
