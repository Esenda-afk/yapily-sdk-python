# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.220
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class ATMMapServiceLinks(object):
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
        'bing_maps_url': 'str',
        'google_maps_url': 'str',
        'here_maps_url': 'str'
    }

    attribute_map = {
        'bing_maps_url': 'bingMapsUrl',
        'google_maps_url': 'googleMapsUrl',
        'here_maps_url': 'hereMapsUrl'
    }

    def __init__(self, bing_maps_url=None, google_maps_url=None, here_maps_url=None, local_vars_configuration=None):  # noqa: E501
        """ATMMapServiceLinks - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bing_maps_url = None
        self._google_maps_url = None
        self._here_maps_url = None
        self.discriminator = None

        if bing_maps_url is not None:
            self.bing_maps_url = bing_maps_url
        if google_maps_url is not None:
            self.google_maps_url = google_maps_url
        if here_maps_url is not None:
            self.here_maps_url = here_maps_url

    @property
    def bing_maps_url(self):
        """Gets the bing_maps_url of this ATMMapServiceLinks.  # noqa: E501


        :return: The bing_maps_url of this ATMMapServiceLinks.  # noqa: E501
        :rtype: str
        """
        return self._bing_maps_url

    @bing_maps_url.setter
    def bing_maps_url(self, bing_maps_url):
        """Sets the bing_maps_url of this ATMMapServiceLinks.


        :param bing_maps_url: The bing_maps_url of this ATMMapServiceLinks.  # noqa: E501
        :type: str
        """

        self._bing_maps_url = bing_maps_url

    @property
    def google_maps_url(self):
        """Gets the google_maps_url of this ATMMapServiceLinks.  # noqa: E501


        :return: The google_maps_url of this ATMMapServiceLinks.  # noqa: E501
        :rtype: str
        """
        return self._google_maps_url

    @google_maps_url.setter
    def google_maps_url(self, google_maps_url):
        """Sets the google_maps_url of this ATMMapServiceLinks.


        :param google_maps_url: The google_maps_url of this ATMMapServiceLinks.  # noqa: E501
        :type: str
        """

        self._google_maps_url = google_maps_url

    @property
    def here_maps_url(self):
        """Gets the here_maps_url of this ATMMapServiceLinks.  # noqa: E501


        :return: The here_maps_url of this ATMMapServiceLinks.  # noqa: E501
        :rtype: str
        """
        return self._here_maps_url

    @here_maps_url.setter
    def here_maps_url(self, here_maps_url):
        """Sets the here_maps_url of this ATMMapServiceLinks.


        :param here_maps_url: The here_maps_url of this ATMMapServiceLinks.  # noqa: E501
        :type: str
        """

        self._here_maps_url = here_maps_url

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
        if not isinstance(other, ATMMapServiceLinks):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ATMMapServiceLinks):
            return True

        return self.to_dict() != other.to_dict()
