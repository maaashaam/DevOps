"""
Test function summ
"""

import pytest
from main import summ

def test_pos_sum():
    """Test the sum of positive numbers"""
    assert summ(1, 2) == 3

def test_neg_sum():
    """Test the sum of negative numbers"""
    assert summ(-1, 2) == 1
