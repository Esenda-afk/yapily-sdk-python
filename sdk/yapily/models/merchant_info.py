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


class MerchantInfo(object):
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
        'category_code': 'str',
        'customer_id': 'str',
        'address': 'Address'
    }

    attribute_map = {
        'category_code': 'categoryCode',
        'customer_id': 'customerId',
        'address': 'address'
    }

    def __init__(self, category_code=None, customer_id=None, address=None, local_vars_configuration=None):  # noqa: E501
        """MerchantInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._category_code = None
        self._customer_id = None
        self._address = None
        self.discriminator = None

        self.category_code = category_code
        self.customer_id = customer_id
        self.address = address

    @property
    def category_code(self):
        """Gets the category_code of this MerchantInfo.  # noqa: E501


        :return: The category_code of this MerchantInfo.  # noqa: E501
        :rtype: str
        """
        return self._category_code

    @category_code.setter
    def category_code(self, category_code):
        """Sets the category_code of this MerchantInfo.


        :param category_code: The category_code of this MerchantInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and category_code is None:  # noqa: E501
            raise ValueError("Invalid value for `category_code`, must not be `None`")  # noqa: E501

        self._category_code = category_code

    @property
    def customer_id(self):
        """Gets the customer_id of this MerchantInfo.  # noqa: E501


        :return: The customer_id of this MerchantInfo.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this MerchantInfo.


        :param customer_id: The customer_id of this MerchantInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and customer_id is None:  # noqa: E501
            raise ValueError("Invalid value for `customer_id`, must not be `None`")  # noqa: E501

        self._customer_id = customer_id

    @property
    def address(self):
        """Gets the address of this MerchantInfo.  # noqa: E501


        :return: The address of this MerchantInfo.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this MerchantInfo.


        :param address: The address of this MerchantInfo.  # noqa: E501
        :type: Address
        """
        if self.local_vars_configuration.client_side_validation and address is None:  # noqa: E501
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

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
        if not isinstance(other, MerchantInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MerchantInfo):
            return True

        return self.to_dict() != other.to_dict()
