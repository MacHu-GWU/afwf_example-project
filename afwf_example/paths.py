# -*- coding: utf-8 -*-

from pathlib_mate import Path

dir_python_lib = Path.dir_here(__file__)
dir_project_root = dir_python_lib.parent

PACKAGE_NAME = dir_python_lib.basename

dir_home = Path.home()
dir_project_home = dir_home / ".alfred-afwf" / PACKAGE_NAME
dir_project_home.mkdir_if_not_exists()

dir_cache = dir_project_home / ".cache"
path_config_json = dir_project_home / "config.json"
