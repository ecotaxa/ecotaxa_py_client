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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from ecotaxa_py_client.models.min_user_model import MinUserModel
from typing import Optional, Set
from typing_extensions import Self

class CollectionModel(BaseModel):
    """
    Basic and computed information about the Collection.
    """ # noqa: E501
    project_ids: Annotated[List[StrictInt], Field(min_length=1)] = Field(description="The list of composing project IDs.")
    provider_user: Optional[MinUserModel] = Field(default=None, description="Is the person who         is responsible for the content of this metadata record. Writer of the title and abstract.")
    contact_user: Optional[MinUserModel] = Field(default=None, description="Is the person who         should be contacted in cases of questions regarding the content of the dataset or any data restrictions.         This is also the person who is most likely to stay involved in the dataset the longest.")
    creator_users: Optional[List[MinUserModel]] = Field(default=None, description="All people who         are responsible for the creation of the collection. Data creators should receive credit         for their work and should therefore be included in the citation.")
    creator_organisations: Optional[List[StrictStr]] = Field(default=None, description="All         organisations who are responsible for the creation of the collection. Data creators should         receive credit for their work and should therefore be included in the citation.")
    associate_users: Optional[List[MinUserModel]] = Field(default=None, description="Other person(s)         associated with the collection.")
    associate_organisations: Optional[List[StrictStr]] = Field(default=None, description="Other         organisation(s) associated with the collection.")
    id: StrictInt = Field(description="The collection Id.")
    external_id: StrictStr = Field(description="The external Id.")
    external_id_system: StrictStr = Field(description="The external Id system.")
    title: StrictStr = Field(description="The collection title.")
    short_title: Optional[StrictStr] = Field(default=None, description="The collection short title.")
    citation: Optional[StrictStr] = Field(default=None, description="The collection citation.")
    license: Optional[StrictStr] = Field(default=None, description="The collection license.")
    abstract: Optional[StrictStr] = Field(default=None, description="The collection abstract.")
    description: Optional[StrictStr] = Field(default=None, description="The collection description.")
    __properties: ClassVar[List[str]] = ["project_ids", "provider_user", "contact_user", "creator_users", "creator_organisations", "associate_users", "associate_organisations", "id", "external_id", "external_id_system", "title", "short_title", "citation", "license", "abstract", "description"]

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
        """Create an instance of CollectionModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of provider_user
        if self.provider_user:
            _dict['provider_user'] = self.provider_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of contact_user
        if self.contact_user:
            _dict['contact_user'] = self.contact_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in creator_users (list)
        _items = []
        if self.creator_users:
            for _item in self.creator_users:
                if _item:
                    _items.append(_item.to_dict())
            _dict['creator_users'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in associate_users (list)
        _items = []
        if self.associate_users:
            for _item in self.associate_users:
                if _item:
                    _items.append(_item.to_dict())
            _dict['associate_users'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CollectionModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "project_ids": obj.get("project_ids"),
            "provider_user": MinUserModel.from_dict(obj["provider_user"]) if obj.get("provider_user") is not None else None,
            "contact_user": MinUserModel.from_dict(obj["contact_user"]) if obj.get("contact_user") is not None else None,
            "creator_users": [MinUserModel.from_dict(_item) for _item in obj["creator_users"]] if obj.get("creator_users") is not None else None,
            "creator_organisations": obj.get("creator_organisations"),
            "associate_users": [MinUserModel.from_dict(_item) for _item in obj["associate_users"]] if obj.get("associate_users") is not None else None,
            "associate_organisations": obj.get("associate_organisations"),
            "id": obj.get("id"),
            "external_id": obj.get("external_id"),
            "external_id_system": obj.get("external_id_system"),
            "title": obj.get("title"),
            "short_title": obj.get("short_title"),
            "citation": obj.get("citation"),
            "license": obj.get("license"),
            "abstract": obj.get("abstract"),
            "description": obj.get("description")
        })
        return _obj


