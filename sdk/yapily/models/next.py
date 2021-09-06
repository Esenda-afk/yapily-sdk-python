# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 1.64.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class Next(object):
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
        'before': 'datetime',
        'cursor': 'str',
        '_from': 'datetime',
        'limit': 'int'
    }

    attribute_map = {
        'before': 'before',
        'cursor': 'cursor',
        '_from': 'from',
        'limit': 'limit'
    }

    def __init__(self, before=None, cursor=None, _from=None, limit=None, local_vars_configuration=None):  # noqa: E501
        """Next - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._before = None
        self._cursor = None
        self.__from = None
        self._limit = None
        self.discriminator = None

        if before is not None:
            self.before = before
        if cursor is not None:
            self.cursor = cursor
        if _from is not None:
            self._from = _from
        if limit is not None:
            self.limit = limit

    @property
    def before(self):
        """Gets the before of this Next.  # noqa: E501


        :return: The before of this Next.  # noqa: E501
        :rtype: datetime
        """
        return self._before

    @before.setter
    def before(self, before):
        """Sets the before of this Next.


        :param before: The before of this Next.  # noqa: E501
        :type: datetime
        """

        self._before = before

    @property
    def cursor(self):
        """Gets the cursor of this Next.  # noqa: E501


        :return: The cursor of this Next.  # noqa: E501
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """Sets the cursor of this Next.


        :param cursor: The cursor of this Next.  # noqa: E501
        :type: str
        """

        self._cursor = cursor

    @property
    def _from(self):
        """Gets the _from of this Next.  # noqa: E501


        :return: The _from of this Next.  # noqa: E501
        :rtype: datetime
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this Next.


        :param _from: The _from of this Next.  # noqa: E501
        :type: datetime
        """

        self.__from = _from

    @property
    def limit(self):
        """Gets the limit of this Next.  # noqa: E501


        :return: The limit of this Next.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this Next.


        :param limit: The limit of this Next.  # noqa: E501
        :type: int
        """

        self._limit = limit

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
        if not isinstance(other, Next):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Next):
            return True

        return self.to_dict() != other.to_dict()
