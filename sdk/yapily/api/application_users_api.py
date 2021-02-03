# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.305
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from yapily.api_client import ApiClient
from yapily.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ApplicationUsersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_user_using_post(self, new_application_user, **kwargs):  # noqa: E501
        """Add an application user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_user_using_post(new_application_user, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param NewApplicationUser new_application_user: newApplicationUser (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ApplicationUser
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.add_user_using_post_with_http_info(new_application_user, **kwargs)  # noqa: E501

    def add_user_using_post_with_http_info(self, new_application_user, **kwargs):  # noqa: E501
        """Add an application user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_user_using_post_with_http_info(new_application_user, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param NewApplicationUser new_application_user: newApplicationUser (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ApplicationUser, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'new_application_user'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_user_using_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'new_application_user' is set
        if self.api_client.client_side_validation and ('new_application_user' not in local_var_params or  # noqa: E501
                                                        local_var_params['new_application_user'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `new_application_user` when calling `add_user_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'new_application_user' in local_var_params:
            body_params = local_var_params['new_application_user']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/users', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationUser',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_user_using_delete(self, user_uuid, **kwargs):  # noqa: E501
        """Delete an application user and sub-resources (including consent resources on institution APIs if they exist)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user_using_delete(user_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str user_uuid: userUuid (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ApiResponseOfUserDeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_user_using_delete_with_http_info(user_uuid, **kwargs)  # noqa: E501

    def delete_user_using_delete_with_http_info(self, user_uuid, **kwargs):  # noqa: E501
        """Delete an application user and sub-resources (including consent resources on institution APIs if they exist)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user_using_delete_with_http_info(user_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str user_uuid: userUuid (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ApiResponseOfUserDeleteResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'user_uuid'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user_using_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'user_uuid' is set
        if self.api_client.client_side_validation and ('user_uuid' not in local_var_params or  # noqa: E501
                                                        local_var_params['user_uuid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_uuid` when calling `delete_user_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_uuid' in local_var_params:
            path_params['userUuid'] = local_var_params['user_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/users/{userUuid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseOfUserDeleteResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_delete_users_job_using_get(self, job_id, **kwargs):  # noqa: E501
        """Get details of a user deletion job  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_delete_users_job_using_get(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str job_id: job-id (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ApiResponseOfBulkUserDeleteDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_delete_users_job_using_get_with_http_info(job_id, **kwargs)  # noqa: E501

    def get_delete_users_job_using_get_with_http_info(self, job_id, **kwargs):  # noqa: E501
        """Get details of a user deletion job  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_delete_users_job_using_get_with_http_info(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str job_id: job-id (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ApiResponseOfBulkUserDeleteDetails, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'job_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_delete_users_job_using_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'job_id' is set
        if self.api_client.client_side_validation and ('job_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['job_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `job_id` when calling `get_delete_users_job_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job-id'] = local_var_params['job_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/delete-users/{job-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseOfBulkUserDeleteDetails',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_delete_users_jobs_using_get(self, **kwargs):  # noqa: E501
        """Get details of all user deletion jobs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_delete_users_jobs_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ApiListResponseOfBulkUserDelete
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_delete_users_jobs_using_get_with_http_info(**kwargs)  # noqa: E501

    def get_delete_users_jobs_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get details of all user deletion jobs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_delete_users_jobs_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ApiListResponseOfBulkUserDelete, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_delete_users_jobs_using_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/delete-users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiListResponseOfBulkUserDelete',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_using_get(self, user_uuid, **kwargs):  # noqa: E501
        """Get an application user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_using_get(user_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str user_uuid: userUuid (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ApplicationUser
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_user_using_get_with_http_info(user_uuid, **kwargs)  # noqa: E501

    def get_user_using_get_with_http_info(self, user_uuid, **kwargs):  # noqa: E501
        """Get an application user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_using_get_with_http_info(user_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str user_uuid: userUuid (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ApplicationUser, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'user_uuid'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_using_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'user_uuid' is set
        if self.api_client.client_side_validation and ('user_uuid' not in local_var_params or  # noqa: E501
                                                        local_var_params['user_uuid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_uuid` when calling `get_user_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_uuid' in local_var_params:
            path_params['userUuid'] = local_var_params['user_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/users/{userUuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationUser',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_users_using_get(self, **kwargs):  # noqa: E501
        """Get application users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_users_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[str] filter_application_user_id: Filter users by the provided application user Id (applicationUserId) when the user was created.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[ApplicationUser]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_users_using_get_with_http_info(**kwargs)  # noqa: E501

    def get_users_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get application users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_users_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[str] filter_application_user_id: Filter users by the provided application user Id (applicationUserId) when the user was created.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[ApplicationUser], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'filter_application_user_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_users_using_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter_application_user_id' in local_var_params and local_var_params['filter_application_user_id'] is not None:  # noqa: E501
            query_params.append(('filter[applicationUserId]', local_var_params['filter_application_user_id']))  # noqa: E501
            collection_formats['filter[applicationUserId]'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ApplicationUser]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def start_delete_users_job_using_post(self, user_delete_request, **kwargs):  # noqa: E501
        """Start a job to delete application users by specifying their identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.start_delete_users_job_using_post(user_delete_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param UserDeleteRequest user_delete_request: userDeleteRequest (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ApiResponseOfBulkUserDeleteDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.start_delete_users_job_using_post_with_http_info(user_delete_request, **kwargs)  # noqa: E501

    def start_delete_users_job_using_post_with_http_info(self, user_delete_request, **kwargs):  # noqa: E501
        """Start a job to delete application users by specifying their identifiers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.start_delete_users_job_using_post_with_http_info(user_delete_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param UserDeleteRequest user_delete_request: userDeleteRequest (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ApiResponseOfBulkUserDeleteDetails, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'user_delete_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method start_delete_users_job_using_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'user_delete_request' is set
        if self.api_client.client_side_validation and ('user_delete_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['user_delete_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_delete_request` when calling `start_delete_users_job_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user_delete_request' in local_var_params:
            body_params = local_var_params['user_delete_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/delete-users', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseOfBulkUserDeleteDetails',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
