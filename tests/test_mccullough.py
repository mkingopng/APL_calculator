# tests/test_mccullough.py
"""
Test the mccullough module.
"""
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from calculation.mccullough import McCulloughFoster


def test_mccullough_calculation():
    mc = McCulloughFoster()

    # Test with known values
    assert mc.calc_mccullough(80, 600, False, 30) > 0
    assert mc.calc_mccullough(60, 500, True, 50) > 0

    # Test with invalid age (should default to 1.0 coefficient)
    assert mc.calc_mccullough(80, 600, False, -5) == mc.calc_mccullough(80, 600, False, 1)

    # Edge cases
    assert mc.calc_mccullough(0, 0, False, 23) == 0

if __name__ == "__main__":
    pytest.main()
