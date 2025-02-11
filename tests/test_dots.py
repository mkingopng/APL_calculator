#
"""

"""
import pytest
from calculation.dots import DOTS

@pytest.fixture
def dots():
    return DOTS()

def test_dots_valid_cases(dots):
    assert dots.calc_dots(80, 600, False) > 0
    assert dots.calc_dots(60, 500, True) > 0

def test_dots_min_max_bodyweight(dots):
    assert dots.calc_dots(150, 700, False) > 0  # Max male
    assert dots.calc_dots(210, 900, False) > 0  # Beyond max male
    assert dots.calc_dots(40, 300, True) > 0    # Min female
    assert dots.calc_dots(150, 800, True) > 0   # Max female

def test_dots_zero_lift(dots):
    assert dots.calc_dots(80, 0, False) == 0
    assert dots.calc_dots(80, 0, True) == 0

if __name__ == "__main__":
    pytest.main()
