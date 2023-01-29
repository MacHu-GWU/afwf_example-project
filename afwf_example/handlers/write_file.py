# -*- coding: utf-8 -*-

import sys
import afwf
import attr

from ..paths import dir_project_home


@attr.define
class WriteRequestHandler(afwf.Handler):
    def low_level_api(self, content: str) -> afwf.ScriptFilter:
        sf = afwf.ScriptFilter()
        path = dir_project_home / "file.txt"
        path.write_text(content)
        return sf

    def handler(self, query: str) -> afwf.ScriptFilter:
        return self.low_level_api(content=query)


write_request_handler = WriteRequestHandler(id="write_request_handler")


@attr.define
class Handler(afwf.Handler):
    def low_level_api(self, content: str) -> afwf.ScriptFilter:
        sf = afwf.ScriptFilter()
        path = dir_project_home / "file.txt"
        cmd = f"{sys.executable} main.py 'write_request_handler {content}'"
        item = afwf.Item(
            title=f"Write {content!r} to {path.basename}",
            arg=f"{sys.executable} main.py 'write_request_handler {content}'",
        )
        item.run_script(cmd)
        item.send_notification(
            title=f"Write {content!r} to {path.basename}",
            subtitle="success",
        )
        sf.items.append(item)
        return sf

    def handler(self, query: str) -> afwf.ScriptFilter:
        return self.low_level_api(content=query)


handler = Handler(id="write_file")
