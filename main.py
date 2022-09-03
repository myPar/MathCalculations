import math
import plotly.express as px
import numpy as np


class RootFinder(object):
    def __init__(self, epsilon, delta, a, b, c):
        self.epsilon = epsilon
        self.delta = delta
        self.a = a
        self.b = b
        self.c = c

    def calc_function_value(self, x):
        return x**3 + self.a * x**2 + self.b * x + self.c

    def calc_function_der_value(self, x):
        return 3 * x**2 + 2 * self.a * x + self.b

    # finds unknown bound and returns segment
    def get_segment(self, st_point) -> list:
        st_point_value = self.calc_function_value(st_point)
        end_point = st_point

        if st_point_value > 0:
            direction = -1
        elif st_point_value < 0:
            direction = 1
        else:
            assert False

        while st_point_value * self.calc_function_value(end_point) >= 0:
            end_point += self.delta * direction

        return sorted([st_point, end_point])

    # find root on segment
    def find_root(self, left_bound, right_bound):
        assert left_bound < right_bound

        result = left_bound + (right_bound - left_bound) / 2
        result_value = self.calc_function_value(result)

        while abs(result_value) >= self.epsilon:
            if result_value * self.calc_function_value(left_bound) < 0:
                right_bound = result
            elif result_value * self.calc_function_value(right_bound) < 0:
                left_bound = result
            else:
                # result value is equal to 0 so this is the root
                return result

            result = left_bound + (right_bound - left_bound) / 2
            result_value = self.calc_function_value(result)

        return result

    # returns list of extremums
    def find_extremums(self):
        discriminant = 4 * self.a ** 2 - 12 * self.b

        if discriminant < 0:
            return []
        elif discriminant == 0:
            return [-self.a / 3]
        else:
            return [(-2 * self.a - math.sqrt(discriminant))/6, (-2 * self.a + math.sqrt(discriminant)) / 6]

    # returns list of roots of our equation
    def find_roots_two_extremums(self, extremums_points):
        local_max = extremums_points[0]
        local_min = extremums_points[1]

        local_max_value = self.calc_function_value(local_max)
        local_min_value = self.calc_function_value(local_min)

        assert local_max_value > local_min_value and local_max < local_min

        if local_min_value > 0:
            segment = self.get_segment(local_max)

            return [self.find_root(*segment)]

        elif local_min_value == 0:
            segment = self.get_segment(local_max)

            return [self.find_root(*segment), local_min]

        elif local_min_value < 0 < local_max_value:
            segment1 = self.get_segment(local_max)
            segment2 = [local_max, local_min]
            segment3 = self.get_segment(local_min)

            return [self.find_root(*segment1), self.find_root(*segment2), self.find_root(*segment3)]

        elif local_max_value == 0:
            segment = self.get_segment(local_min)

            return [local_max, self.find_root(*segment)]
        else:
            segment = self.get_segment(local_min)

            return [self.find_root(*segment)]

    # returns list of roots
    def find_roots(self):
        extremums = self.find_extremums()
        extremums_count = len(extremums)

        if extremums_count == 2:
            return self.find_roots_two_extremums(extremums)
        else:
            st_point = 0
            st_point_value = self.calc_function_value(st_point)

            if st_point_value == 0:
                return [st_point_value]

            bounds = self.get_segment(st_point)

            return [self.find_root(*bounds)]
