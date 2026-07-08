class PowerUtils:

    @staticmethod
    def sum_of_squares(lower_bound, upper_bound):
        result = 0

        for current_value in range(lower_bound, upper_bound + 1):
            result += PowerUtils.square(current_value)

        return result

    @staticmethod
    def square(k):
        return k * k