# -*- coding: utf-8 -*-

import os
import pytest
import afwf_example


def test_import():
    _ = afwf_example.wf


if __name__ == "__main__":
    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
