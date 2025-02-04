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
    from pydantic.v1 import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
except ImportError:
    from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ObjectStats(BaseModel):
    """
    ObjectStats
    """ # noqa: E501
    path: StrictStr
    path_type: StrictStr
    physical_address: StrictStr = Field(description="The location of the object on the underlying object store. Formatted as a native URI with the object store type as scheme (\"s3://...\", \"gs://...\", etc.) Or, in the case of presign=true, will be an HTTP URL to be consumed via regular HTTP GET ")
    physical_address_expiry: Optional[StrictInt] = Field(default=None, description="If present and nonzero, physical_address is a pre-signed URL and will expire at this Unix Epoch time.  This will be shorter than the pre-signed URL lifetime if an authentication token is about to expire.  This field is *optional*. ")
    checksum: StrictStr
    size_bytes: Optional[StrictInt] = Field(default=None, description="The number of bytes in the object.  lakeFS always populates this field when returning ObjectStats.  This field is optional _for the client_ to supply, for instance on upload. ")
    mtime: StrictInt = Field(description="Unix Epoch in seconds")
    metadata: Optional[Dict[str, StrictStr]] = None
    content_type: Optional[StrictStr] = Field(default=None, description="Object media type")
    __properties: ClassVar[List[str]] = ["path", "path_type", "physical_address", "physical_address_expiry", "checksum", "size_bytes", "mtime", "metadata", "content_type"]

    @field_validator('path_type')
    def path_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['common_prefix', 'object']):
            raise ValueError("must be one of enum values ('common_prefix', 'object')")
        return value

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
        """Create an instance of ObjectStats from a JSON string"""
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
        """Create an instance of ObjectStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "path": obj.get("path"),
            "path_type": obj.get("path_type"),
            "physical_address": obj.get("physical_address"),
            "physical_address_expiry": obj.get("physical_address_expiry"),
            "checksum": obj.get("checksum"),
            "size_bytes": obj.get("size_bytes"),
            "mtime": obj.get("mtime"),
            "metadata": obj.get("metadata"),
            "content_type": obj.get("content_type")
        })
        return _obj


