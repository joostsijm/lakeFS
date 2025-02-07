# coding: utf-8

"""
    lakeFS API

    lakeFS HTTP API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: services@treeverse.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
try:
    from pydantic.v1 import BaseModel, Field, conlist
except ImportError:
    from pydantic import BaseModel, Field, conlist
from lakefs_sdk.models.range_metadata import RangeMetadata

class MetaRangeCreation(BaseModel):
    """
    MetaRangeCreation
    """
    ranges: conlist(RangeMetadata, min_items=1) = Field(...)
    __properties = ["ranges"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> MetaRangeCreation:
        """Create an instance of MetaRangeCreation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in ranges (list)
        _items = []
        if self.ranges:
            for _item in self.ranges:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ranges'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MetaRangeCreation:
        """Create an instance of MetaRangeCreation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MetaRangeCreation.parse_obj(obj)

        _obj = MetaRangeCreation.parse_obj({
            "ranges": [RangeMetadata.from_dict(_item) for _item in obj.get("ranges")] if obj.get("ranges") is not None else None
        })
        return _obj

