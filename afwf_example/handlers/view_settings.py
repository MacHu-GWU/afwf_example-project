# -*- coding: utf-8 -*-

"""
[CN]

该 Script Filter 的功能是让用户对用作 settings 的 sqlite 进行读取. 可以和 ``set_settings.py``
模块配合使用查看效果.
"""

import attrs
import afwf.api as afwf

from ..settings import path_settings_sqlite, settings, SettingsKeyEnum


@attrs.define
class Handler(afwf.Handler):
    def main(self) -> afwf.ScriptFilter:
        sf = afwf.ScriptFilter()
        for settings_key in SettingsKeyEnum:
            value = settings.get(settings_key.value)
            item = afwf.Item(
                title=f"settings.{settings_key} = {value!r}",
                subtitle=f"settings are stored at {path_settings_sqlite}",
            )
            sf.items.append(item)
        return sf

    def parse_query(self, query: str):
        return {}


handler = Handler(id="view_settings")
