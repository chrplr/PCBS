"""
Word counts

Implement the function `get_word_counts()`,
which takes as input a list of words,
and returns a dictionary which maps each word in the list
to the number of times this word appears (case-sensitive) in the list.

For example, passing the list ["Jim", "Apple", "Jim", "apple", "Joe"]
would return {"Jim": 2, "Apple": 1, "apple": 1, "Joe": 1}.

The function should be able to work with any list value passed to it.
Test cases have been provided for you.
Run this script with python to execute the tests.
You will know that you have succeeded once all the tests pass.
"""

from w_1_common import test_function_output_for_input_equals_expected

def get_word_counts(words):
    pass


expected_input_output_pairs = [
    ([], {}),
    (["20-hour-long"], {"20-hour-long": 1}),
    (["Jim", "Apple", "Jim", "apple", "Joe"],
     {"Jim": 2, "Apple": 1, "apple": 1, "Joe": 1})
]
words = """no man is an island entire of itself
    every man is a piece of the continent a part of the main""".split()
word_counts = {"no": 1, "man": 2, "is": 2, "an": 1, "island": 1, "entire": 1,
    "of": 3, "itself": 1, "every": 1, "a": 2, "piece": 1,
    "the": 2, "continent": 1, "part": 1, "main": 1}
expected_input_output_pairs.append((words, word_counts))

for input_value, output_expected in expected_input_output_pairs:
    test_function_output_for_input_equals_expected(
        get_word_counts, input_value, output_expected
    )
