# coding: utf-8

"""
    EcoTaxa

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.37
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from ecotaxa_py_client.models.license_enum import LicenseEnum
from ecotaxa_py_client.models.min_user_model import MinUserModel
from typing import Optional, Set
from typing_extensions import Self

class ProjectModel(BaseModel):
    """
    Basic and computed information about the Project.
    """ # noqa: E501
    obj_free_cols: Optional[Dict[str, StrictStr]] = Field(default=None, description="Object free columns.")
    sample_free_cols: Optional[Dict[str, StrictStr]] = Field(default=None, description="Sample free columns.")
    acquisition_free_cols: Optional[Dict[str, StrictStr]] = Field(default=None, description="Acquisition free columns.")
    process_free_cols: Optional[Dict[str, StrictStr]] = Field(default=None, description="Process free columns.")
    bodc_variables: Dict[str, str] = Field(default=None, description="BODC quantities from columns. Only the 3 keys listed in example are valid.")
    init_classif_list: Optional[List[StrictInt]] = Field(default=None, description="Favorite taxa used in classification.")
    managers: Optional[List[MinUserModel]] = Field(default=None, description="Managers of this project.")
    annotators: Optional[List[MinUserModel]] = Field(default=None, description="Annotators of this project, if not manager.")
    viewers: Optional[List[MinUserModel]] = Field(default=None, description="Viewers of this project, if not manager nor annotator.")
    instrument: Optional[StrictStr] = Field(default=None, description="This project's instrument code.")
    instrument_url: Optional[StrictStr] = Field(default=None, description="This project's instrument BODC definition.")
    contact: Optional[MinUserModel] = Field(default=None, description="The contact person is a manager who serves as the contact person for other users and EcoTaxa's managers.")
    highest_right: Optional[StrictStr] = Field(default='', description="The highest right for requester on this project. One of 'Manage', 'Annotate', 'View'.")
    license: Optional[LicenseEnum] = Field(default=None, description="Data licence.")
    projid: StrictInt = Field(description="The project Id.")
    title: StrictStr = Field(description="The project title.")
    visible: Optional[StrictBool] = Field(default=None, description="The project visibility.")
    status: Optional[StrictStr] = Field(default=None, description="The project status.")
    objcount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The number of objects.")
    pctvalidated: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Percentage of validated images.")
    pctclassified: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Percentage of classified images.")
    classifsettings: Optional[StrictStr] = None
    classiffieldlist: Optional[StrictStr] = None
    popoverfieldlist: Optional[StrictStr] = None
    comments: Optional[StrictStr] = Field(default=None, description="The project comments.")
    description: Optional[StrictStr] = Field(default=None, description="The project description, i.e. main traits.")
    rf_models_used: Optional[StrictStr] = None
    cnn_network_id: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["obj_free_cols", "sample_free_cols", "acquisition_free_cols", "process_free_cols", "bodc_variables", "init_classif_list", "managers", "annotators", "viewers", "instrument", "instrument_url", "contact", "highest_right", "license", "projid", "title", "visible", "status", "objcount", "pctvalidated", "pctclassified", "classifsettings", "classiffieldlist", "popoverfieldlist", "comments", "description", "rf_models_used", "cnn_network_id"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ProjectModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in managers (list)
        _items = []
        if self.managers:
            for _item in self.managers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['managers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in annotators (list)
        _items = []
        if self.annotators:
            for _item in self.annotators:
                if _item:
                    _items.append(_item.to_dict())
            _dict['annotators'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in viewers (list)
        _items = []
        if self.viewers:
            for _item in self.viewers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['viewers'] = _items
        # override the default output from pydantic by calling `to_dict()` of contact
        if self.contact:
            _dict['contact'] = self.contact.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProjectModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "obj_free_cols": obj.get("obj_free_cols"),
            "sample_free_cols": obj.get("sample_free_cols"),
            "acquisition_free_cols": obj.get("acquisition_free_cols"),
            "process_free_cols": obj.get("process_free_cols"),
            "bodc_variables": obj.get("bodc_variables"),
            "init_classif_list": obj.get("init_classif_list"),
            "managers": [MinUserModel.from_dict(_item) for _item in obj["managers"]] if obj.get("managers") is not None else None,
            "annotators": [MinUserModel.from_dict(_item) for _item in obj["annotators"]] if obj.get("annotators") is not None else None,
            "viewers": [MinUserModel.from_dict(_item) for _item in obj["viewers"]] if obj.get("viewers") is not None else None,
            "instrument": obj.get("instrument"),
            "instrument_url": obj.get("instrument_url"),
            "contact": MinUserModel.from_dict(obj["contact"]) if obj.get("contact") is not None else None,
            "highest_right": obj.get("highest_right") if obj.get("highest_right") is not None else '',
            "license": obj.get("license"),
            "projid": obj.get("projid"),
            "title": obj.get("title"),
            "visible": obj.get("visible"),
            "status": obj.get("status"),
            "objcount": obj.get("objcount"),
            "pctvalidated": obj.get("pctvalidated"),
            "pctclassified": obj.get("pctclassified"),
            "classifsettings": obj.get("classifsettings"),
            "classiffieldlist": obj.get("classiffieldlist"),
            "popoverfieldlist": obj.get("popoverfieldlist"),
            "comments": obj.get("comments"),
            "description": obj.get("description"),
            "rf_models_used": obj.get("rf_models_used"),
            "cnn_network_id": obj.get("cnn_network_id")
        })
        return _obj


