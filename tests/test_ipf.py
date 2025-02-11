#
"""

"""
import pytest
from calculation.ipf import IPF

@pytest.fixture
def ipf():
    return IPF()

def test_ipf_valid_cases(ipf):
    assert ipf.calc_ipf(80, 600, False, "CLPL") > 0
    assert ipf.calc_ipf(60, 500, True, "EQPL") > 0

def test_ipf_invalid_competition(ipf):
    assert ipf.calc_ipf(80, 600, False, "UNKNOWN") == "0.00"

def test_ipf_zero_lift(ipf):
    assert ipf.calc_ipf(80, 0, False, "CLPL") == "0.00"
    assert ipf.calc_ipf(80, 0, True, "CLPL") == "0.00"

if __name__ == "__main__":
    pytest.main()
