"""
Common utility functions for week 1 exercises
"""

def test_function_output_for_input_equals_expected(function, input, output_expected,
    should_unpack_input=False, verbose=True):
    if verbose:
        print("input", input)
    output_actual = function(*input) if should_unpack_input else function(input)
    if verbose:
        print("output", output_actual)
    assert output_actual == output_expected

def print_success():
    print("Exercise complete!")
