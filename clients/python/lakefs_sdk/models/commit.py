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


from typing import Dict, List, Optional
try:
    from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conint, conlist
except ImportError:
    from pydantic import BaseModel, Field, StrictInt, StrictStr, conint, conlist

class Commit(BaseModel):
    """
    Commit
    """
    id: StrictStr = Field(...)
    parents: conlist(StrictStr) = Field(...)
    committer: StrictStr = Field(...)
    message: StrictStr = Field(...)
    creation_date: StrictInt = Field(..., description="Unix Epoch in seconds")
    meta_range_id: StrictStr = Field(...)
    metadata: Optional[Dict[str, StrictStr]] = None
    generation: Optional[StrictInt] = None
    version: Optional[conint(strict=True, le=1, ge=0)] = None
    __properties = ["id", "parents", "committer", "message", "creation_date", "meta_range_id", "metadata", "generation", "version"]

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
    def from_json(cls, json_str: str) -> Commit:
        """Create an instance of Commit from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Commit:
        """Create an instance of Commit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Commit.parse_obj(obj)

        _obj = Commit.parse_obj({
            "id": obj.get("id"),
            "parents": obj.get("parents"),
            "committer": obj.get("committer"),
            "message": obj.get("message"),
            "creation_date": obj.get("creation_date"),
            "meta_range_id": obj.get("meta_range_id"),
            "metadata": obj.get("metadata"),
            "generation": obj.get("generation"),
            "version": obj.get("version")
        })
        return _obj

