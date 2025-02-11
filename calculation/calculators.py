# calculation/calculators.py
"""
calculators.py - Powerlifting score calculators including McCullough
"""
from calculation.dots import DOTS
from calculation.goodlift import GoodLift
from calculation.ipf import IPF
from calculation.wilks import Wilks
from calculation.wilks_2 import Newwilks
from calculation.mccullough import McCulloughFoster

def get_scores(body_weight, total, is_kg, is_female, competition, age):
    """
    Generate scores based on inputs
    :param body_weight: Body weight of the lifter
    :param total: Total weight lifted (sum of squat, bench, and deadlift)
    :param is_kg: Boolean indicating if units are in kilograms
    :param is_female: Boolean indicating if the lifter is female
    :param competition: Type of competition
    :param age: Age of the lifter
    :return: Dictionary with calculated scores
    """
    weight_coeff = 0.45359237
    body_weight = body_weight if is_kg else body_weight * weight_coeff
    total = total if is_kg else total * weight_coeff

    # Instantiate calculators
    wilks_calculator = Wilks()
    new_wilks_calc = Newwilks()
    dots_calc = DOTS()
    ipf_calc = IPF()
    goodlift_calc = GoodLift()
    mccullough_calc = McCulloughFoster()  # ✅ Ensure this class is implemented

    return {
        "body_weight": body_weight,
        "total": total,
        "unit": "KG" if is_kg else "LB",
        "old_wilks": wilks_calculator.calc_old_wilks(body_weight, total, is_female),
        "new_wilks": new_wilks_calc.calculate_new_wilks(body_weight, total, is_female),
        "dots": dots_calc.calc_dots(body_weight, total, is_female),
        "ipf": ipf_calc.calc_ipf(body_weight, total, is_female, competition),
        "good_lifts": goodlift_calc.calc_goodlift(body_weight, total, is_female, competition),
        "mccullough": mccullough_calc.calc_mccullough(body_weight, total, is_female, age)
    }
