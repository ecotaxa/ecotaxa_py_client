"""
    EcoTaxa

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.27
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ecotaxa_py_client.api_client import ApiClient, Endpoint as _Endpoint
from ecotaxa_py_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from ecotaxa_py_client.model.collection_model import CollectionModel
from ecotaxa_py_client.model.create_collection_req import CreateCollectionReq
from ecotaxa_py_client.model.darwin_core_export_rsp import DarwinCoreExportRsp
from ecotaxa_py_client.model.http_validation_error import HTTPValidationError


class CollectionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.collection_by_short_title_endpoint = _Endpoint(
            settings={
                'response_type': (CollectionModel,),
                'auth': [],
                'endpoint_path': '/collections/by_short_title',
                'operation_id': 'collection_by_short_title',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'q',
                ],
                'required': [
                    'q',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'q':
                        (str,),
                },
                'attribute_map': {
                    'q': 'q',
                },
                'location_map': {
                    'q': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.collection_by_title_endpoint = _Endpoint(
            settings={
                'response_type': (CollectionModel,),
                'auth': [],
                'endpoint_path': '/collections/by_title',
                'operation_id': 'collection_by_title',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'q',
                ],
                'required': [
                    'q',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'q':
                        (str,),
                },
                'attribute_map': {
                    'q': 'q',
                },
                'location_map': {
                    'q': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.create_collection_endpoint = _Endpoint(
            settings={
                'response_type': (int,),
                'auth': [
                    'BearerOrCookieAuth'
                ],
                'endpoint_path': '/collections/create',
                'operation_id': 'create_collection',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'create_collection_req',
                ],
                'required': [
                    'create_collection_req',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'create_collection_req':
                        (CreateCollectionReq,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'create_collection_req': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.darwin_core_format_export_endpoint = _Endpoint(
            settings={
                'response_type': (DarwinCoreExportRsp,),
                'auth': [
                    'BearerOrCookieAuth'
                ],
                'endpoint_path': '/collections/{collection_id}/export/darwin_core',
                'operation_id': 'darwin_core_format_export',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'collection_id',
                    'dry_run',
                    'with_zeroes',
                    'auto_morpho',
                    'with_computations',
                ],
                'required': [
                    'collection_id',
                    'dry_run',
                    'with_zeroes',
                    'auto_morpho',
                    'with_computations',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'collection_id':
                        (int,),
                    'dry_run':
                        (bool,),
                    'with_zeroes':
                        (bool,),
                    'auto_morpho':
                        (bool,),
                    'with_computations':
                        (bool,),
                },
                'attribute_map': {
                    'collection_id': 'collection_id',
                    'dry_run': 'dry_run',
                    'with_zeroes': 'with_zeroes',
                    'auto_morpho': 'auto_morpho',
                    'with_computations': 'with_computations',
                },
                'location_map': {
                    'collection_id': 'path',
                    'dry_run': 'query',
                    'with_zeroes': 'query',
                    'auto_morpho': 'query',
                    'with_computations': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.erase_collection_endpoint = _Endpoint(
            settings={
                'response_type': (int,),
                'auth': [
                    'BearerOrCookieAuth'
                ],
                'endpoint_path': '/collections/{collection_id}',
                'operation_id': 'erase_collection',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'collection_id',
                ],
                'required': [
                    'collection_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'collection_id':
                        (int,),
                },
                'attribute_map': {
                    'collection_id': 'collection_id',
                },
                'location_map': {
                    'collection_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_collection_endpoint = _Endpoint(
            settings={
                'response_type': (CollectionModel,),
                'auth': [
                    'BearerOrCookieAuth'
                ],
                'endpoint_path': '/collections/{collection_id}',
                'operation_id': 'get_collection',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'collection_id',
                ],
                'required': [
                    'collection_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'collection_id':
                        (int,),
                },
                'attribute_map': {
                    'collection_id': 'collection_id',
                },
                'location_map': {
                    'collection_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.search_collections_endpoint = _Endpoint(
            settings={
                'response_type': ([CollectionModel],),
                'auth': [
                    'BearerOrCookieAuth'
                ],
                'endpoint_path': '/collections/search',
                'operation_id': 'search_collections',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'title',
                ],
                'required': [
                    'title',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'title':
                        (str,),
                },
                'attribute_map': {
                    'title': 'title',
                },
                'location_map': {
                    'title': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.update_collection_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [
                    'BearerOrCookieAuth'
                ],
                'endpoint_path': '/collections/{collection_id}',
                'operation_id': 'update_collection',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'collection_id',
                    'collection_model',
                ],
                'required': [
                    'collection_id',
                    'collection_model',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'collection_id':
                        (int,),
                    'collection_model':
                        (CollectionModel,),
                },
                'attribute_map': {
                    'collection_id': 'collection_id',
                },
                'location_map': {
                    'collection_id': 'path',
                    'collection_model': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def collection_by_short_title(
        self,
        q,
        **kwargs
    ):
        """Collection By Short Title  # noqa: E501

        Return the **single collection with this short title**.  *For published datasets.*  ⚠️ DO NOT MODIFY BEHAVIOR ⚠️  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.collection_by_short_title(q, async_req=True)
        >>> result = thread.get()

        Args:
            q (str): Search by **exact** short title.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CollectionModel
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['q'] = \
            q
        return self.collection_by_short_title_endpoint.call_with_http_info(**kwargs)

    def collection_by_title(
        self,
        q,
        **kwargs
    ):
        """Collection By Title  # noqa: E501

        Return the **single collection with this title**.  *For published datasets.*  ⚠️ DO NOT MODIFY BEHAVIOR ⚠️  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.collection_by_title(q, async_req=True)
        >>> result = thread.get()

        Args:
            q (str): Search by **exact** title.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CollectionModel
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['q'] = \
            q
        return self.collection_by_title_endpoint.call_with_http_info(**kwargs)

    def create_collection(
        self,
        create_collection_req,
        **kwargs
    ):
        """Create Collection  # noqa: E501

        **Create a collection** with at least one project inside.  Returns the created collection Id.  🔒 *For admins only.*  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_collection(create_collection_req, async_req=True)
        >>> result = thread.get()

        Args:
            create_collection_req (CreateCollectionReq):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            int
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['create_collection_req'] = \
            create_collection_req
        return self.create_collection_endpoint.call_with_http_info(**kwargs)

    def darwin_core_format_export(
        self,
        collection_id,
        dry_run,
        with_zeroes,
        auto_morpho,
        with_computations,
        **kwargs
    ):
        """Emodnet Format Export  # noqa: E501

        **Export the collection in Darwin Core format, e.g. for EMODnet portal**, @see https://www.emodnet-ingestion.eu  Produces a DwC-A (https://dwc.tdwg.org/) archive into a temporary directory, ready for download.  Maybe useful, a reader in Python: https://python-dwca-reader.readthedocs.io/en/latest/index.html  🔒 *For admins only.*  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.darwin_core_format_export(collection_id, dry_run, with_zeroes, auto_morpho, with_computations, async_req=True)
        >>> result = thread.get()

        Args:
            collection_id (int): Internal, the unique numeric id of this collection.
            dry_run (bool): If set, then only a diagnostic of doability will be done.
            with_zeroes (bool): If set, then *absent* records will be generated, in the relevant samples, for categories present in other samples.
            auto_morpho (bool): If set, then any object classified on a Morpho category will be added to the count of the nearest Phylo parent, upward in the tree.
            with_computations (bool): If set, then an attempt will be made to compute organisms concentrations and biovolumes.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            DarwinCoreExportRsp
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['collection_id'] = \
            collection_id
        kwargs['dry_run'] = \
            dry_run
        kwargs['with_zeroes'] = \
            with_zeroes
        kwargs['auto_morpho'] = \
            auto_morpho
        kwargs['with_computations'] = \
            with_computations
        return self.darwin_core_format_export_endpoint.call_with_http_info(**kwargs)

    def erase_collection(
        self,
        collection_id,
        **kwargs
    ):
        """Erase Collection  # noqa: E501

        **Delete the collection**,  i.e. the precious fields, as the projects are just linked-at from the collection.  🔒 *For admins only.*  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.erase_collection(collection_id, async_req=True)
        >>> result = thread.get()

        Args:
            collection_id (int): Internal, the unique numeric id of this collection.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            int
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['collection_id'] = \
            collection_id
        return self.erase_collection_endpoint.call_with_http_info(**kwargs)

    def get_collection(
        self,
        collection_id,
        **kwargs
    ):
        """Get Collection  # noqa: E501

        Returns **information about the collection** corresponding to the given id.   🔒 *For admins only.*  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_collection(collection_id, async_req=True)
        >>> result = thread.get()

        Args:
            collection_id (int): Internal, the unique numeric id of this collection.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CollectionModel
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['collection_id'] = \
            collection_id
        return self.get_collection_endpoint.call_with_http_info(**kwargs)

    def search_collections(
        self,
        title,
        **kwargs
    ):
        """Search Collections  # noqa: E501

        **Search for collections.**  🔒 *For admins only.*  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_collections(title, async_req=True)
        >>> result = thread.get()

        Args:
            title (str): Search by title, use % for searching with 'any char'.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            [CollectionModel]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['title'] = \
            title
        return self.search_collections_endpoint.call_with_http_info(**kwargs)

    def update_collection(
        self,
        collection_id,
        collection_model,
        **kwargs
    ):
        """Update Collection  # noqa: E501

        **Update the collection**. Note that some updates are silently failing when not compatible  with the composing projects.   **Returns NULL upon success.**   🔒 *For admins only.*  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_collection(collection_id, collection_model, async_req=True)
        >>> result = thread.get()

        Args:
            collection_id (int): Internal, the unique numeric id of this collection.
            collection_model (CollectionModel):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            bool, date, datetime, dict, float, int, list, str, none_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['collection_id'] = \
            collection_id
        kwargs['collection_model'] = \
            collection_model
        return self.update_collection_endpoint.call_with_http_info(**kwargs)

