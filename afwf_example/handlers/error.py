# -*- coding: utf-8 -*-

"""
This handler will always raise an error. It is used for testing purpose.
"""

import typing as T
import attrs
import afwf.api as afwf


@attrs.define
class Handler(afwf.Handler):
    def main(self) -> afwf.ScriptFilter:
        afwf.log_debug_info("before raising the error")
        raise Exception("raise this error intentionally")

    def parse_query(self, query: str) -> T.Dict[str, T.Any]:
        return {}


handler = Handler(id="error")
