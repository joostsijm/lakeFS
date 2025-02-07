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
    from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr
except ImportError:
    from pydantic import BaseModel, Field, StrictInt, StrictStr

class User(BaseModel):
    """
    User
    """
    id: StrictStr = Field(..., description="A unique identifier for the user. Cannot be edited.")
    creation_date: StrictInt = Field(..., description="Unix Epoch in seconds")
    friendly_name: Optional[StrictStr] = Field(None, description="A shorter name for the user than the id. Unlike id it does not identify the user (it might not be unique). Used in some places in the UI. ")
    email: Optional[StrictStr] = Field(None, description="The email address of the user. If API authentication is enabled, this field is mandatory and will be invited to login. If API authentication is disabled, this field will be ignored. All current APIAuthenticators require the email to be  lowercase and unique, although custom authenticators may not enforce this. ")
    __properties = ["id", "creation_date", "friendly_name", "email"]

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
    def from_json(cls, json_str: str) -> User:
        """Create an instance of User from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> User:
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return User.parse_obj(obj)

        _obj = User.parse_obj({
            "id": obj.get("id"),
            "creation_date": obj.get("creation_date"),
            "friendly_name": obj.get("friendly_name"),
            "email": obj.get("email")
        })
        return _obj

