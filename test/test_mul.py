"""
Test function mul
"""

from main import mul

def test_pos_mul():
    """Test the mul of positive numbers"""
    assert mul(2, 4) == 8

def test_neg_mul():
    """Test the mul of negative numbers"""
    assert mul(-5, 3) == -15
