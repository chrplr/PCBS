"""
Coin flip streaks 

Implement the function `get_num_of_streaks()`
which takes as input
- a sequence of coin flips ("H" for head or "T" for tail) represented as a list,
- a streak length, l,
and returns how many times a streak of l heads or l tails comes up in the sequence.

For example, given ["H", "T", "T", "T", "H", "T" "T"] and l=2, it should return 3.

The function should be able to work with any list value passed to it.
Test cases have been provided for you.
Run this script with python to execute the tests.
You can be confident that you have succeeded once all the tests pass.
"""

from w_1_common import test_function_output_for_input_equals_expected, print_success

def get_num_of_streaks(coin_flips, streak_length):
    pass


expected_input_output_pairs = [ (([], 1), 0) ]

coin_flips_1 = ["H", "T", "T", "T", "H", "H", "T", "T"]
expected_input_output_pairs.extend([
    ((coin_flips_1, 4), 0),
    ((coin_flips_1, 3), 1),
    ((coin_flips_1, 2), 4),
    ((coin_flips_1, 1), 8)
])

coin_flips_2 = "T T H T T T T H H H H T T T T T T T T T H T H H H T".split()
expected_input_output_pairs.extend([
    ((coin_flips_2, 10), 0),
    ((coin_flips_2, 9), 1),
    ((coin_flips_2, 4), 8),
    ((coin_flips_2, 3), 12)
])

# Test that function yields the correct output
for input_args, output_expected in expected_input_output_pairs:
    test_function_output_for_input_equals_expected(
        get_num_of_streaks, input_args, output_expected, should_unpack_input=True
    )

# Test that function terminates on unexpected input arguments
get_num_of_streaks(coin_flips_2, 0)
get_num_of_streaks([], -1)
get_num_of_streaks(["H", "T"], -1)

print_success()
