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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ImportReq(BaseModel):
    """
    Import request, from UI choices.
    """ # noqa: E501
    source_path: StrictStr = Field(description="Source path on server, to zip or plain directory.     The path can be returned by a file upload (absolute),     otherwise it's relative to shared file area root.")
    taxo_mappings: Optional[Dict[str, StrictStr]] = Field(default=None, description="Optional taxonomy mapping, the key specifies the taxonomy ID found in file and the value specifies the final taxonomy ID to write.")
    skip_loaded_files: Optional[StrictBool] = Field(default=False, description="If true skip loaded files, else don't.")
    skip_existing_objects: Optional[StrictBool] = Field(default=False, description="If true skip existing objects, else don't.")
    update_mode: Optional[StrictStr] = Field(default='', description="Update data ('Yes'), including classification ('Cla').")
    __properties: ClassVar[List[str]] = ["source_path", "taxo_mappings", "skip_loaded_files", "skip_existing_objects", "update_mode"]

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
        """Create an instance of ImportReq from a JSON string"""
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
        """Create an instance of ImportReq from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "source_path": obj.get("source_path"),
            "taxo_mappings": obj.get("taxo_mappings"),
            "skip_loaded_files": obj.get("skip_loaded_files") if obj.get("skip_loaded_files") is not None else False,
            "skip_existing_objects": obj.get("skip_existing_objects") if obj.get("skip_existing_objects") is not None else False,
            "update_mode": obj.get("update_mode") if obj.get("update_mode") is not None else ''
        })
        return _obj


