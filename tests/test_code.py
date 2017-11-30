"""
Unit tests for our python code
"""

from custom_library import my_module 
import pytest

@pytest.fixture(scope='function')
def adder_instance():
    m = my_module.Adder(1)
    return m

def test_add_one(adder_instance):
    """Test that adding one works correctly"""
    assert adder_instance.add_one() == 2

def test_square_root_letter(adder_instance):
    """Test that adding two works correctly"""
    assert adder_instance.add_two() == 3
