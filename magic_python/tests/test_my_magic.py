import numpy as np
import pytest

import magic_python

# We want numpy to give us expections
np.seterr(all="raise")


def test_values():
    result = magic_python.my_magic_function(17.0, 45.0)
    expected_result = np.log(17.0) + np.log(45.0)
    assert result == expected_result


def test_math():
    result = magic_python.my_magic_function(14.0, 72.0)
    expected_result = np.log(14.0 * 72.0)
    # with pytest.raises(AssertionError):
    #     assert expected_result == result
    assert pytest.approx(expected_result, 1e-6) == result


def test_test_negative():
    with pytest.raises(FloatingPointError):
        magic_python.my_magic_function(-1, 23.0)
    with pytest.raises(FloatingPointError):
        magic_python.my_magic_function(5, -23.0)
    with pytest.raises(FloatingPointError):
        magic_python.my_magic_function(0, 2.0)
    with pytest.raises(FloatingPointError):
        magic_python.my_magic_function(7, 0.0)
