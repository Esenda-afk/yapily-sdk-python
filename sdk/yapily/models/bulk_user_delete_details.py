# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.358
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class BulkUserDeleteDetails(object):
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
        'invalid_application_user_ids': 'list[str]',
        'invalid_user_uuids': 'list[str]',
        'status': 'str',
        'started_at': 'datetime',
        'users': 'list[UserDeleteResponse]',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'invalid_application_user_ids': 'invalidApplicationUserIds',
        'invalid_user_uuids': 'invalidUserUuids',
        'status': 'status',
        'started_at': 'startedAt',
        'users': 'users',
        'links': 'links'
    }

    def __init__(self, id=None, invalid_application_user_ids=None, invalid_user_uuids=None, status=None, started_at=None, users=None, links=None, local_vars_configuration=None):  # noqa: E501
        """BulkUserDeleteDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._invalid_application_user_ids = None
        self._invalid_user_uuids = None
        self._status = None
        self._started_at = None
        self._users = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if invalid_application_user_ids is not None:
            self.invalid_application_user_ids = invalid_application_user_ids
        if invalid_user_uuids is not None:
            self.invalid_user_uuids = invalid_user_uuids
        if status is not None:
            self.status = status
        if started_at is not None:
            self.started_at = started_at
        if users is not None:
            self.users = users
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this BulkUserDeleteDetails.  # noqa: E501


        :return: The id of this BulkUserDeleteDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BulkUserDeleteDetails.


        :param id: The id of this BulkUserDeleteDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def invalid_application_user_ids(self):
        """Gets the invalid_application_user_ids of this BulkUserDeleteDetails.  # noqa: E501


        :return: The invalid_application_user_ids of this BulkUserDeleteDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._invalid_application_user_ids

    @invalid_application_user_ids.setter
    def invalid_application_user_ids(self, invalid_application_user_ids):
        """Sets the invalid_application_user_ids of this BulkUserDeleteDetails.


        :param invalid_application_user_ids: The invalid_application_user_ids of this BulkUserDeleteDetails.  # noqa: E501
        :type: list[str]
        """

        self._invalid_application_user_ids = invalid_application_user_ids

    @property
    def invalid_user_uuids(self):
        """Gets the invalid_user_uuids of this BulkUserDeleteDetails.  # noqa: E501


        :return: The invalid_user_uuids of this BulkUserDeleteDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._invalid_user_uuids

    @invalid_user_uuids.setter
    def invalid_user_uuids(self, invalid_user_uuids):
        """Sets the invalid_user_uuids of this BulkUserDeleteDetails.


        :param invalid_user_uuids: The invalid_user_uuids of this BulkUserDeleteDetails.  # noqa: E501
        :type: list[str]
        """

        self._invalid_user_uuids = invalid_user_uuids

    @property
    def status(self):
        """Gets the status of this BulkUserDeleteDetails.  # noqa: E501


        :return: The status of this BulkUserDeleteDetails.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BulkUserDeleteDetails.


        :param status: The status of this BulkUserDeleteDetails.  # noqa: E501
        :type: str
        """
        allowed_values = ["IN_PROGRESS", "COMPLETED", "FAILED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def started_at(self):
        """Gets the started_at of this BulkUserDeleteDetails.  # noqa: E501


        :return: The started_at of this BulkUserDeleteDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this BulkUserDeleteDetails.


        :param started_at: The started_at of this BulkUserDeleteDetails.  # noqa: E501
        :type: datetime
        """

        self._started_at = started_at

    @property
    def users(self):
        """Gets the users of this BulkUserDeleteDetails.  # noqa: E501


        :return: The users of this BulkUserDeleteDetails.  # noqa: E501
        :rtype: list[UserDeleteResponse]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this BulkUserDeleteDetails.


        :param users: The users of this BulkUserDeleteDetails.  # noqa: E501
        :type: list[UserDeleteResponse]
        """

        self._users = users

    @property
    def links(self):
        """Gets the links of this BulkUserDeleteDetails.  # noqa: E501


        :return: The links of this BulkUserDeleteDetails.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this BulkUserDeleteDetails.


        :param links: The links of this BulkUserDeleteDetails.  # noqa: E501
        :type: dict(str, str)
        """

        self._links = links

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
        if not isinstance(other, BulkUserDeleteDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BulkUserDeleteDetails):
            return True

        return self.to_dict() != other.to_dict()
