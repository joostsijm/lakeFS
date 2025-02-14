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



try:
    from pydantic.v1 import BaseModel, Field, StrictStr
except ImportError:
    from pydantic import BaseModel, Field, StrictStr

class FindMergeBaseResult(BaseModel):
    """
    FindMergeBaseResult
    """
    source_commit_id: StrictStr = Field(..., description="The commit ID of the merge source")
    destination_commit_id: StrictStr = Field(..., description="The commit ID of the merge destination")
    base_commit_id: StrictStr = Field(..., description="The commit ID of the merge base")
    __properties = ["source_commit_id", "destination_commit_id", "base_commit_id"]

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
    def from_json(cls, json_str: str) -> FindMergeBaseResult:
        """Create an instance of FindMergeBaseResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FindMergeBaseResult:
        """Create an instance of FindMergeBaseResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FindMergeBaseResult.parse_obj(obj)

        _obj = FindMergeBaseResult.parse_obj({
            "source_commit_id": obj.get("source_commit_id"),
            "destination_commit_id": obj.get("destination_commit_id"),
            "base_commit_id": obj.get("base_commit_id")
        })
        return _obj

