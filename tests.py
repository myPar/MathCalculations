import unittest
import pytest
from main import RootFinder

test_timeout = 10


def in_area(epsilon, check_point, dst_point) -> bool:
    return dst_point - epsilon < check_point < dst_point + epsilon


class TestRootFinding(unittest.TestCase):
    def setUp(self) -> None:
        self.args = [[0.001, 0.1, 0, 0, 0],
                     [0.001, 0.1, 1, 0, 0],
                     [0.001, 0.1, 0, 1, 0],
                     [0.001, 0.1, 0, 0, 1],
                     [0.001, 0.1, 1, 1, 1]]
        self.answers = [[0],
                        [0, -1],
                        [0],
                        [-1],
                        [-1]]

    @pytest.mark.timeout(test_timeout)
    def test(self):
        examples_count = len(self.answers)

        for i in range(examples_count):
            test_object = RootFinder(*self.args[i])
            epsilon = self.args[i][0]

            result = sorted(test_object.find_roots())
            answer = sorted(self.answers[i])

            self.assertTrue(len(result) == len(self.answers[i]), "TEST-" + str(i) +
                            " invalid root count: " + str(result) + "\nanswer: " + str(answer))

            for j in range(len(answer)):
                result_point_value = test_object.calc_function_value(result[j])
                self.assertTrue(in_area(epsilon, result_point_value, 0), "TEST-" + str(i) +
                                " invalid root: " + str(result[j]) + "\nanswer root: " + str(answer[j]))
