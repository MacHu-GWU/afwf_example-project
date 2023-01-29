# -*- coding: utf-8 -*-

from ._version import __version__

__author__ = "Sanhe Hu"
__chore__ = "dc2ba0d33e28cbfd762ab8579bcb8483"

try:
    from .workflow import wf
except ImportError: # pragma: no cover
    pass