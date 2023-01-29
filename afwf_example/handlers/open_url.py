# -*- coding: utf-8 -*-

import afwf
import attr


@attr.define
class Handler(afwf.Handler):
    def low_level_api(self) -> afwf.ScriptFilter:
        sf = afwf.ScriptFilter()
        for title, url in [
            ("Alfred App", "https://www.alfredapp.com/"),
            ("Python", "https://www.python.org/"),
            ("GitHub", "https://github.com/"),
        ]:
            item = afwf.Item(
                title=title,
                subtitle=url,
                autocomplete=title,
                arg=url,
            )
            item.open_url(url=url)
            sf.items.append(item)
        return sf

    def handler(self, query: str) -> afwf.ScriptFilter:
        return self.low_level_api()


handler = Handler(id="open_url")
