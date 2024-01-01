# -*- coding: utf-8 -*-

"""
[CN]

该 Script Filter 的功能是展示 file.txt 文件中的内容. 仅仅是和 ``write_file.py`` 模块
配合使用, 永远验证.
"""

import attrs
import afwf.api as afwf

from ..paths import dir_project_home

path_file = dir_project_home / "file.txt"
path_file.parent.mkdir(parents=True, exist_ok=True)
if path_file.exists() is False:
    path_file.write_text("hello world")


@attrs.define
class Handler(afwf.Handler):
    def main(self) -> afwf.ScriptFilter:
        sf = afwf.ScriptFilter()
        if path_file.exists():
            content = path_file.read_text()
            item = afwf.Item(
                title=f"content of {path_file} is",
                subtitle=content,
            )
        else:
            item = afwf.Item(
                title=f"{path_file} does not exist!",
            )
            item.set_icon(afwf.IconFileEnum.error)

        sf.items.append(item)
        return sf

    def parse_query(self, query: str):
        return {}


handler = Handler(id="read_file")
