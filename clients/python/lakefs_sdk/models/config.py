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


from typing import List, Optional
try:
    from pydantic.v1 import BaseModel, conlist
except ImportError:
    from pydantic import BaseModel, conlist
from lakefs_sdk.models.storage_config import StorageConfig
from lakefs_sdk.models.version_config import VersionConfig

class Config(BaseModel):
    """
    Config
    """
    version_config: Optional[VersionConfig] = None
    storage_config: Optional[StorageConfig] = None
    storage_config_list: Optional[conlist(StorageConfig)] = None
    __properties = ["version_config", "storage_config", "storage_config_list"]

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
    def from_json(cls, json_str: str) -> Config:
        """Create an instance of Config from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of version_config
        if self.version_config:
            _dict['version_config'] = self.version_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of storage_config
        if self.storage_config:
            _dict['storage_config'] = self.storage_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in storage_config_list (list)
        _items = []
        if self.storage_config_list:
            for _item in self.storage_config_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['storage_config_list'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Config:
        """Create an instance of Config from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Config.parse_obj(obj)

        _obj = Config.parse_obj({
            "version_config": VersionConfig.from_dict(obj.get("version_config")) if obj.get("version_config") is not None else None,
            "storage_config": StorageConfig.from_dict(obj.get("storage_config")) if obj.get("storage_config") is not None else None,
            "storage_config_list": [StorageConfig.from_dict(_item) for _item in obj.get("storage_config_list")] if obj.get("storage_config_list") is not None else None
        })
        return _obj


