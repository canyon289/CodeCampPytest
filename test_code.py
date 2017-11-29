"""
Unit tests for our python code
"""

import my_module 
import pytest

def test_square_root_4():
    """Test that square root four works"""
    assert my_module.square_root(4) == 2

def test_square_root_letter():
    """Test that string raises an error"""
    with pytest.raises(TypeError):
        my_module.square_root('a')
