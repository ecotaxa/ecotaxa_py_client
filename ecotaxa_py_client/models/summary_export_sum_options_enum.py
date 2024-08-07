# coding: utf-8

"""
    EcoTaxa

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.37
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class SummaryExportSumOptionsEnum(str, Enum):
    """
    An enumeration.
    """

    """
    allowed enum values
    """
    NONE = 'none'
    SAMPLE = 'sample'
    ACQUISITION = 'acquisition'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SummaryExportSumOptionsEnum from a JSON string"""
        return cls(json.loads(json_str))


