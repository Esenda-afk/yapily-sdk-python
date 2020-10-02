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


class ConsentDeleteResponse(object):
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
        'delete_status': 'str',
        'institution_id': 'str',
        'institution_consent_id': 'str',
        'creation_date': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'delete_status': 'deleteStatus',
        'institution_id': 'institutionId',
        'institution_consent_id': 'institutionConsentId',
        'creation_date': 'creationDate'
    }

    def __init__(self, id=None, delete_status=None, institution_id=None, institution_consent_id=None, creation_date=None, local_vars_configuration=None):  # noqa: E501
        """ConsentDeleteResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._delete_status = None
        self._institution_id = None
        self._institution_consent_id = None
        self._creation_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if delete_status is not None:
            self.delete_status = delete_status
        if institution_id is not None:
            self.institution_id = institution_id
        if institution_consent_id is not None:
            self.institution_consent_id = institution_consent_id
        if creation_date is not None:
            self.creation_date = creation_date

    @property
    def id(self):
        """Gets the id of this ConsentDeleteResponse.  # noqa: E501


        :return: The id of this ConsentDeleteResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConsentDeleteResponse.


        :param id: The id of this ConsentDeleteResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def delete_status(self):
        """Gets the delete_status of this ConsentDeleteResponse.  # noqa: E501


        :return: The delete_status of this ConsentDeleteResponse.  # noqa: E501
        :rtype: str
        """
        return self._delete_status

    @delete_status.setter
    def delete_status(self, delete_status):
        """Sets the delete_status of this ConsentDeleteResponse.


        :param delete_status: The delete_status of this ConsentDeleteResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["SUCCESS", "FAILED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and delete_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `delete_status` ({0}), must be one of {1}"  # noqa: E501
                .format(delete_status, allowed_values)
            )

        self._delete_status = delete_status

    @property
    def institution_id(self):
        """Gets the institution_id of this ConsentDeleteResponse.  # noqa: E501


        :return: The institution_id of this ConsentDeleteResponse.  # noqa: E501
        :rtype: str
        """
        return self._institution_id

    @institution_id.setter
    def institution_id(self, institution_id):
        """Sets the institution_id of this ConsentDeleteResponse.


        :param institution_id: The institution_id of this ConsentDeleteResponse.  # noqa: E501
        :type: str
        """

        self._institution_id = institution_id

    @property
    def institution_consent_id(self):
        """Gets the institution_consent_id of this ConsentDeleteResponse.  # noqa: E501


        :return: The institution_consent_id of this ConsentDeleteResponse.  # noqa: E501
        :rtype: str
        """
        return self._institution_consent_id

    @institution_consent_id.setter
    def institution_consent_id(self, institution_consent_id):
        """Sets the institution_consent_id of this ConsentDeleteResponse.


        :param institution_consent_id: The institution_consent_id of this ConsentDeleteResponse.  # noqa: E501
        :type: str
        """

        self._institution_consent_id = institution_consent_id

    @property
    def creation_date(self):
        """Gets the creation_date of this ConsentDeleteResponse.  # noqa: E501


        :return: The creation_date of this ConsentDeleteResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ConsentDeleteResponse.


        :param creation_date: The creation_date of this ConsentDeleteResponse.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

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
        if not isinstance(other, ConsentDeleteResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConsentDeleteResponse):
            return True

        return self.to_dict() != other.to_dict()
