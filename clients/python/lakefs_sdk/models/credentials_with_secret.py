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
    from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr
except ImportError:
    from pydantic import BaseModel, Field, StrictInt, StrictStr

class CredentialsWithSecret(BaseModel):
    """
    CredentialsWithSecret
    """
    access_key_id: StrictStr = Field(...)
    secret_access_key: StrictStr = Field(...)
    creation_date: StrictInt = Field(..., description="Unix Epoch in seconds")
    __properties = ["access_key_id", "secret_access_key", "creation_date"]

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
    def from_json(cls, json_str: str) -> CredentialsWithSecret:
        """Create an instance of CredentialsWithSecret from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CredentialsWithSecret:
        """Create an instance of CredentialsWithSecret from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CredentialsWithSecret.parse_obj(obj)

        _obj = CredentialsWithSecret.parse_obj({
            "access_key_id": obj.get("access_key_id"),
            "secret_access_key": obj.get("secret_access_key"),
            "creation_date": obj.get("creation_date")
        })
        return _obj

