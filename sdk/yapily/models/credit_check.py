# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.287
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class CreditCheck(object):
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
        'notes': 'list[str]',
        'scoring_type': 'str'
    }

    attribute_map = {
        'notes': 'Notes',
        'scoring_type': 'ScoringType'
    }

    def __init__(self, notes=None, scoring_type=None, local_vars_configuration=None):  # noqa: E501
        """CreditCheck - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._notes = None
        self._scoring_type = None
        self.discriminator = None

        if notes is not None:
            self.notes = notes
        if scoring_type is not None:
            self.scoring_type = scoring_type

    @property
    def notes(self):
        """Gets the notes of this CreditCheck.  # noqa: E501


        :return: The notes of this CreditCheck.  # noqa: E501
        :rtype: list[str]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this CreditCheck.


        :param notes: The notes of this CreditCheck.  # noqa: E501
        :type: list[str]
        """

        self._notes = notes

    @property
    def scoring_type(self):
        """Gets the scoring_type of this CreditCheck.  # noqa: E501


        :return: The scoring_type of this CreditCheck.  # noqa: E501
        :rtype: str
        """
        return self._scoring_type

    @scoring_type.setter
    def scoring_type(self, scoring_type):
        """Sets the scoring_type of this CreditCheck.


        :param scoring_type: The scoring_type of this CreditCheck.  # noqa: E501
        :type: str
        """
        allowed_values = ["Hard", "Soft"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and scoring_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `scoring_type` ({0}), must be one of {1}"  # noqa: E501
                .format(scoring_type, allowed_values)
            )

        self._scoring_type = scoring_type

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
        if not isinstance(other, CreditCheck):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreditCheck):
            return True

        return self.to_dict() != other.to_dict()
