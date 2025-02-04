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
from lakefs_sdk.models.staging_location import StagingLocation
from typing import Optional, Set
from typing_extensions import Self

class StagingMetadata(BaseModel):
    """
    information about uploaded object
    """ # noqa: E501
    staging: StagingLocation
    checksum: StrictStr = Field(description="unique identifier of object content on backing store (typically ETag)")
    size_bytes: StrictInt
    user_metadata: Optional[Dict[str, StrictStr]] = None
    content_type: Optional[StrictStr] = Field(default=None, description="Object media type")
    mtime: Optional[StrictInt] = Field(default=None, description="Unix Epoch in seconds.  May be ignored by server.")
    force: Optional[StrictBool] = False
    __properties: ClassVar[List[str]] = ["staging", "checksum", "size_bytes", "user_metadata", "content_type", "mtime", "force"]

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
        """Create an instance of StagingMetadata from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of staging
        if self.staging:
            _dict['staging'] = self.staging.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StagingMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "staging": StagingLocation.from_dict(obj["staging"]) if obj.get("staging") is not None else None,
            "checksum": obj.get("checksum"),
            "size_bytes": obj.get("size_bytes"),
            "user_metadata": obj.get("user_metadata"),
            "content_type": obj.get("content_type"),
            "mtime": obj.get("mtime"),
            "force": obj.get("force") if obj.get("force") is not None else False
        })
        return _obj


