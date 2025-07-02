import math

class MatchService:

    @staticmethod
    def calculate_compatibility(result1, result2):
        if not result1 or not result2:
            return None
        diff = math.sqrt(
            (result1.vec_ei - result2.vec_ei) ** 2 +
            (result1.vec_sn - result2.vec_sn) ** 2 +
            (result1.vec_tf - result2.vec_tf) ** 2 +
            (result1.vec_jp - result2.vec_jp) ** 2
        )
        max_distance = math.sqrt(4 * (6 ** 2))
        return round(1 - (diff / max_distance), 2)