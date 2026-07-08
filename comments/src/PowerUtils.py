class PowerUtils:

    @staticmethod
    def sum_of_squares(lower_bound, upper_bound):
        p = 0

        # Iterate from lower to upper bound 
        for i in range(lower_bound, upper_bound + 1):
            # Add square of each number in the range
            p += PowerUtils.square(i)

        # Return accumulated sum
        return p

    @staticmethod
    def square(k):
        # Return square of input
        return k * k