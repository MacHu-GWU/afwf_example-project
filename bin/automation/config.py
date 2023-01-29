# -*- coding: utf-8 -*-

"""
Automation config management.
"""

import dataclasses
from pathlib_mate import Path


@dataclasses.dataclass
class AutomationConfig:
    dir_workflow: Path = dataclasses.field()


config = AutomationConfig(
    dir_workflow=Path(
        "/Users/sanhehu/Documents/Alfred-Preferences/Alfred.alfredpreferences/workflows/user.workflow.BE825014-E97C-4213-BEFE-E652C1C83974"
    ),
)
