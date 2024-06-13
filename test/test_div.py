"""
Test function div
"""

from main import div

def test_pos_div():
    """Test the div of positive numbers"""
    assert div(15, 5) == 3

def test_neg_div():
    """Test the div of negative numbers"""
    assert div(-8, 2) == -4
