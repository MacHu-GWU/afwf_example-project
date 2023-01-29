# -*- coding: utf-8 -*-

import afwf

from .handlers import (
    open_url,
    open_file,
    write_file,
    read_file,
    error,
)

wf = afwf.Workflow()
wf.register(open_url.handler)
wf.register(open_file.handler)
wf.register(write_file.write_request_handler)
wf.register(write_file.handler)
wf.register(read_file.handler)
wf.register(error.handler)
