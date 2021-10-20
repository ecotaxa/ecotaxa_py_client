"""
    EcoTaxa

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.17
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ecotaxa_cli_py.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from ecotaxa_cli_py.exceptions import ApiAttributeError



class ObjectHeaderModel(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'objid': (int,),  # noqa: E501
            'acquisid': (int,),  # noqa: E501
            'orig_id': (str,),  # noqa: E501
            'objdate': (date,),  # noqa: E501
            'objtime': (str,),  # noqa: E501
            'latitude': (float,),  # noqa: E501
            'longitude': (float,),  # noqa: E501
            'depth_min': (float,),  # noqa: E501
            'depth_max': (float,),  # noqa: E501
            'sunpos': (str,),  # noqa: E501
            'classif_id': (int,),  # noqa: E501
            'classif_qual': (str,),  # noqa: E501
            'classif_who': (int,),  # noqa: E501
            'classif_when': (datetime,),  # noqa: E501
            'classif_auto_id': (int,),  # noqa: E501
            'classif_auto_score': (float,),  # noqa: E501
            'classif_auto_when': (datetime,),  # noqa: E501
            'classif_crossvalidation_id': (int,),  # noqa: E501
            'complement_info': (str,),  # noqa: E501
            'similarity': (float,),  # noqa: E501
            'random_value': (int,),  # noqa: E501
            'object_link': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'objid': 'objid',  # noqa: E501
        'acquisid': 'acquisid',  # noqa: E501
        'orig_id': 'orig_id',  # noqa: E501
        'objdate': 'objdate',  # noqa: E501
        'objtime': 'objtime',  # noqa: E501
        'latitude': 'latitude',  # noqa: E501
        'longitude': 'longitude',  # noqa: E501
        'depth_min': 'depth_min',  # noqa: E501
        'depth_max': 'depth_max',  # noqa: E501
        'sunpos': 'sunpos',  # noqa: E501
        'classif_id': 'classif_id',  # noqa: E501
        'classif_qual': 'classif_qual',  # noqa: E501
        'classif_who': 'classif_who',  # noqa: E501
        'classif_when': 'classif_when',  # noqa: E501
        'classif_auto_id': 'classif_auto_id',  # noqa: E501
        'classif_auto_score': 'classif_auto_score',  # noqa: E501
        'classif_auto_when': 'classif_auto_when',  # noqa: E501
        'classif_crossvalidation_id': 'classif_crossvalidation_id',  # noqa: E501
        'complement_info': 'complement_info',  # noqa: E501
        'similarity': 'similarity',  # noqa: E501
        'random_value': 'random_value',  # noqa: E501
        'object_link': 'object_link',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, objid, acquisid, orig_id, *args, **kwargs):  # noqa: E501
        """ObjectHeaderModel - a model defined in OpenAPI

        Args:
            objid (int):
            acquisid (int):
            orig_id (str):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            objdate (date): [optional]  # noqa: E501
            objtime (str): [optional]  # noqa: E501
            latitude (float): [optional]  # noqa: E501
            longitude (float): [optional]  # noqa: E501
            depth_min (float): [optional]  # noqa: E501
            depth_max (float): [optional]  # noqa: E501
            sunpos (str): [optional]  # noqa: E501
            classif_id (int): [optional]  # noqa: E501
            classif_qual (str): [optional]  # noqa: E501
            classif_who (int): [optional]  # noqa: E501
            classif_when (datetime): [optional]  # noqa: E501
            classif_auto_id (int): [optional]  # noqa: E501
            classif_auto_score (float): [optional]  # noqa: E501
            classif_auto_when (datetime): [optional]  # noqa: E501
            classif_crossvalidation_id (int): [optional]  # noqa: E501
            complement_info (str): [optional]  # noqa: E501
            similarity (float): [optional]  # noqa: E501
            random_value (int): [optional]  # noqa: E501
            object_link (str): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.objid = objid
        self.acquisid = acquisid
        self.orig_id = orig_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, objid, acquisid, orig_id, *args, **kwargs):  # noqa: E501
        """ObjectHeaderModel - a model defined in OpenAPI

        Args:
            objid (int):
            acquisid (int):
            orig_id (str):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            objdate (date): [optional]  # noqa: E501
            objtime (str): [optional]  # noqa: E501
            latitude (float): [optional]  # noqa: E501
            longitude (float): [optional]  # noqa: E501
            depth_min (float): [optional]  # noqa: E501
            depth_max (float): [optional]  # noqa: E501
            sunpos (str): [optional]  # noqa: E501
            classif_id (int): [optional]  # noqa: E501
            classif_qual (str): [optional]  # noqa: E501
            classif_who (int): [optional]  # noqa: E501
            classif_when (datetime): [optional]  # noqa: E501
            classif_auto_id (int): [optional]  # noqa: E501
            classif_auto_score (float): [optional]  # noqa: E501
            classif_auto_when (datetime): [optional]  # noqa: E501
            classif_crossvalidation_id (int): [optional]  # noqa: E501
            complement_info (str): [optional]  # noqa: E501
            similarity (float): [optional]  # noqa: E501
            random_value (int): [optional]  # noqa: E501
            object_link (str): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.objid = objid
        self.acquisid = acquisid
        self.orig_id = orig_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
