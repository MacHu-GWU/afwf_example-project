# -*- coding: utf-8 -*-

import os
import pytest
from afwf_example.handlers.set_settings import handler
from rich import print as rprint

def test():
    # no query, show list of key value
    sf = handler.handler(query="")
    assert [item.title for item in sf.items] == ["email", "password"]
    # rprint(sf)

    # sort key by query
    sf = handler.handler(query="nothing")
    assert len(sf.items) == 2
    # rprint(sf)

    # sort key by query
    sf = handler.handler(query="email my@email.com")
    assert len(sf.items) == 1


if __name__ == "__main__":
    from afwf_example.tests import run_cov_test

    run_cov_test(__file__, "afwf_example.handlers.set_settings", preview=False)
