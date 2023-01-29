# -*- coding: utf-8 -*-

import afwf
import attr

@attr.define
class Handler(afwf.Handler):
    def low_level_api(self) -> afwf.ScriptFilter:
        raise Exception("raise this error intentionally")

    def handler(self, query: str) -> afwf.ScriptFilter:
        return self.low_level_api()


handler = Handler(id="error")
