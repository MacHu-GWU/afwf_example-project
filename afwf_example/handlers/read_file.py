# -*- coding: utf-8 -*-

"""
[CN]

该 Script Filter 的功能是展示 file.txt 文件中的内容. 仅仅是和 ``write_file.py`` 模块
配合使用, 永远验证.
"""

import sys
import afwf
import attr

from ..paths import dir_project_home


@attr.define
class Handler(afwf.Handler):
    def main(self) -> afwf.ScriptFilter:
        sf = afwf.ScriptFilter()
        path = dir_project_home / "file.txt"
        if path.exists():
            content = path.read_text()
            item = afwf.Item(
                title=f"content of file.txt is",
                subtitle=content,
            )
        else:
            content = "file.txt does not exist!"
            item = afwf.Item(
                title=f"Write {content!r} to {path.basename}",
                arg=f"{sys.executable} main.py 'write_request_handler {content}'",
            ).set_icon(afwf.IconFileEnum.error)

        sf.items.append(item)
        return sf

    def parse_query(self, query: str):
        return {}


handler = Handler(id="read_file")
