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


from typing import List, Optional
try:
    from pydantic.v1 import BaseModel, Field, StrictStr, conlist, validator
except ImportError:
    from pydantic import BaseModel, Field, StrictStr, conlist, validator

class LoginConfig(BaseModel):
    """
    LoginConfig
    """
    rbac: Optional[StrictStr] = Field(None, alias="RBAC", description="RBAC will remain enabled on GUI if \"external\".  That only works with an external auth service. ")
    username_ui_placeholder: Optional[StrictStr] = Field(None, description="Placeholder text to display in the username field of the login form. ")
    password_ui_placeholder: Optional[StrictStr] = Field(None, description="Placeholder text to display in the password field of the login form. ")
    login_url: StrictStr = Field(..., description="primary URL to use for login.")
    login_failed_message: Optional[StrictStr] = Field(None, description="message to display to users who fail to login; a full sentence that is rendered in HTML and may contain a link to a secondary login method ")
    fallback_login_url: Optional[StrictStr] = Field(None, description="secondary URL to offer users to use for login.")
    fallback_login_label: Optional[StrictStr] = Field(None, description="label to place on fallback_login_url.")
    login_cookie_names: conlist(StrictStr) = Field(..., description="cookie names used to store JWT")
    logout_url: StrictStr = Field(..., description="URL to use for logging out.")
    __properties = ["RBAC", "username_ui_placeholder", "password_ui_placeholder", "login_url", "login_failed_message", "fallback_login_url", "fallback_login_label", "login_cookie_names", "logout_url"]

    @validator('rbac')
    def rbac_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('none', 'simplified', 'external'):
            raise ValueError("must be one of enum values ('none', 'simplified', 'external')")
        return value

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
    def from_json(cls, json_str: str) -> LoginConfig:
        """Create an instance of LoginConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoginConfig:
        """Create an instance of LoginConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoginConfig.parse_obj(obj)

        _obj = LoginConfig.parse_obj({
            "rbac": obj.get("RBAC"),
            "username_ui_placeholder": obj.get("username_ui_placeholder"),
            "password_ui_placeholder": obj.get("password_ui_placeholder"),
            "login_url": obj.get("login_url"),
            "login_failed_message": obj.get("login_failed_message"),
            "fallback_login_url": obj.get("fallback_login_url"),
            "fallback_login_label": obj.get("fallback_login_label"),
            "login_cookie_names": obj.get("login_cookie_names"),
            "logout_url": obj.get("logout_url")
        })
        return _obj

