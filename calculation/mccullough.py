# calculation/mccullough.py
"""
McCullough score calculation
"""
class McCullough:
    """
    Formula for McCullough coefficient calculation.
    Ensure the coefficients are correctly implemented.
    """
    def __init__(self):
        self.male_coeff = [0.00001, -0.002, 0.5, 10]  # todo: confirm coefficients
        self.female_coeff = [0.00002, -0.0015, 0.4, 9]  # todo: confirm coefficients

    def calc_mccullough(self, body_weight, total, is_female):
        """
        Calculate McCullough score
        :param body_weight: Body weight of the lifter
        :param total: Total weight lifted
        :param is_female: Boolean indicating if the lifter is female
        :return: McCullough score
        """
        coeff = self.female_coeff if is_female else self.male_coeff
        score = (coeff[0] * (body_weight ** 3)) + (coeff[1] * (body_weight ** 2)) + (coeff[2] * body_weight) + coeff[3]
        return round(score * total, 2)  # Apply total lift multiplier
