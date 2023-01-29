# -*- coding: utf-8 -*-

import afwf
import attr
from pathlib_mate import Path


@attr.define
class Handler(afwf.Handler):
    def low_level_api(self) -> afwf.ScriptFilter:
        sf = afwf.ScriptFilter()
        dir_here = Path.dir_here(__file__)
        for p in dir_here.iterdir():
            if p.ext.lower() == ".py":
                item = afwf.Item(
                    title=p.basename,
                    subtitle=f"Open {p.abspath}",
                    autocomplete=p.basename,
                    arg=p.abspath,
                )
                item.open_file(path=p.abspath)
                sf.items.append(item)
        return sf

    def handler(self, query: str) -> afwf.ScriptFilter:
        return self.low_level_api()


handler = Handler(id="open_file")
