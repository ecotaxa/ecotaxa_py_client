"""
    EcoTaxa

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.24
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ecotaxa_py_client.model_utils import (  # noqa: F401
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
from ecotaxa_py_client.exceptions import ApiAttributeError


def lazy_import():
    from ecotaxa_py_client.model.user_model import UserModel
    globals()['UserModel'] = UserModel


class ProjectModel(ModelNormal):
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
        lazy_import()
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
        lazy_import()
        return {
            'license': (str,),  # noqa: E501
            'projid': (int,),  # noqa: E501
            'title': (str,),  # noqa: E501
            'obj_free_cols': ({str: (str,)},),  # noqa: E501
            'sample_free_cols': ({str: (str,)},),  # noqa: E501
            'acquisition_free_cols': ({str: (str,)},),  # noqa: E501
            'process_free_cols': ({str: (str,)},),  # noqa: E501
            'init_classif_list': ([int],),  # noqa: E501
            'managers': ([UserModel],),  # noqa: E501
            'annotators': ([UserModel],),  # noqa: E501
            'viewers': ([UserModel],),  # noqa: E501
            'instrument': (str,),  # noqa: E501
            'contact': (dict,),  # noqa: E501
            'highest_right': (str,),  # noqa: E501
            'visible': (bool,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'objcount': (float,),  # noqa: E501
            'pctvalidated': (float,),  # noqa: E501
            'pctclassified': (float,),  # noqa: E501
            'classifsettings': (str,),  # noqa: E501
            'classiffieldlist': (str,),  # noqa: E501
            'popoverfieldlist': (str,),  # noqa: E501
            'comments': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'rf_models_used': (str,),  # noqa: E501
            'cnn_network_id': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'license': 'license',  # noqa: E501
        'projid': 'projid',  # noqa: E501
        'title': 'title',  # noqa: E501
        'obj_free_cols': 'obj_free_cols',  # noqa: E501
        'sample_free_cols': 'sample_free_cols',  # noqa: E501
        'acquisition_free_cols': 'acquisition_free_cols',  # noqa: E501
        'process_free_cols': 'process_free_cols',  # noqa: E501
        'init_classif_list': 'init_classif_list',  # noqa: E501
        'managers': 'managers',  # noqa: E501
        'annotators': 'annotators',  # noqa: E501
        'viewers': 'viewers',  # noqa: E501
        'instrument': 'instrument',  # noqa: E501
        'contact': 'contact',  # noqa: E501
        'highest_right': 'highest_right',  # noqa: E501
        'visible': 'visible',  # noqa: E501
        'status': 'status',  # noqa: E501
        'objcount': 'objcount',  # noqa: E501
        'pctvalidated': 'pctvalidated',  # noqa: E501
        'pctclassified': 'pctclassified',  # noqa: E501
        'classifsettings': 'classifsettings',  # noqa: E501
        'classiffieldlist': 'classiffieldlist',  # noqa: E501
        'popoverfieldlist': 'popoverfieldlist',  # noqa: E501
        'comments': 'comments',  # noqa: E501
        'description': 'description',  # noqa: E501
        'rf_models_used': 'rf_models_used',  # noqa: E501
        'cnn_network_id': 'cnn_network_id',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, license, projid, title, *args, **kwargs):  # noqa: E501
        """ProjectModel - a model defined in OpenAPI

        Args:
            license (str):
            projid (int): The project Id.
            title (str): The project title.

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
            obj_free_cols ({str: (str,)}): Object free columns.. [optional] if omitted the server will use the default value of {}  # noqa: E501
            sample_free_cols ({str: (str,)}): Sample free columns.. [optional] if omitted the server will use the default value of {}  # noqa: E501
            acquisition_free_cols ({str: (str,)}): Acquisition free columns.. [optional] if omitted the server will use the default value of {}  # noqa: E501
            process_free_cols ({str: (str,)}): Process free columns.. [optional] if omitted the server will use the default value of {}  # noqa: E501
            init_classif_list ([int]): Favorite taxa used in classification.. [optional] if omitted the server will use the default value of []  # noqa: E501
            managers ([UserModel]): Managers of this project.. [optional] if omitted the server will use the default value of []  # noqa: E501
            annotators ([UserModel]): Annotators of this project, if not manager.. [optional] if omitted the server will use the default value of []  # noqa: E501
            viewers ([UserModel]): Viewers of this project, if not manager nor annotator.. [optional] if omitted the server will use the default value of []  # noqa: E501
            instrument (str): This project's instrument. Transitory: if several of them, then coma-separated.. [optional]  # noqa: E501
            contact (dict): The contact person is a manager who serves as the contact person for other users and EcoTaxa's managers.. [optional]  # noqa: E501
            highest_right (str): The highest right for requester on this project. One of 'Manage', 'Annotate', 'View'.. [optional] if omitted the server will use the default value of ""  # noqa: E501
            visible (bool): The project visibility.. [optional]  # noqa: E501
            status (str): The project status.. [optional]  # noqa: E501
            objcount (float): The number of objects.. [optional]  # noqa: E501
            pctvalidated (float): Percentage of validated images.. [optional]  # noqa: E501
            pctclassified (float): Percentage of classified images.. [optional]  # noqa: E501
            classifsettings (str): [optional]  # noqa: E501
            classiffieldlist (str): [optional]  # noqa: E501
            popoverfieldlist (str): [optional]  # noqa: E501
            comments (str): The project comments.. [optional]  # noqa: E501
            description (str): The project description, i.e. main traits.. [optional]  # noqa: E501
            rf_models_used (str): [optional]  # noqa: E501
            cnn_network_id (str): [optional]  # noqa: E501
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

        self.license = license
        self.projid = projid
        self.title = title
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
    def __init__(self, license, projid, title, *args, **kwargs):  # noqa: E501
        """ProjectModel - a model defined in OpenAPI

        Args:
            license (str):
            projid (int): The project Id.
            title (str): The project title.

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
            obj_free_cols ({str: (str,)}): Object free columns.. [optional] if omitted the server will use the default value of {}  # noqa: E501
            sample_free_cols ({str: (str,)}): Sample free columns.. [optional] if omitted the server will use the default value of {}  # noqa: E501
            acquisition_free_cols ({str: (str,)}): Acquisition free columns.. [optional] if omitted the server will use the default value of {}  # noqa: E501
            process_free_cols ({str: (str,)}): Process free columns.. [optional] if omitted the server will use the default value of {}  # noqa: E501
            init_classif_list ([int]): Favorite taxa used in classification.. [optional] if omitted the server will use the default value of []  # noqa: E501
            managers ([UserModel]): Managers of this project.. [optional] if omitted the server will use the default value of []  # noqa: E501
            annotators ([UserModel]): Annotators of this project, if not manager.. [optional] if omitted the server will use the default value of []  # noqa: E501
            viewers ([UserModel]): Viewers of this project, if not manager nor annotator.. [optional] if omitted the server will use the default value of []  # noqa: E501
            instrument (str): This project's instrument. Transitory: if several of them, then coma-separated.. [optional]  # noqa: E501
            contact (dict): The contact person is a manager who serves as the contact person for other users and EcoTaxa's managers.. [optional]  # noqa: E501
            highest_right (str): The highest right for requester on this project. One of 'Manage', 'Annotate', 'View'.. [optional] if omitted the server will use the default value of ""  # noqa: E501
            visible (bool): The project visibility.. [optional]  # noqa: E501
            status (str): The project status.. [optional]  # noqa: E501
            objcount (float): The number of objects.. [optional]  # noqa: E501
            pctvalidated (float): Percentage of validated images.. [optional]  # noqa: E501
            pctclassified (float): Percentage of classified images.. [optional]  # noqa: E501
            classifsettings (str): [optional]  # noqa: E501
            classiffieldlist (str): [optional]  # noqa: E501
            popoverfieldlist (str): [optional]  # noqa: E501
            comments (str): The project comments.. [optional]  # noqa: E501
            description (str): The project description, i.e. main traits.. [optional]  # noqa: E501
            rf_models_used (str): [optional]  # noqa: E501
            cnn_network_id (str): [optional]  # noqa: E501
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

        self.license = license
        self.projid = projid
        self.title = title
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
