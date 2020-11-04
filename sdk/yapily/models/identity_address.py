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


class IdentityAddress(object):
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
        'address_lines': 'list[str]',
        'city': 'str',
        'postal_code': 'str',
        'country': 'str',
        'street_name': 'str',
        'building_number': 'str',
        'type': 'str',
        'county': 'str'
    }

    attribute_map = {
        'address_lines': 'addressLines',
        'city': 'city',
        'postal_code': 'postalCode',
        'country': 'country',
        'street_name': 'streetName',
        'building_number': 'buildingNumber',
        'type': 'type',
        'county': 'county'
    }

    def __init__(self, address_lines=None, city=None, postal_code=None, country=None, street_name=None, building_number=None, type=None, county=None, local_vars_configuration=None):  # noqa: E501
        """IdentityAddress - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address_lines = None
        self._city = None
        self._postal_code = None
        self._country = None
        self._street_name = None
        self._building_number = None
        self._type = None
        self._county = None
        self.discriminator = None

        if address_lines is not None:
            self.address_lines = address_lines
        if city is not None:
            self.city = city
        if postal_code is not None:
            self.postal_code = postal_code
        if country is not None:
            self.country = country
        if street_name is not None:
            self.street_name = street_name
        if building_number is not None:
            self.building_number = building_number
        if type is not None:
            self.type = type
        if county is not None:
            self.county = county

    @property
    def address_lines(self):
        """Gets the address_lines of this IdentityAddress.  # noqa: E501


        :return: The address_lines of this IdentityAddress.  # noqa: E501
        :rtype: list[str]
        """
        return self._address_lines

    @address_lines.setter
    def address_lines(self, address_lines):
        """Sets the address_lines of this IdentityAddress.


        :param address_lines: The address_lines of this IdentityAddress.  # noqa: E501
        :type: list[str]
        """

        self._address_lines = address_lines

    @property
    def city(self):
        """Gets the city of this IdentityAddress.  # noqa: E501


        :return: The city of this IdentityAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this IdentityAddress.


        :param city: The city of this IdentityAddress.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def postal_code(self):
        """Gets the postal_code of this IdentityAddress.  # noqa: E501


        :return: The postal_code of this IdentityAddress.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this IdentityAddress.


        :param postal_code: The postal_code of this IdentityAddress.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def country(self):
        """Gets the country of this IdentityAddress.  # noqa: E501


        :return: The country of this IdentityAddress.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this IdentityAddress.


        :param country: The country of this IdentityAddress.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def street_name(self):
        """Gets the street_name of this IdentityAddress.  # noqa: E501


        :return: The street_name of this IdentityAddress.  # noqa: E501
        :rtype: str
        """
        return self._street_name

    @street_name.setter
    def street_name(self, street_name):
        """Sets the street_name of this IdentityAddress.


        :param street_name: The street_name of this IdentityAddress.  # noqa: E501
        :type: str
        """

        self._street_name = street_name

    @property
    def building_number(self):
        """Gets the building_number of this IdentityAddress.  # noqa: E501


        :return: The building_number of this IdentityAddress.  # noqa: E501
        :rtype: str
        """
        return self._building_number

    @building_number.setter
    def building_number(self, building_number):
        """Sets the building_number of this IdentityAddress.


        :param building_number: The building_number of this IdentityAddress.  # noqa: E501
        :type: str
        """

        self._building_number = building_number

    @property
    def type(self):
        """Gets the type of this IdentityAddress.  # noqa: E501


        :return: The type of this IdentityAddress.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IdentityAddress.


        :param type: The type of this IdentityAddress.  # noqa: E501
        :type: str
        """
        allowed_values = ["BUSINESS", "CORRESPONDENCE", "DELIVERY_TO", "MAIL_TO", "PO_BOX", "POSTAL", "RESIDENTIAL", "STATEMENT", "UNKNOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def county(self):
        """Gets the county of this IdentityAddress.  # noqa: E501


        :return: The county of this IdentityAddress.  # noqa: E501
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """Sets the county of this IdentityAddress.


        :param county: The county of this IdentityAddress.  # noqa: E501
        :type: str
        """

        self._county = county

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
        if not isinstance(other, IdentityAddress):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IdentityAddress):
            return True

        return self.to_dict() != other.to_dict()
