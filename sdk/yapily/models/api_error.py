# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.262
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class ApiError(object):
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
        'code': 'int',
        'institution_error': 'InstitutionError',
        'message': 'str',
        'source': 'str',
        'status': 'str',
        'tracing_id': 'str'
    }

    attribute_map = {
        'code': 'code',
        'institution_error': 'institutionError',
        'message': 'message',
        'source': 'source',
        'status': 'status',
        'tracing_id': 'tracingId'
    }

    def __init__(self, code=None, institution_error=None, message=None, source=None, status=None, tracing_id=None, local_vars_configuration=None):  # noqa: E501
        """ApiError - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._institution_error = None
        self._message = None
        self._source = None
        self._status = None
        self._tracing_id = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if institution_error is not None:
            self.institution_error = institution_error
        if message is not None:
            self.message = message
        if source is not None:
            self.source = source
        if status is not None:
            self.status = status
        if tracing_id is not None:
            self.tracing_id = tracing_id

    @property
    def code(self):
        """Gets the code of this ApiError.  # noqa: E501


        :return: The code of this ApiError.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ApiError.


        :param code: The code of this ApiError.  # noqa: E501
        :type: int
        """

        self._code = code

    @property
    def institution_error(self):
        """Gets the institution_error of this ApiError.  # noqa: E501


        :return: The institution_error of this ApiError.  # noqa: E501
        :rtype: InstitutionError
        """
        return self._institution_error

    @institution_error.setter
    def institution_error(self, institution_error):
        """Sets the institution_error of this ApiError.


        :param institution_error: The institution_error of this ApiError.  # noqa: E501
        :type: InstitutionError
        """

        self._institution_error = institution_error

    @property
    def message(self):
        """Gets the message of this ApiError.  # noqa: E501


        :return: The message of this ApiError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ApiError.


        :param message: The message of this ApiError.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def source(self):
        """Gets the source of this ApiError.  # noqa: E501


        :return: The source of this ApiError.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ApiError.


        :param source: The source of this ApiError.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def status(self):
        """Gets the status of this ApiError.  # noqa: E501


        :return: The status of this ApiError.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApiError.


        :param status: The status of this ApiError.  # noqa: E501
        :type: str
        """
        allowed_values = ["400", "401", "402", "403", "404", "405", "406", "407", "408", "409", "410", "411", "412", "413", "414", "415", "416", "417", "418", "419", "420", "421", "422", "423", "424", "426", "428", "429", "431", "451", "500", "501", "502", "503", "504", "505", "506", "507", "508", "509", "510", "511"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def tracing_id(self):
        """Gets the tracing_id of this ApiError.  # noqa: E501


        :return: The tracing_id of this ApiError.  # noqa: E501
        :rtype: str
        """
        return self._tracing_id

    @tracing_id.setter
    def tracing_id(self, tracing_id):
        """Sets the tracing_id of this ApiError.


        :param tracing_id: The tracing_id of this ApiError.  # noqa: E501
        :type: str
        """

        self._tracing_id = tracing_id

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
        if not isinstance(other, ApiError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiError):
            return True

        return self.to_dict() != other.to_dict()
