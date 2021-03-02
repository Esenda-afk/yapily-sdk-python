# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.311
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class CoreProduct(object):
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
        'monthly_maximum_charge': 'str',
        'product_description': 'str',
        'product_url': 'str',
        'sales_access_channels': 'list[str]',
        'servicing_access_channels': 'list[str]',
        'tcs_and_cs_url': 'str'
    }

    attribute_map = {
        'monthly_maximum_charge': 'MonthlyMaximumCharge',
        'product_description': 'ProductDescription',
        'product_url': 'ProductURL',
        'sales_access_channels': 'SalesAccessChannels',
        'servicing_access_channels': 'ServicingAccessChannels',
        'tcs_and_cs_url': 'TcsAndCsURL'
    }

    def __init__(self, monthly_maximum_charge=None, product_description=None, product_url=None, sales_access_channels=None, servicing_access_channels=None, tcs_and_cs_url=None, local_vars_configuration=None):  # noqa: E501
        """CoreProduct - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._monthly_maximum_charge = None
        self._product_description = None
        self._product_url = None
        self._sales_access_channels = None
        self._servicing_access_channels = None
        self._tcs_and_cs_url = None
        self.discriminator = None

        if monthly_maximum_charge is not None:
            self.monthly_maximum_charge = monthly_maximum_charge
        if product_description is not None:
            self.product_description = product_description
        if product_url is not None:
            self.product_url = product_url
        if sales_access_channels is not None:
            self.sales_access_channels = sales_access_channels
        if servicing_access_channels is not None:
            self.servicing_access_channels = servicing_access_channels
        if tcs_and_cs_url is not None:
            self.tcs_and_cs_url = tcs_and_cs_url

    @property
    def monthly_maximum_charge(self):
        """Gets the monthly_maximum_charge of this CoreProduct.  # noqa: E501


        :return: The monthly_maximum_charge of this CoreProduct.  # noqa: E501
        :rtype: str
        """
        return self._monthly_maximum_charge

    @monthly_maximum_charge.setter
    def monthly_maximum_charge(self, monthly_maximum_charge):
        """Sets the monthly_maximum_charge of this CoreProduct.


        :param monthly_maximum_charge: The monthly_maximum_charge of this CoreProduct.  # noqa: E501
        :type: str
        """

        self._monthly_maximum_charge = monthly_maximum_charge

    @property
    def product_description(self):
        """Gets the product_description of this CoreProduct.  # noqa: E501


        :return: The product_description of this CoreProduct.  # noqa: E501
        :rtype: str
        """
        return self._product_description

    @product_description.setter
    def product_description(self, product_description):
        """Sets the product_description of this CoreProduct.


        :param product_description: The product_description of this CoreProduct.  # noqa: E501
        :type: str
        """

        self._product_description = product_description

    @property
    def product_url(self):
        """Gets the product_url of this CoreProduct.  # noqa: E501


        :return: The product_url of this CoreProduct.  # noqa: E501
        :rtype: str
        """
        return self._product_url

    @product_url.setter
    def product_url(self, product_url):
        """Sets the product_url of this CoreProduct.


        :param product_url: The product_url of this CoreProduct.  # noqa: E501
        :type: str
        """

        self._product_url = product_url

    @property
    def sales_access_channels(self):
        """Gets the sales_access_channels of this CoreProduct.  # noqa: E501


        :return: The sales_access_channels of this CoreProduct.  # noqa: E501
        :rtype: list[str]
        """
        return self._sales_access_channels

    @sales_access_channels.setter
    def sales_access_channels(self, sales_access_channels):
        """Sets the sales_access_channels of this CoreProduct.


        :param sales_access_channels: The sales_access_channels of this CoreProduct.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Branch", "CallCentre", "Post", "Online", "RelationshipManager"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(sales_access_channels).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `sales_access_channels` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(sales_access_channels) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._sales_access_channels = sales_access_channels

    @property
    def servicing_access_channels(self):
        """Gets the servicing_access_channels of this CoreProduct.  # noqa: E501


        :return: The servicing_access_channels of this CoreProduct.  # noqa: E501
        :rtype: list[str]
        """
        return self._servicing_access_channels

    @servicing_access_channels.setter
    def servicing_access_channels(self, servicing_access_channels):
        """Sets the servicing_access_channels of this CoreProduct.


        :param servicing_access_channels: The servicing_access_channels of this CoreProduct.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ATM", "Branch", "CallCentre", "Post", "MobileBankingApp", "Online", "PostOffice", "RelationshipManager", "Text"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(servicing_access_channels).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `servicing_access_channels` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(servicing_access_channels) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._servicing_access_channels = servicing_access_channels

    @property
    def tcs_and_cs_url(self):
        """Gets the tcs_and_cs_url of this CoreProduct.  # noqa: E501


        :return: The tcs_and_cs_url of this CoreProduct.  # noqa: E501
        :rtype: str
        """
        return self._tcs_and_cs_url

    @tcs_and_cs_url.setter
    def tcs_and_cs_url(self, tcs_and_cs_url):
        """Sets the tcs_and_cs_url of this CoreProduct.


        :param tcs_and_cs_url: The tcs_and_cs_url of this CoreProduct.  # noqa: E501
        :type: str
        """

        self._tcs_and_cs_url = tcs_and_cs_url

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
        if not isinstance(other, CoreProduct):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CoreProduct):
            return True

        return self.to_dict() != other.to_dict()
