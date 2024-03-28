# coding: utf-8

"""
    EcoTaxa

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.36
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ObjectSetQueryRsp(BaseModel):
    """
    ObjectSetQueryRsp
    """ # noqa: E501
    object_ids: Optional[List[StrictInt]] = Field(default=None, description="Matching object IDs.")
    acquisition_ids: Optional[List[StrictInt]] = Field(default=None, description="Parent (acquisition) IDs.")
    sample_ids: Optional[List[StrictInt]] = Field(default=None, description="Parent (sample) IDs.")
    project_ids: Optional[List[StrictInt]] = Field(default=None, description="Project Ids.")
    details: Optional[List[List[Any]]] = Field(default=None, description="Requested fields, in request order.")
    total_ids: Optional[StrictInt] = Field(default=0, description="Total rows returned by the query, even if it was window-ed.")
    __properties: ClassVar[List[str]] = ["object_ids", "acquisition_ids", "sample_ids", "project_ids", "details", "total_ids"]

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
        """Create an instance of ObjectSetQueryRsp from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ObjectSetQueryRsp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object_ids": obj.get("object_ids"),
            "acquisition_ids": obj.get("acquisition_ids"),
            "sample_ids": obj.get("sample_ids"),
            "project_ids": obj.get("project_ids"),
            "details": obj.get("details"),
            "total_ids": obj.get("total_ids") if obj.get("total_ids") is not None else 0
        })
        return _obj

