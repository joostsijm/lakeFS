# coding: utf-8

"""
    lakeFS API

    lakeFS HTTP API

    The version of the OpenAPI document: 1.0.0
    Contact: services@treeverse.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

try:
    from pydantic.v1 import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
except ImportError:
    from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from lakefs_sdk.models.commit_overrides import CommitOverrides
from typing import Optional, Set
from typing_extensions import Self

class RevertCreation(BaseModel):
    """
    RevertCreation
    """ # noqa: E501
    ref: StrictStr = Field(description="the commit to revert, given by a ref")
    commit_overrides: Optional[CommitOverrides] = None
    parent_number: StrictInt = Field(description="when reverting a merge commit, the parent number (starting from 1) relative to which to perform the revert.")
    force: Optional[StrictBool] = False
    allow_empty: Optional[StrictBool] = Field(default=False, description="allow empty commit (revert without changes)")
    __properties: ClassVar[List[str]] = ["ref", "commit_overrides", "parent_number", "force", "allow_empty"]

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
        """Create an instance of RevertCreation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of commit_overrides
        if self.commit_overrides:
            _dict['commit_overrides'] = self.commit_overrides.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RevertCreation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ref": obj.get("ref"),
            "commit_overrides": CommitOverrides.from_dict(obj["commit_overrides"]) if obj.get("commit_overrides") is not None else None,
            "parent_number": obj.get("parent_number"),
            "force": obj.get("force") if obj.get("force") is not None else False,
            "allow_empty": obj.get("allow_empty") if obj.get("allow_empty") is not None else False
        })
        return _obj


