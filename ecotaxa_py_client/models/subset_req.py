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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from ecotaxa_py_client.models.group_definitions import GroupDefinitions
from ecotaxa_py_client.models.limit_methods import LimitMethods
from ecotaxa_py_client.models.project_filters_dict import ProjectFiltersDict
from typing import Optional, Set
from typing_extensions import Self

class SubsetReq(BaseModel):
    """
    Subset request.
    """ # noqa: E501
    filters: Optional[ProjectFiltersDict] = Field(default=None, description="The filters to apply to project.")
    dest_prj_id: StrictInt = Field(description="The destination project ID.")
    group_type: GroupDefinitions = Field(description="Define the groups in which to apply limits. C for categories, S for samples, A for acquisitions.")
    limit_type: LimitMethods = Field(description="The type of limit_value: P for %, V for constant, both per group.")
    limit_value: Union[StrictFloat, StrictInt] = Field(description="Limit value, e.g. 20% or 5 per copepoda or 5% per sample.")
    __properties: ClassVar[List[str]] = ["filters", "dest_prj_id", "group_type", "limit_type", "limit_value"]

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
        """Create an instance of SubsetReq from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of filters
        if self.filters:
            _dict['filters'] = self.filters.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubsetReq from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "filters": ProjectFiltersDict.from_dict(obj["filters"]) if obj.get("filters") is not None else None,
            "dest_prj_id": obj.get("dest_prj_id"),
            "group_type": obj.get("group_type"),
            "limit_type": obj.get("limit_type"),
            "limit_value": obj.get("limit_value")
        })
        return _obj


