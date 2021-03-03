# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.312
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class URL(object):
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
        'authority': 'str',
        'content': 'object',
        'default_port': 'int',
        'file': 'str',
        'host': 'str',
        'path': 'str',
        'port': 'int',
        'protocol': 'str',
        'query': 'str',
        'ref': 'str',
        'user_info': 'str'
    }

    attribute_map = {
        'authority': 'authority',
        'content': 'content',
        'default_port': 'defaultPort',
        'file': 'file',
        'host': 'host',
        'path': 'path',
        'port': 'port',
        'protocol': 'protocol',
        'query': 'query',
        'ref': 'ref',
        'user_info': 'userInfo'
    }

    def __init__(self, authority=None, content=None, default_port=None, file=None, host=None, path=None, port=None, protocol=None, query=None, ref=None, user_info=None, local_vars_configuration=None):  # noqa: E501
        """URL - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._authority = None
        self._content = None
        self._default_port = None
        self._file = None
        self._host = None
        self._path = None
        self._port = None
        self._protocol = None
        self._query = None
        self._ref = None
        self._user_info = None
        self.discriminator = None

        if authority is not None:
            self.authority = authority
        if content is not None:
            self.content = content
        if default_port is not None:
            self.default_port = default_port
        if file is not None:
            self.file = file
        if host is not None:
            self.host = host
        if path is not None:
            self.path = path
        if port is not None:
            self.port = port
        if protocol is not None:
            self.protocol = protocol
        if query is not None:
            self.query = query
        if ref is not None:
            self.ref = ref
        if user_info is not None:
            self.user_info = user_info

    @property
    def authority(self):
        """Gets the authority of this URL.  # noqa: E501


        :return: The authority of this URL.  # noqa: E501
        :rtype: str
        """
        return self._authority

    @authority.setter
    def authority(self, authority):
        """Sets the authority of this URL.


        :param authority: The authority of this URL.  # noqa: E501
        :type: str
        """

        self._authority = authority

    @property
    def content(self):
        """Gets the content of this URL.  # noqa: E501


        :return: The content of this URL.  # noqa: E501
        :rtype: object
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this URL.


        :param content: The content of this URL.  # noqa: E501
        :type: object
        """

        self._content = content

    @property
    def default_port(self):
        """Gets the default_port of this URL.  # noqa: E501


        :return: The default_port of this URL.  # noqa: E501
        :rtype: int
        """
        return self._default_port

    @default_port.setter
    def default_port(self, default_port):
        """Sets the default_port of this URL.


        :param default_port: The default_port of this URL.  # noqa: E501
        :type: int
        """

        self._default_port = default_port

    @property
    def file(self):
        """Gets the file of this URL.  # noqa: E501


        :return: The file of this URL.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this URL.


        :param file: The file of this URL.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def host(self):
        """Gets the host of this URL.  # noqa: E501


        :return: The host of this URL.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this URL.


        :param host: The host of this URL.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def path(self):
        """Gets the path of this URL.  # noqa: E501


        :return: The path of this URL.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this URL.


        :param path: The path of this URL.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def port(self):
        """Gets the port of this URL.  # noqa: E501


        :return: The port of this URL.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this URL.


        :param port: The port of this URL.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this URL.  # noqa: E501


        :return: The protocol of this URL.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this URL.


        :param protocol: The protocol of this URL.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def query(self):
        """Gets the query of this URL.  # noqa: E501


        :return: The query of this URL.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this URL.


        :param query: The query of this URL.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def ref(self):
        """Gets the ref of this URL.  # noqa: E501


        :return: The ref of this URL.  # noqa: E501
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this URL.


        :param ref: The ref of this URL.  # noqa: E501
        :type: str
        """

        self._ref = ref

    @property
    def user_info(self):
        """Gets the user_info of this URL.  # noqa: E501


        :return: The user_info of this URL.  # noqa: E501
        :rtype: str
        """
        return self._user_info

    @user_info.setter
    def user_info(self, user_info):
        """Sets the user_info of this URL.


        :param user_info: The user_info of this URL.  # noqa: E501
        :type: str
        """

        self._user_info = user_info

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
        if not isinstance(other, URL):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, URL):
            return True

        return self.to_dict() != other.to_dict()
