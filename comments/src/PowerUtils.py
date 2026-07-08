class PowerUtils:

    @staticmethod
    def sum_of_squares(lower_bound, upper_bound):
        result = 0

        # Iterate from lower to upper bound 
        for current_value in range(lower_bound, upper_bound + 1):
            # Add square of each number in the range
            result += PowerUtils.square(current_value)

        return result

    @staticmethod
    def square(k):
        # Return square of input
        return k * k