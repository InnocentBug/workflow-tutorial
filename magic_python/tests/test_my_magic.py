import pytest
import numpy as np
# We want numpy to give us expections
np.seterr(all='raise')
import magic_python

def test_values():
    result = magic_python.my_magic_function(17., 45.)
    expected_result = np.log(17.) + np.log(45.)
    assert result == expected_result

def test_math():
    result = magic_python.my_magic_function(14., 72.)
    expected_result = np.log(14. *72.)
    # with pytest.raises(AssertionError):
    #     assert expected_result == result
    assert pytest.approx(expected_result, 1e-6) == result

def test_test_negative():
    with pytest.raises(FloatingPointError):
        magic_python.my_magic_function(-1, 23.)
    with pytest.raises(FloatingPointError):
        magic_python.my_magic_function(5, -23.)
    with pytest.raises(FloatingPointError):
        magic_python.my_magic_function(0, 2.)
    with pytest.raises(FloatingPointError):
        magic_python.my_magic_function(7, 0.)
