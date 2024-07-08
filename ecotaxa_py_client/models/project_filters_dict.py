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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ProjectFiltersDict(BaseModel):
    """
    ProjectFiltersDict
    """ # noqa: E501
    taxo: Optional[StrictStr] = None
    taxochild: Optional[StrictStr] = None
    statusfilter: Optional[StrictStr] = None
    map_n: Optional[StrictStr] = Field(default=None, alias="MapN")
    map_w: Optional[StrictStr] = Field(default=None, alias="MapW")
    map_e: Optional[StrictStr] = Field(default=None, alias="MapE")
    map_s: Optional[StrictStr] = Field(default=None, alias="MapS")
    depthmin: Optional[StrictStr] = None
    depthmax: Optional[StrictStr] = None
    samples: Optional[StrictStr] = None
    instrum: Optional[StrictStr] = None
    daytime: Optional[StrictStr] = None
    month: Optional[StrictStr] = None
    fromdate: Optional[StrictStr] = None
    todate: Optional[StrictStr] = None
    fromtime: Optional[StrictStr] = None
    totime: Optional[StrictStr] = None
    inverttime: Optional[StrictStr] = None
    validfromdate: Optional[StrictStr] = None
    validtodate: Optional[StrictStr] = None
    freenum: Optional[StrictStr] = None
    freenumst: Optional[StrictStr] = None
    freenumend: Optional[StrictStr] = None
    freetxt: Optional[StrictStr] = None
    freetxtval: Optional[StrictStr] = None
    filt_annot: Optional[StrictStr] = None
    filt_last_annot: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["taxo", "taxochild", "statusfilter", "MapN", "MapW", "MapE", "MapS", "depthmin", "depthmax", "samples", "instrum", "daytime", "month", "fromdate", "todate", "fromtime", "totime", "inverttime", "validfromdate", "validtodate", "freenum", "freenumst", "freenumend", "freetxt", "freetxtval", "filt_annot", "filt_last_annot"]

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
        """Create an instance of ProjectFiltersDict from a JSON string"""
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
        """Create an instance of ProjectFiltersDict from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "taxo": obj.get("taxo"),
            "taxochild": obj.get("taxochild"),
            "statusfilter": obj.get("statusfilter"),
            "MapN": obj.get("MapN"),
            "MapW": obj.get("MapW"),
            "MapE": obj.get("MapE"),
            "MapS": obj.get("MapS"),
            "depthmin": obj.get("depthmin"),
            "depthmax": obj.get("depthmax"),
            "samples": obj.get("samples"),
            "instrum": obj.get("instrum"),
            "daytime": obj.get("daytime"),
            "month": obj.get("month"),
            "fromdate": obj.get("fromdate"),
            "todate": obj.get("todate"),
            "fromtime": obj.get("fromtime"),
            "totime": obj.get("totime"),
            "inverttime": obj.get("inverttime"),
            "validfromdate": obj.get("validfromdate"),
            "validtodate": obj.get("validtodate"),
            "freenum": obj.get("freenum"),
            "freenumst": obj.get("freenumst"),
            "freenumend": obj.get("freenumend"),
            "freetxt": obj.get("freetxt"),
            "freetxtval": obj.get("freetxtval"),
            "filt_annot": obj.get("filt_annot"),
            "filt_last_annot": obj.get("filt_last_annot")
        })
        return _obj


