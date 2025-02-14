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


from typing import Optional
try:
    from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr
except ImportError:
    from pydantic import BaseModel, Field, StrictBool, StrictStr

class BranchCreation(BaseModel):
    """
    BranchCreation
    """
    name: StrictStr = Field(...)
    source: StrictStr = Field(...)
    force: Optional[StrictBool] = False
    hidden: Optional[StrictBool] = Field(False, description="When set, branch will not show up when listing branches by default. *EXPERIMENTAL*")
    __properties = ["name", "source", "force", "hidden"]

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
    def from_json(cls, json_str: str) -> BranchCreation:
        """Create an instance of BranchCreation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BranchCreation:
        """Create an instance of BranchCreation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BranchCreation.parse_obj(obj)

        _obj = BranchCreation.parse_obj({
            "name": obj.get("name"),
            "source": obj.get("source"),
            "force": obj.get("force") if obj.get("force") is not None else False,
            "hidden": obj.get("hidden") if obj.get("hidden") is not None else False
        })
        return _obj

