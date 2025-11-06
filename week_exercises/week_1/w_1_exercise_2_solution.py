"""
Comma code

Implement the function `get_string_by_enumerating_items()`
which takes a list of string items as an argument and
returns a string with all the items separated by a comma and a space,
with 'and' inserted before the last item.

For example, passing the list ["apples", "bananas", "tofu", "cats"]
would return "apples, bananas, tofu, and cats",
and passing ["apples", "bananas"] would return "apples, and bananas".

The function should be able to work with any list value passed to it.
Test cases have been provided for you.
Run this script with python to execute the tests.
You can be confident that you have succeeded once all the tests pass.
"""

from w_1_common import test_function_output_for_input_equals_expected, print_success

def get_string_by_enumerating_items(items):
    n_items = len(items)
    if n_items > 1:
        items_before_last, last_item = items[:-1], items[-1]
        string_before_last = ", ".join(items_before_last)
        return ", and ".join([string_before_last, last_item])
    elif n_items == 1:
        return items[0]
    else:
        return ""


expected_input_output_pairs = [
   (["birthday"], "birthday"),
   (["control", "quality"], "control, and quality"),
   (["insect", "medicine", "disk", "contract", "relationship", "map"],
    "insect, medicine, disk, contract, relationship, and map"),
   ([], "")
]
for input_value, output_expected in expected_input_output_pairs:
    test_function_output_for_input_equals_expected(
        get_string_by_enumerating_items, input_value, output_expected
    )
print_success()
