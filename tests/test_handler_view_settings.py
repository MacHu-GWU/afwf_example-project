# -*- coding: utf-8 -*-

from afwf_example.handlers.set_settings import handler
from rich import print as rprint


def test_parse_query():
    assert handler.parse_query("") == dict(key=None, value=None)
    assert handler.parse_query("abc") == dict(key="abc", value=None)
    assert handler.parse_query("email alice@example.com") == dict(
        key="email",
        value="alice@example.com",
    )


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
