# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.383
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class Beneficiary(object):
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
        'trusted': 'bool',
        'reference': 'str',
        'payee': 'Payee'
    }

    attribute_map = {
        'id': 'id',
        'trusted': 'trusted',
        'reference': 'reference',
        'payee': 'payee'
    }

    def __init__(self, id=None, trusted=None, reference=None, payee=None, local_vars_configuration=None):  # noqa: E501
        """Beneficiary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._trusted = None
        self._reference = None
        self._payee = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if trusted is not None:
            self.trusted = trusted
        if reference is not None:
            self.reference = reference
        if payee is not None:
            self.payee = payee

    @property
    def id(self):
        """Gets the id of this Beneficiary.  # noqa: E501


        :return: The id of this Beneficiary.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Beneficiary.


        :param id: The id of this Beneficiary.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def trusted(self):
        """Gets the trusted of this Beneficiary.  # noqa: E501


        :return: The trusted of this Beneficiary.  # noqa: E501
        :rtype: bool
        """
        return self._trusted

    @trusted.setter
    def trusted(self, trusted):
        """Sets the trusted of this Beneficiary.


        :param trusted: The trusted of this Beneficiary.  # noqa: E501
        :type: bool
        """

        self._trusted = trusted

    @property
    def reference(self):
        """Gets the reference of this Beneficiary.  # noqa: E501


        :return: The reference of this Beneficiary.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this Beneficiary.


        :param reference: The reference of this Beneficiary.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def payee(self):
        """Gets the payee of this Beneficiary.  # noqa: E501


        :return: The payee of this Beneficiary.  # noqa: E501
        :rtype: Payee
        """
        return self._payee

    @payee.setter
    def payee(self, payee):
        """Sets the payee of this Beneficiary.


        :param payee: The payee of this Beneficiary.  # noqa: E501
        :type: Payee
        """

        self._payee = payee

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
        if not isinstance(other, Beneficiary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Beneficiary):
            return True

        return self.to_dict() != other.to_dict()
