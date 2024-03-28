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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class HistoricalLastClassif(BaseModel):
    """
    HistoricalLastClassif
    """ # noqa: E501
    objid: Optional[StrictInt] = Field(default=None, description="The object Id.")
    classif_id: Optional[StrictInt] = Field(default=None, description="The classification Id.")
    histo_classif_date: Optional[datetime] = Field(default=None, description="The classification date.")
    histo_classif_type: Optional[StrictStr] = Field(default=None, description="The type of classification. Could be **A** for Automatic or **M** for Manual.")
    histo_classif_id: Optional[StrictInt] = Field(default=None, description="The classification Id.")
    histo_classif_qual: Optional[StrictStr] = Field(default=None, description="The classification qualification. Could be **P** for predicted, **V** for validated or **D** for Dubious.")
    histo_classif_who: Optional[StrictInt] = Field(default=None, description="The user who manualy classify this object.")
    __properties: ClassVar[List[str]] = ["objid", "classif_id", "histo_classif_date", "histo_classif_type", "histo_classif_id", "histo_classif_qual", "histo_classif_who"]

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
        """Create an instance of HistoricalLastClassif from a JSON string"""
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
        """Create an instance of HistoricalLastClassif from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "objid": obj.get("objid"),
            "classif_id": obj.get("classif_id"),
            "histo_classif_date": obj.get("histo_classif_date"),
            "histo_classif_type": obj.get("histo_classif_type"),
            "histo_classif_id": obj.get("histo_classif_id"),
            "histo_classif_qual": obj.get("histo_classif_qual"),
            "histo_classif_who": obj.get("histo_classif_who")
        })
        return _obj

