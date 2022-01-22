import pytest
import os
from mmpower.Context import Context


default_data_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..',
            'mmpower',
            'data'
        )
    )

@pytest.fixture
def dirlist():
    return [default_data_dir]

@pytest.fixture
def ctx():
    return Context()

