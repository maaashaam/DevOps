"""
Test function dif
"""

import pytest
from main import dif

def test_pos_dif():
    """Test the dif of positive numbers"""
    assert dif(2, 1) == 1

def test_neg_dif():
    """Test the dif of negative numbers"""
    assert dif(-5, -2) == -3
