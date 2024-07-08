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


class SummaryExportGroupingEnum(str, Enum):
    """
    It's implied that we minimally group/aggregate by category AKA classification AKA taxon
    """

    """
    allowed enum values
    """
    EMPTY = ''
    S = 'S'
    A = 'A'
    P = 'P'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SummaryExportGroupingEnum from a JSON string"""
        return cls(json.loads(json_str))


