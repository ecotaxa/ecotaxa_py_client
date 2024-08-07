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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ProjectFilters(BaseModel):
    """
    How to reduce project data.
    """ # noqa: E501
    taxo: Optional[StrictStr] = Field(default=None, description="Coma-separated list of numeric taxonomy/category ids. Only include objects classified with one of them.")
    taxochild: Optional[StrictStr] = Field(default=None, description="If 'Y' and taxo is set, also include children of each member of 'taxo' list in taxonomy tree.")
    statusfilter: Optional[Annotated[str, Field(strict=True, max_length=3)]] = Field(default=None, description="Include objects with given status:             'NV': Not validated              'PV': Predicted or Validated              'PVD': Predicted or Validated or Dubious             'NVM': Validated, but not by me              'VM': Validated by me              'U': Not classified             other: direct equality comparison with DB value          ")
    map_n: Optional[StrictStr] = Field(default=None, description="If all 4 are set (MapN, MapW, MapE, MapS), include objects inside the defined bounding rectangle.", alias="MapN")
    map_w: Optional[StrictStr] = Field(default=None, description="If all 4 are set (MapN, MapW, MapE, MapS), include objects inside the defined bounding rectangle.", alias="MapW")
    map_e: Optional[StrictStr] = Field(default=None, description="If all 4 are set (MapN, MapW, MapE, MapS), include objects inside the defined bounding rectangle.", alias="MapE")
    map_s: Optional[StrictStr] = Field(default=None, description="If all 4 are set (MapN, MapW, MapE, MapS), include objects inside the defined bounding rectangle.", alias="MapS")
    depthmin: Optional[StrictStr] = Field(default=None, description="Positive values. If both are set (depthmin, depthmax), include objects for which both depths (min and max) are inside the range.")
    depthmax: Optional[StrictStr] = Field(default=None, description="Positive values. If both are set (depthmin, depthmax), include objects for which both depths (min and max) are inside the range.")
    samples: Optional[StrictStr] = Field(default=None, description="Coma-separated list of sample IDs, include only objects for these samples.")
    instrum: Optional[StrictStr] = Field(default=None, description="Instrument name, include objects for which sampling was done using this instrument.")
    daytime: Optional[StrictStr] = Field(default=None, description="Coma-separated list of sun position values: D for Day, U for Dusk, N for Night, A for Dawn (Aube in French).")
    month: Optional[StrictStr] = Field(default=None, description="Coma-separated list of month numbers, 1=Jan and so on.")
    fromdate: Optional[StrictStr] = Field(default=None, description="Format is 'YYYY-MM-DD', include objects collected after this date.")
    todate: Optional[StrictStr] = Field(default=None, description="Format is 'YYYY-MM-DD', include objects collected before this date.")
    fromtime: Optional[StrictStr] = Field(default=None, description="Format is 'HH24:MM:SS', include objects collected after this time of day.")
    totime: Optional[StrictStr] = Field(default=None, description="Format is 'HH24:MM:SS', include objects collected before this time of day.")
    inverttime: Optional[StrictStr] = Field(default=None, description="If '1', include objects outside fromtime and totime range.")
    validfromdate: Optional[StrictStr] = Field(default=None, description="Format is 'YYYY-MM-DD HH24:MI', include objects validated/set to dubious after this date+time.")
    validtodate: Optional[StrictStr] = Field(default=None, description="Format is 'YYYY-MM-DD HH24:MI', include objects validated/set to dubious before this date+time.")
    freenum: Optional[StrictStr] = Field(default=None, description="Numerical DB column number in Object as basis for the 2 following criteria (freenumst, freenumend).")
    freenumst: Optional[StrictStr] = Field(default=None, description="Start of included range for the column defined by freenum, in which objects are included.")
    freenumend: Optional[StrictStr] = Field(default=None, description="End of included range for the column defined by freenum, in which objects are included.")
    freetxt: Optional[StrictStr] = Field(default=None, description=" Textual DB column number as basis for following criteria (freetxtval)             If starts with 's' then it's a text column in Sample             If starts with 'a' then it's a text column in Acquisition              If starts with 'p' then it's a text column in Process              If starts with 'o' then it's a text column in Object .         ")
    freetxtval: Optional[StrictStr] = Field(default=None, description="Text to match in the column defined by freetxt, for an object to be include.")
    filt_annot: Optional[StrictStr] = Field(default=None, description="Coma-separated list of annotators, i.e. persons who validated the classification at any point in time.")
    filt_last_annot: Optional[StrictStr] = Field(default=None, description="Coma-separated list of annotators, i.e. persons who validated the classification in last.")
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
        """Create an instance of ProjectFilters from a JSON string"""
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
        """Create an instance of ProjectFilters from a dict"""
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


