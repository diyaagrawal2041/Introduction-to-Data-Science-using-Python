#The dataset file in assets/grades.txt contains a line separated list of people with their grade in a class. 
#Create a regex to generate a list of just those students who received a B in the course.

import re
def grades():
    with open ("assets/grades.txt", "r") as file:
        grades = file.read()

    # YOUR CODE HERE
    result = re.findall('([A-Z]\\S*\\s[A-Z]\\S*): B', grades)
    return result
    raise NotImplementedError()
assert len(grades()) == 16
