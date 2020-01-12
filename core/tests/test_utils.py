import pytest

from core.utils import generate_slug


def test_generate_slug():
    assert generate_slug('Test this creation tool', 100) == 'test-this-creation-tool-100'
