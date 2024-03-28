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

class ProjectTaxoStatsModel(BaseModel):
    """
    ProjectTaxoStatsModel
    """ # noqa: E501
    projid: StrictInt = Field(description="The project id.")
    used_taxa: Optional[List[StrictInt]] = Field(default=None, description="The taxa/category ids used inside the project. An id of -1 means some unclassified objects.")
    nb_unclassified: StrictInt = Field(description="The number of unclassified objects inside the project.")
    nb_validated: StrictInt = Field(description="The number of validated objects inside the project.")
    nb_dubious: StrictInt = Field(description="The number of dubious objects inside the project.")
    nb_predicted: StrictInt = Field(description="The number of predicted objects inside the project.")
    __properties: ClassVar[List[str]] = ["projid", "used_taxa", "nb_unclassified", "nb_validated", "nb_dubious", "nb_predicted"]

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
        """Create an instance of ProjectTaxoStatsModel from a JSON string"""
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
        """Create an instance of ProjectTaxoStatsModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "projid": obj.get("projid"),
            "used_taxa": obj.get("used_taxa"),
            "nb_unclassified": obj.get("nb_unclassified"),
            "nb_validated": obj.get("nb_validated"),
            "nb_dubious": obj.get("nb_dubious"),
            "nb_predicted": obj.get("nb_predicted")
        })
        return _obj

