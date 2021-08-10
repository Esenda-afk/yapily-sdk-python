# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.398
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class BulkPaymentEmbeddedAuthorisationRequest(object):
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
        'user_uuid': 'str',
        'application_user_id': 'str',
        'forward_parameters': 'list[str]',
        'institution_id': 'str',
        'callback': 'str',
        'one_time_token': 'bool',
        'redirect': 'RedirectRequest',
        'payment_request': 'BulkPaymentRequest',
        'user_credentials': 'UserCredentials',
        'selected_sca_method': 'ScaMethod',
        'sca_code': 'str'
    }

    attribute_map = {
        'user_uuid': 'userUuid',
        'application_user_id': 'applicationUserId',
        'forward_parameters': 'forwardParameters',
        'institution_id': 'institutionId',
        'callback': 'callback',
        'one_time_token': 'oneTimeToken',
        'redirect': 'redirect',
        'payment_request': 'paymentRequest',
        'user_credentials': 'userCredentials',
        'selected_sca_method': 'selectedScaMethod',
        'sca_code': 'scaCode'
    }

    def __init__(self, user_uuid=None, application_user_id=None, forward_parameters=None, institution_id=None, callback=None, one_time_token=None, redirect=None, payment_request=None, user_credentials=None, selected_sca_method=None, sca_code=None, local_vars_configuration=None):  # noqa: E501
        """BulkPaymentEmbeddedAuthorisationRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_uuid = None
        self._application_user_id = None
        self._forward_parameters = None
        self._institution_id = None
        self._callback = None
        self._one_time_token = None
        self._redirect = None
        self._payment_request = None
        self._user_credentials = None
        self._selected_sca_method = None
        self._sca_code = None
        self.discriminator = None

        if user_uuid is not None:
            self.user_uuid = user_uuid
        if application_user_id is not None:
            self.application_user_id = application_user_id
        if forward_parameters is not None:
            self.forward_parameters = forward_parameters
        self.institution_id = institution_id
        self.callback = callback
        self.one_time_token = one_time_token
        if redirect is not None:
            self.redirect = redirect
        self.payment_request = payment_request
        if user_credentials is not None:
            self.user_credentials = user_credentials
        if selected_sca_method is not None:
            self.selected_sca_method = selected_sca_method
        if sca_code is not None:
            self.sca_code = sca_code

    @property
    def user_uuid(self):
        """Gets the user_uuid of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501


        :return: The user_uuid of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this BulkPaymentEmbeddedAuthorisationRequest.


        :param user_uuid: The user_uuid of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501
        :type: str
        """

        self._user_uuid = user_uuid

    @property
    def application_user_id(self):
        """Gets the application_user_id of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501


        :return: The application_user_id of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._application_user_id

    @application_user_id.setter
    def application_user_id(self, application_user_id):
        """Sets the application_user_id of this BulkPaymentEmbeddedAuthorisationRequest.


        :param application_user_id: The application_user_id of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501
        :type: str
        """

        self._application_user_id = application_user_id

    @property
    def forward_parameters(self):
        """Gets the forward_parameters of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501


        :return: The forward_parameters of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._forward_parameters

    @forward_parameters.setter
    def forward_parameters(self, forward_parameters):
        """Sets the forward_parameters of this BulkPaymentEmbeddedAuthorisationRequest.


        :param forward_parameters: The forward_parameters of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501
        :type: list[str]
        """

        self._forward_parameters = forward_parameters

    @property
    def institution_id(self):
        """Gets the institution_id of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501


        :return: The institution_id of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._institution_id

    @institution_id.setter
    def institution_id(self, institution_id):
        """Sets the institution_id of this BulkPaymentEmbeddedAuthorisationRequest.


        :param institution_id: The institution_id of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and institution_id is None:  # noqa: E501
            raise ValueError("Invalid value for `institution_id`, must not be `None`")  # noqa: E501

        self._institution_id = institution_id

    @property
    def callback(self):
        """Gets the callback of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501


        :return: The callback of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._callback

    @callback.setter
    def callback(self, callback):
        """Sets the callback of this BulkPaymentEmbeddedAuthorisationRequest.


        :param callback: The callback of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and callback is None:  # noqa: E501
            raise ValueError("Invalid value for `callback`, must not be `None`")  # noqa: E501

        self._callback = callback

    @property
    def one_time_token(self):
        """Gets the one_time_token of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501


        :return: The one_time_token of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501
        :rtype: bool
        """
        return self._one_time_token

    @one_time_token.setter
    def one_time_token(self, one_time_token):
        """Sets the one_time_token of this BulkPaymentEmbeddedAuthorisationRequest.


        :param one_time_token: The one_time_token of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and one_time_token is None:  # noqa: E501
            raise ValueError("Invalid value for `one_time_token`, must not be `None`")  # noqa: E501

        self._one_time_token = one_time_token

    @property
    def redirect(self):
        """Gets the redirect of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501


        :return: The redirect of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501
        :rtype: RedirectRequest
        """
        return self._redirect

    @redirect.setter
    def redirect(self, redirect):
        """Sets the redirect of this BulkPaymentEmbeddedAuthorisationRequest.


        :param redirect: The redirect of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501
        :type: RedirectRequest
        """

        self._redirect = redirect

    @property
    def payment_request(self):
        """Gets the payment_request of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501


        :return: The payment_request of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501
        :rtype: BulkPaymentRequest
        """
        return self._payment_request

    @payment_request.setter
    def payment_request(self, payment_request):
        """Sets the payment_request of this BulkPaymentEmbeddedAuthorisationRequest.


        :param payment_request: The payment_request of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501
        :type: BulkPaymentRequest
        """
        if self.local_vars_configuration.client_side_validation and payment_request is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_request`, must not be `None`")  # noqa: E501

        self._payment_request = payment_request

    @property
    def user_credentials(self):
        """Gets the user_credentials of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501


        :return: The user_credentials of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501
        :rtype: UserCredentials
        """
        return self._user_credentials

    @user_credentials.setter
    def user_credentials(self, user_credentials):
        """Sets the user_credentials of this BulkPaymentEmbeddedAuthorisationRequest.


        :param user_credentials: The user_credentials of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501
        :type: UserCredentials
        """

        self._user_credentials = user_credentials

    @property
    def selected_sca_method(self):
        """Gets the selected_sca_method of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501


        :return: The selected_sca_method of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501
        :rtype: ScaMethod
        """
        return self._selected_sca_method

    @selected_sca_method.setter
    def selected_sca_method(self, selected_sca_method):
        """Sets the selected_sca_method of this BulkPaymentEmbeddedAuthorisationRequest.


        :param selected_sca_method: The selected_sca_method of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501
        :type: ScaMethod
        """

        self._selected_sca_method = selected_sca_method

    @property
    def sca_code(self):
        """Gets the sca_code of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501


        :return: The sca_code of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._sca_code

    @sca_code.setter
    def sca_code(self, sca_code):
        """Sets the sca_code of this BulkPaymentEmbeddedAuthorisationRequest.


        :param sca_code: The sca_code of this BulkPaymentEmbeddedAuthorisationRequest.  # noqa: E501
        :type: str
        """

        self._sca_code = sca_code

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
        if not isinstance(other, BulkPaymentEmbeddedAuthorisationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BulkPaymentEmbeddedAuthorisationRequest):
            return True

        return self.to_dict() != other.to_dict()
