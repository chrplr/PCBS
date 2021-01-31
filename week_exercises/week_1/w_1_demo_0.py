"""
Mean

Implement the function `get_mean()`,
which takes as input a list of numeric values,
and returns their mean.

For example, passing the list [3.2, 100, -2, 0] would return 25.3

The function should be able to work with any list value passed to it.
Test cases have been provided for you.
Run this script with python to execute the tests.
You will know that you have succeeded once all the tests pass.
"""

from w_1_common import test_function_output_for_input_equals_expected, print_success

def get_mean(values):
    pass


expected_input_output_pairs = [
    ([9.1], 9.1),
    ([3.2, 100, -2, 0], 25.3),
    ([], 0),
]

for input_value, output_expected in expected_input_output_pairs:
    test_function_output_for_input_equals_expected(
        get_mean, input_value, output_expected
    )
print_success()
