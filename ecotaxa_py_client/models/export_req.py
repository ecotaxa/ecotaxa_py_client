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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ecotaxa_py_client.models.export_type_enum import ExportTypeEnum
from ecotaxa_py_client.models.summary_export_grouping_enum import SummaryExportGroupingEnum
from typing import Optional, Set
from typing_extensions import Self

class ExportReq(BaseModel):
    """
    Export request.
    """ # noqa: E501
    project_id: StrictInt = Field(description="The project to export.")
    exp_type: ExportTypeEnum = Field(description="The export type.")
    use_latin1: Optional[StrictBool] = Field(default=False, description="Export using latin 1 character set, AKA iso-8859-1. Default is utf-8.")
    tsv_entities: Optional[StrictStr] = Field(default='', description="For 'TSV' type, the entities to export, one letter for each of O(bject), P(rocess), A(cquisition), S(ample), C(omments).")
    only_annotations: Optional[StrictBool] = Field(default=False, description="For 'BAK' type, only save objects' last annotation data in backup.")
    split_by: Optional[StrictStr] = Field(default='', description="For 'TSV' type, inside archives, split in one directory per... 'sample', 'acquisition', 'taxon' or '' (no split).")
    coma_as_separator: Optional[StrictBool] = Field(default=False, description="For 'TSV' type, use a , instead of . for decimal separator.")
    format_dates_times: Optional[StrictBool] = Field(default=True, description="For 'TSV' type, format dates and times using - and : respectively.")
    with_images: Optional[StrictBool] = Field(default=False, description="For 'BAK' and 'DOI' types, export images as well.")
    with_internal_ids: Optional[StrictBool] = Field(default=False, description="For 'TSV' type, export internal DB IDs.")
    with_types_row: Optional[StrictBool] = Field(default=False, description="Add an EcoTaxa-compatible second line with types.")
    only_first_image: Optional[StrictBool] = Field(default=False, description="For 'DOI' type, export only first (displayed) image.")
    sum_subtotal: Optional[SummaryExportGroupingEnum] = Field(default=None, description="For 'SUM', 'ABO', 'CNC' and 'BIV' types, if computations should be combined. Per A(cquisition) or S(ample) or <Empty>(just taxa).")
    pre_mapping: Optional[Dict[str, StrictInt]] = Field(default=None, description="For 'ABO', 'CNC' and 'BIV' types types, mapping from present taxon (key) to output replacement one (value). Use a null replacement to _discard_ the present taxon.")
    formulae: Optional[Dict[str, StrictStr]] = Field(default=None, description="Transitory: For 'CNC' and 'BIV' type, how to get values from DB free columns. Python syntax, prefixes are 'sam', 'ssm' and 'obj'.Variables used in computations are 'total_water_volume', 'subsample_coef' and 'individual_volume'")
    out_to_ftp: Optional[StrictBool] = Field(default=False, description="Copy result file to FTP area. Original file is still available.")
    __properties: ClassVar[List[str]] = ["project_id", "exp_type", "use_latin1", "tsv_entities", "only_annotations", "split_by", "coma_as_separator", "format_dates_times", "with_images", "with_internal_ids", "with_types_row", "only_first_image", "sum_subtotal", "pre_mapping", "formulae", "out_to_ftp"]

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
        """Create an instance of ExportReq from a JSON string"""
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
        """Create an instance of ExportReq from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "project_id": obj.get("project_id"),
            "exp_type": obj.get("exp_type"),
            "use_latin1": obj.get("use_latin1") if obj.get("use_latin1") is not None else False,
            "tsv_entities": obj.get("tsv_entities") if obj.get("tsv_entities") is not None else '',
            "only_annotations": obj.get("only_annotations") if obj.get("only_annotations") is not None else False,
            "split_by": obj.get("split_by") if obj.get("split_by") is not None else '',
            "coma_as_separator": obj.get("coma_as_separator") if obj.get("coma_as_separator") is not None else False,
            "format_dates_times": obj.get("format_dates_times") if obj.get("format_dates_times") is not None else True,
            "with_images": obj.get("with_images") if obj.get("with_images") is not None else False,
            "with_internal_ids": obj.get("with_internal_ids") if obj.get("with_internal_ids") is not None else False,
            "with_types_row": obj.get("with_types_row") if obj.get("with_types_row") is not None else False,
            "only_first_image": obj.get("only_first_image") if obj.get("only_first_image") is not None else False,
            "sum_subtotal": obj.get("sum_subtotal"),
            "pre_mapping": obj.get("pre_mapping"),
            "formulae": obj.get("formulae"),
            "out_to_ftp": obj.get("out_to_ftp") if obj.get("out_to_ftp") is not None else False
        })
        return _obj


