# -*- coding: utf-8 -*-

import json
from automation.ops import path_bin_python, dir_workflow
from afwf_example.handlers import (
    error,
    memorize_cache,
    open_file,
    open_url,
    read_file,
    set_settings,
    view_settings,
    write_file,
)
from rich import print as rprint

# verbose = True
verbose = False

# handler = error.handler
# handler = open_file.handler
# handler = open_url.handler
# handler = read_file.handler

# handler = set_settings.handler
# query = "email my@email.com"

# handler = set_settings.set_setting_value_handler
# query = "email my@email.com"

# handler = view_settings.handler
# query = ""

# handler = write_file.handler
# query = "hello"

handler = memorize_cache.handler
query = "my_key"

res = handler.run_script_command(path_bin_python, dir_workflow, query, verbose=verbose)
if res is None:
    print(f"res = {res}")
else:
    rprint(json.loads(res))
