#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!
# Checks that the program outputs "1" for an input of "2 - 1"
assert run("2 - 1").output == "1"
# Checks that the program outputs "2" for an input of "4 / 2"
assert run("4 / 2").output == "2"
###

print("All tests passed!")