class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        abs_divisor = abs(divisor)
        abs_dividend = abs(dividend)
        result = 0
        is_negative = (dividend < 0) ^ (divisor < 0)

        current_sum = abs_divisor
        current_multiple = 1
        last_sum = 0
        last_multiple = 0

        while current_sum <= abs_dividend:
            last_sum = current_sum
            last_multiple = current_multiple

            current_sum += current_sum
            current_multiple += current_multiple

            if current_sum > abs_dividend:
                if last_sum + abs_divisor <= abs_dividend:
                    result += last_multiple
                    abs_dividend -= last_sum
                    current_sum = abs_divisor
                    current_multiple = 1
                    last_sum = 0
                    last_multiple = 0

        result += last_multiple
        result = -result if is_negative else result
        return max(min(result, 2**31 - 1), -2**31)