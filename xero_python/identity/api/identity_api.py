# coding: utf-8

"""
    Xero oAuth 2 identity service

    This specifing endpoints related to managing authentication tokens and identity for Xero API  # noqa: E501

    OpenAPI spec version: 2.2.13
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import importlib
import re  # noqa: F401

from xero_python import exceptions
from xero_python.api_client import ApiClient, ModelFinder

try:
    from .exception_handler import translate_status_exception
except ImportError:
    translate_status_exception = exceptions.translate_status_exception


class empty:
    """ empty object to mark optional parameter not set """


class IdentityApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    base_url = "https://api.xero.com"
    models_module = importlib.import_module("xero_python.identity.models")

    def __init__(self, api_client=None, base_url=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.base_url = base_url or self.base_url

    def get_resource_url(self, resource_path):
        """
        Combine API base url with resource specific path
        :param str resource_path: API endpoint specific path
        :return: str full resource path
        """
        return self.base_url + resource_path

    def get_model_finder(self):
        return ModelFinder(self.models_module)

    def delete_connection(
        self,
        id,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Allows you to delete a connection for this user (i.e. disconnect a tenant)  # noqa: E501
        OAuth2 scope: N/A
        Override the base server url that include version  # noqa: E501
        :param str id: Unique identifier for retrieving single object (required)
        :param bool _return_http_data_only: return received data only
        :param bool _preload_content: load received data in models
        :param bool _request_timeout: maximum wait time for response
        :return: None
        """

        # verify the required parameter 'id' is set
        if id is None:
            raise ValueError(
                "Missing the required parameter `id` "
                "when calling `delete_connection`"
            )

        collection_formats = {}
        path_params = {
            "id": id,
        }

        query_params = []

        header_params = {}

        local_var_files = {}
        form_params = []

        body_params = None
        # Authentication setting
        auth_settings = ["OAuth2"]
        url = self.get_resource_url("/connections/{id}")

        try:
            return self.api_client.call_api(
                url,
                "DELETE",
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type=None,
                response_model_finder=self.get_model_finder(),
                auth_settings=auth_settings,
                _return_http_data_only=_return_http_data_only,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                collection_formats=collection_formats,
            )
        except exceptions.HTTPStatusException as error:
            raise translate_status_exception(error, self, "delete_connection")

    def get_connections(
        self,
        auth_event_id=empty,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Allows you to retrieve the connections for this user  # noqa: E501
        OAuth2 scope: N/A
        Override the base server url that include version  # noqa: E501
        :param str auth_event_id: Filter by authEventId
        :param bool _return_http_data_only: return received data only
        :param bool _preload_content: load received data in models
        :param bool _request_timeout: maximum wait time for response
        :return: list[Connection]
        """

        collection_formats = {}
        path_params = {}

        query_params = []

        if auth_event_id is not empty:
            query_params.append(("authEventId", auth_event_id))

        header_params = {}

        local_var_files = {}
        form_params = []

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # Authentication setting
        auth_settings = ["OAuth2"]
        url = self.get_resource_url("/connections")

        try:
            return self.api_client.call_api(
                url,
                "GET",
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type="list[Connection]",
                response_model_finder=self.get_model_finder(),
                auth_settings=auth_settings,
                _return_http_data_only=_return_http_data_only,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                collection_formats=collection_formats,
            )
        except exceptions.HTTPStatusException as error:
            raise translate_status_exception(error, self, "get_connections")
