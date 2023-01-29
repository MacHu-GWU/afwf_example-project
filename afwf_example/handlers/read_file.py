# -*- coding: utf-8 -*-

import sys
import afwf
import attr

from ..paths import dir_project_home


@attr.define
class Handler(afwf.Handler):
    def low_level_api(self) -> afwf.ScriptFilter:
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

    def handler(self, query: str) -> afwf.ScriptFilter:
        return self.low_level_api()


handler = Handler(id="read_file")
