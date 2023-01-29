# -*- coding: utf-8 -*-

import afwf

from .handlers import open_url

wf = afwf.Workflow()
wf.register(open_url.handler)
