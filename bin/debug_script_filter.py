# -*- coding: utf-8 -*-

from automation.alfred import refresh_code, debug

bin_python = "/Users/sanhehu/.pyenv/versions/3.8.11/bin/python"
handler_id = "set_settings"
query = "email my@email.com"

refresh_code()
debug(bin_python, handler_id, query)
