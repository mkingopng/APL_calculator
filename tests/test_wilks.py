#
"""

"""
import pytest
from calculation.wilks import Wilks

@pytest.fixture
def wilks():
    return Wilks()

def test_wilks_valid_male(wilks):
    assert wilks.calc_old_wilks(80, 600, False) > 0
    assert wilks.calc_old_wilks(120, 800, False) > 0

def test_wilks_valid_female(wilks):
    assert wilks.calc_old_wilks(60, 400, True) > 0
    assert wilks.calc_old_wilks(100, 600, True) > 0

def test_wilks_min_max_limits(wilks):
    assert wilks.calc_old_wilks(201.9, 1000, False) > 0  # Max male
    assert wilks.calc_old_wilks(154.53, 900, True) > 0   # Max female
    assert wilks.calc_old_wilks(40, 500, False) > 0      # Min male
    assert wilks.calc_old_wilks(26.51, 200, True) > 0    # Min female

def test_wilks_zero_lift(wilks):
    assert wilks.calc_old_wilks(80, 0, False) == 0
    assert wilks.calc_old_wilks(80, 0, True) == 0

if __name__ == "__main__":
    pytest.main()
