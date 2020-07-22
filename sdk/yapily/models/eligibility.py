# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.213
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class Eligibility(object):
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
        'age_eligibility': 'AgeEligibility',
        'credit_check': 'CreditCheck',
        'id_verification_check': 'IDVerificationCheck',
        'other_eligibility': 'list[EligibilityOtherEligibility]',
        'residency_eligibility': 'ResidencyEligibility'
    }

    attribute_map = {
        'age_eligibility': 'AgeEligibility',
        'credit_check': 'CreditCheck',
        'id_verification_check': 'IDVerificationCheck',
        'other_eligibility': 'OtherEligibility',
        'residency_eligibility': 'ResidencyEligibility'
    }

    def __init__(self, age_eligibility=None, credit_check=None, id_verification_check=None, other_eligibility=None, residency_eligibility=None, local_vars_configuration=None):  # noqa: E501
        """Eligibility - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._age_eligibility = None
        self._credit_check = None
        self._id_verification_check = None
        self._other_eligibility = None
        self._residency_eligibility = None
        self.discriminator = None

        if age_eligibility is not None:
            self.age_eligibility = age_eligibility
        if credit_check is not None:
            self.credit_check = credit_check
        if id_verification_check is not None:
            self.id_verification_check = id_verification_check
        if other_eligibility is not None:
            self.other_eligibility = other_eligibility
        if residency_eligibility is not None:
            self.residency_eligibility = residency_eligibility

    @property
    def age_eligibility(self):
        """Gets the age_eligibility of this Eligibility.  # noqa: E501


        :return: The age_eligibility of this Eligibility.  # noqa: E501
        :rtype: AgeEligibility
        """
        return self._age_eligibility

    @age_eligibility.setter
    def age_eligibility(self, age_eligibility):
        """Sets the age_eligibility of this Eligibility.


        :param age_eligibility: The age_eligibility of this Eligibility.  # noqa: E501
        :type: AgeEligibility
        """

        self._age_eligibility = age_eligibility

    @property
    def credit_check(self):
        """Gets the credit_check of this Eligibility.  # noqa: E501


        :return: The credit_check of this Eligibility.  # noqa: E501
        :rtype: CreditCheck
        """
        return self._credit_check

    @credit_check.setter
    def credit_check(self, credit_check):
        """Sets the credit_check of this Eligibility.


        :param credit_check: The credit_check of this Eligibility.  # noqa: E501
        :type: CreditCheck
        """

        self._credit_check = credit_check

    @property
    def id_verification_check(self):
        """Gets the id_verification_check of this Eligibility.  # noqa: E501


        :return: The id_verification_check of this Eligibility.  # noqa: E501
        :rtype: IDVerificationCheck
        """
        return self._id_verification_check

    @id_verification_check.setter
    def id_verification_check(self, id_verification_check):
        """Sets the id_verification_check of this Eligibility.


        :param id_verification_check: The id_verification_check of this Eligibility.  # noqa: E501
        :type: IDVerificationCheck
        """

        self._id_verification_check = id_verification_check

    @property
    def other_eligibility(self):
        """Gets the other_eligibility of this Eligibility.  # noqa: E501


        :return: The other_eligibility of this Eligibility.  # noqa: E501
        :rtype: list[EligibilityOtherEligibility]
        """
        return self._other_eligibility

    @other_eligibility.setter
    def other_eligibility(self, other_eligibility):
        """Sets the other_eligibility of this Eligibility.


        :param other_eligibility: The other_eligibility of this Eligibility.  # noqa: E501
        :type: list[EligibilityOtherEligibility]
        """

        self._other_eligibility = other_eligibility

    @property
    def residency_eligibility(self):
        """Gets the residency_eligibility of this Eligibility.  # noqa: E501


        :return: The residency_eligibility of this Eligibility.  # noqa: E501
        :rtype: ResidencyEligibility
        """
        return self._residency_eligibility

    @residency_eligibility.setter
    def residency_eligibility(self, residency_eligibility):
        """Sets the residency_eligibility of this Eligibility.


        :param residency_eligibility: The residency_eligibility of this Eligibility.  # noqa: E501
        :type: ResidencyEligibility
        """

        self._residency_eligibility = residency_eligibility

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
        if not isinstance(other, Eligibility):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Eligibility):
            return True

        return self.to_dict() != other.to_dict()
