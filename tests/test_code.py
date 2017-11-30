"""
Unit tests for our python code
"""

from custom_library import my_module 
import pytest

def test_add_one():
    """Test that adding one works correctly"""
    m = my_module.Adder(1)
    assert m.add_one() == 2

def test_square_root_letter():
    """Test that adding two works correctly"""
    m = my_module.Adder(1)
    assert m.add_two() == 3
