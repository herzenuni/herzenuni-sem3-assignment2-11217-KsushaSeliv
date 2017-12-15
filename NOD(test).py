import pytest
import nod
def function_1(A,B,C):
    def test():
        assert nod.nod(A,B)==C
    return test

test_1 = function_1(6,36,6)
test_2 = function_1(18,54,18)
