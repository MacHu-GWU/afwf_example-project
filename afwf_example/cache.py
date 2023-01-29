# -*- coding: utf-8 -*-

from diskcache import Cache

from .paths import dir_cache

cache = Cache(dir_cache.abspath)
