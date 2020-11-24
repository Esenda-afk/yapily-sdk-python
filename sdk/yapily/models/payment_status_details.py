# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.279
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class PaymentStatusDetails(object):
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
        'status': 'str',
        'status_reason': 'str',
        'status_reason_description': 'str',
        'status_update_date': 'datetime',
        'multi_authorisation_status': 'MultiAuthorisation'
    }

    attribute_map = {
        'status': 'status',
        'status_reason': 'statusReason',
        'status_reason_description': 'statusReasonDescription',
        'status_update_date': 'statusUpdateDate',
        'multi_authorisation_status': 'multiAuthorisationStatus'
    }

    def __init__(self, status=None, status_reason=None, status_reason_description=None, status_update_date=None, multi_authorisation_status=None, local_vars_configuration=None):  # noqa: E501
        """PaymentStatusDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._status_reason = None
        self._status_reason_description = None
        self._status_update_date = None
        self._multi_authorisation_status = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if status_reason is not None:
            self.status_reason = status_reason
        if status_reason_description is not None:
            self.status_reason_description = status_reason_description
        if status_update_date is not None:
            self.status_update_date = status_update_date
        if multi_authorisation_status is not None:
            self.multi_authorisation_status = multi_authorisation_status

    @property
    def status(self):
        """Gets the status of this PaymentStatusDetails.  # noqa: E501


        :return: The status of this PaymentStatusDetails.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PaymentStatusDetails.


        :param status: The status of this PaymentStatusDetails.  # noqa: E501
        :type: str
        """
        allowed_values = ["PENDING", "FAILED", "DECLINED", "COMPLETED", "COMPLETED_SETTLEMENT_IN_PROCESS", "EXPIRED", "UNKNOWN", "ACTIVE", "INACTIVE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def status_reason(self):
        """Gets the status_reason of this PaymentStatusDetails.  # noqa: E501


        :return: The status_reason of this PaymentStatusDetails.  # noqa: E501
        :rtype: str
        """
        return self._status_reason

    @status_reason.setter
    def status_reason(self, status_reason):
        """Sets the status_reason of this PaymentStatusDetails.


        :param status_reason: The status_reason of this PaymentStatusDetails.  # noqa: E501
        :type: str
        """

        self._status_reason = status_reason

    @property
    def status_reason_description(self):
        """Gets the status_reason_description of this PaymentStatusDetails.  # noqa: E501


        :return: The status_reason_description of this PaymentStatusDetails.  # noqa: E501
        :rtype: str
        """
        return self._status_reason_description

    @status_reason_description.setter
    def status_reason_description(self, status_reason_description):
        """Sets the status_reason_description of this PaymentStatusDetails.


        :param status_reason_description: The status_reason_description of this PaymentStatusDetails.  # noqa: E501
        :type: str
        """

        self._status_reason_description = status_reason_description

    @property
    def status_update_date(self):
        """Gets the status_update_date of this PaymentStatusDetails.  # noqa: E501


        :return: The status_update_date of this PaymentStatusDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._status_update_date

    @status_update_date.setter
    def status_update_date(self, status_update_date):
        """Sets the status_update_date of this PaymentStatusDetails.


        :param status_update_date: The status_update_date of this PaymentStatusDetails.  # noqa: E501
        :type: datetime
        """

        self._status_update_date = status_update_date

    @property
    def multi_authorisation_status(self):
        """Gets the multi_authorisation_status of this PaymentStatusDetails.  # noqa: E501


        :return: The multi_authorisation_status of this PaymentStatusDetails.  # noqa: E501
        :rtype: MultiAuthorisation
        """
        return self._multi_authorisation_status

    @multi_authorisation_status.setter
    def multi_authorisation_status(self, multi_authorisation_status):
        """Sets the multi_authorisation_status of this PaymentStatusDetails.


        :param multi_authorisation_status: The multi_authorisation_status of this PaymentStatusDetails.  # noqa: E501
        :type: MultiAuthorisation
        """

        self._multi_authorisation_status = multi_authorisation_status

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
        if not isinstance(other, PaymentStatusDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentStatusDetails):
            return True

        return self.to_dict() != other.to_dict()
