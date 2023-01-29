# -*- coding: utf-8 -*-

"""
Automation config management.
"""

import dataclasses


@dataclasses.dataclass
class AutomationConfig:
    python_version: str = dataclasses.field()
    package_name: str = dataclasses.field()


config = AutomationConfig(
    python_version="3.8",
    package_name="aws_idp_doc_store",
)
