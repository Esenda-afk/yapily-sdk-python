# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.227
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class Merchant(object):
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
        'merchant_name': 'str',
        'merchant_category_code': 'str'
    }

    attribute_map = {
        'merchant_name': 'merchantName',
        'merchant_category_code': 'merchantCategoryCode'
    }

    def __init__(self, merchant_name=None, merchant_category_code=None, local_vars_configuration=None):  # noqa: E501
        """Merchant - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._merchant_name = None
        self._merchant_category_code = None
        self.discriminator = None

        if merchant_name is not None:
            self.merchant_name = merchant_name
        if merchant_category_code is not None:
            self.merchant_category_code = merchant_category_code

    @property
    def merchant_name(self):
        """Gets the merchant_name of this Merchant.  # noqa: E501


        :return: The merchant_name of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, merchant_name):
        """Sets the merchant_name of this Merchant.


        :param merchant_name: The merchant_name of this Merchant.  # noqa: E501
        :type: str
        """

        self._merchant_name = merchant_name

    @property
    def merchant_category_code(self):
        """Gets the merchant_category_code of this Merchant.  # noqa: E501


        :return: The merchant_category_code of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._merchant_category_code

    @merchant_category_code.setter
    def merchant_category_code(self, merchant_category_code):
        """Sets the merchant_category_code of this Merchant.


        :param merchant_category_code: The merchant_category_code of this Merchant.  # noqa: E501
        :type: str
        """

        self._merchant_category_code = merchant_category_code

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
        if not isinstance(other, Merchant):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Merchant):
            return True

        return self.to_dict() != other.to_dict()
