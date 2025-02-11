# calculation/mccullough.py
"""
McCullough-Foster Score Calculation
"""

class McCulloughFoster:
    """
    Implements the McCullough-Foster coefficient calculation.
    Includes age coefficients as per verified sources.
    """

    AGE_COEFFICIENTS = [
        0.0, 0.0, 0.0, 0.0, 0.0,  # 0-4: No coefficients exist
        1.73, 1.67, 1.61, 1.55, 1.49, 1.43, 1.38, 1.33, 1.28,  # 5-13
        1.23, 1.18, 1.13, 1.08, 1.06, 1.04, 1.03, 1.02, 1.01,  # 14-22
        *[1.0] * 18,  # 23-40: No adjustment
        1.01, 1.02, 1.031, 1.043, 1.055, 1.068, 1.082, 1.097, 1.113, 1.13,  # 41-50
        1.147, 1.165, 1.184, 1.204, 1.225, 1.246, 1.268, 1.291, 1.315, 1.34,  # 51-60
        1.366, 1.393, 1.421, 1.45, 1.48, 1.511, 1.543, 1.576, 1.61, 1.645,  # 61-70
        1.681, 1.718, 1.756, 1.795, 1.835, 1.876, 1.918, 1.961, 2.005, 2.05,  # 71-80
        2.096, 2.143, 2.19, 2.238, 2.287, 2.337, 2.388, 2.44, 2.494, 2.549,  # 81-90
        2.605, 2.662, 2.72, 2.779, 2.839, 2.9, 2.962, 3.025, 3.089, 3.154   # 91-100
    ]

    def __init__(self):
        self.male_coeff = [0.00001, -0.002, 0.5, 10]  # TODO: Confirm coefficients
        self.female_coeff = [0.00002, -0.0015, 0.4, 9]  # TODO: Confirm coefficients

    @staticmethod
    def foster_mcculloch(age: int) -> float:
        """
        Get the McCullough-Foster coefficient for the given age.
        :param age: Age of the lifter.
        :return: Age coefficient.
        """
        if not isinstance(age, int) or age <= 0:
            return 1.0

        return McCulloughFoster.AGE_COEFFICIENTS[min(age, len(McCulloughFoster.AGE_COEFFICIENTS) - 1)]

    def calc_mccullough(self, body_weight: float, total: float, is_female: bool, age: int) -> float:
        """
        Calculate McCullough score including age adjustment.
        :param body_weight: Body weight of the lifter.
        :param total: Total weight lifted.
        :param is_female: Boolean indicating if the lifter is female.
        :param age: Age of the lifter.
        :return: Adjusted McCullough score.
        """
        coeff = self.female_coeff if is_female else self.male_coeff
        base_score = (coeff[0] * (body_weight ** 3)) + (coeff[1] * (body_weight ** 2)) + (coeff[2] * body_weight) + coeff[3]
        age_coeff = self.foster_mcculloch(age)
        return round(base_score * total * age_coeff, 2)  # Apply total lift multiplier and age adjustment
