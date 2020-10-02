# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.249
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class PostalAddress1(object):
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
        'address_line': 'list[str]',
        'building_number': 'str',
        'country': 'str',
        'country_sub_division': 'list[str]',
        'geo_location': 'GeoLocation1',
        'post_code': 'str',
        'street_name': 'str',
        'town_name': 'str'
    }

    attribute_map = {
        'address_line': 'AddressLine',
        'building_number': 'BuildingNumber',
        'country': 'Country',
        'country_sub_division': 'CountrySubDivision',
        'geo_location': 'GeoLocation',
        'post_code': 'PostCode',
        'street_name': 'StreetName',
        'town_name': 'TownName'
    }

    def __init__(self, address_line=None, building_number=None, country=None, country_sub_division=None, geo_location=None, post_code=None, street_name=None, town_name=None, local_vars_configuration=None):  # noqa: E501
        """PostalAddress1 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address_line = None
        self._building_number = None
        self._country = None
        self._country_sub_division = None
        self._geo_location = None
        self._post_code = None
        self._street_name = None
        self._town_name = None
        self.discriminator = None

        if address_line is not None:
            self.address_line = address_line
        if building_number is not None:
            self.building_number = building_number
        if country is not None:
            self.country = country
        if country_sub_division is not None:
            self.country_sub_division = country_sub_division
        if geo_location is not None:
            self.geo_location = geo_location
        if post_code is not None:
            self.post_code = post_code
        if street_name is not None:
            self.street_name = street_name
        if town_name is not None:
            self.town_name = town_name

    @property
    def address_line(self):
        """Gets the address_line of this PostalAddress1.  # noqa: E501


        :return: The address_line of this PostalAddress1.  # noqa: E501
        :rtype: list[str]
        """
        return self._address_line

    @address_line.setter
    def address_line(self, address_line):
        """Sets the address_line of this PostalAddress1.


        :param address_line: The address_line of this PostalAddress1.  # noqa: E501
        :type: list[str]
        """

        self._address_line = address_line

    @property
    def building_number(self):
        """Gets the building_number of this PostalAddress1.  # noqa: E501


        :return: The building_number of this PostalAddress1.  # noqa: E501
        :rtype: str
        """
        return self._building_number

    @building_number.setter
    def building_number(self, building_number):
        """Sets the building_number of this PostalAddress1.


        :param building_number: The building_number of this PostalAddress1.  # noqa: E501
        :type: str
        """

        self._building_number = building_number

    @property
    def country(self):
        """Gets the country of this PostalAddress1.  # noqa: E501


        :return: The country of this PostalAddress1.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this PostalAddress1.


        :param country: The country of this PostalAddress1.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def country_sub_division(self):
        """Gets the country_sub_division of this PostalAddress1.  # noqa: E501


        :return: The country_sub_division of this PostalAddress1.  # noqa: E501
        :rtype: list[str]
        """
        return self._country_sub_division

    @country_sub_division.setter
    def country_sub_division(self, country_sub_division):
        """Sets the country_sub_division of this PostalAddress1.


        :param country_sub_division: The country_sub_division of this PostalAddress1.  # noqa: E501
        :type: list[str]
        """

        self._country_sub_division = country_sub_division

    @property
    def geo_location(self):
        """Gets the geo_location of this PostalAddress1.  # noqa: E501


        :return: The geo_location of this PostalAddress1.  # noqa: E501
        :rtype: GeoLocation1
        """
        return self._geo_location

    @geo_location.setter
    def geo_location(self, geo_location):
        """Sets the geo_location of this PostalAddress1.


        :param geo_location: The geo_location of this PostalAddress1.  # noqa: E501
        :type: GeoLocation1
        """

        self._geo_location = geo_location

    @property
    def post_code(self):
        """Gets the post_code of this PostalAddress1.  # noqa: E501


        :return: The post_code of this PostalAddress1.  # noqa: E501
        :rtype: str
        """
        return self._post_code

    @post_code.setter
    def post_code(self, post_code):
        """Sets the post_code of this PostalAddress1.


        :param post_code: The post_code of this PostalAddress1.  # noqa: E501
        :type: str
        """

        self._post_code = post_code

    @property
    def street_name(self):
        """Gets the street_name of this PostalAddress1.  # noqa: E501


        :return: The street_name of this PostalAddress1.  # noqa: E501
        :rtype: str
        """
        return self._street_name

    @street_name.setter
    def street_name(self, street_name):
        """Sets the street_name of this PostalAddress1.


        :param street_name: The street_name of this PostalAddress1.  # noqa: E501
        :type: str
        """

        self._street_name = street_name

    @property
    def town_name(self):
        """Gets the town_name of this PostalAddress1.  # noqa: E501


        :return: The town_name of this PostalAddress1.  # noqa: E501
        :rtype: str
        """
        return self._town_name

    @town_name.setter
    def town_name(self, town_name):
        """Sets the town_name of this PostalAddress1.


        :param town_name: The town_name of this PostalAddress1.  # noqa: E501
        :type: str
        """

        self._town_name = town_name

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
        if not isinstance(other, PostalAddress1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostalAddress1):
            return True

        return self.to_dict() != other.to_dict()
