#Find a list of all of the names in the following string using regex.

import re
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    # YOUR CODE HERE
    result = re.findall("[A-Z][a-z]*",simple_string)
    return result
    raise NotImplementedError()
assert len(names()) == 4, "There are four names in the simple_string"
