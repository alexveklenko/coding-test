import pytest
from .task import get_temperature_closest_to_zero


def test_get_temperature_closest_to_zero():
    assert get_temperature_closest_to_zero([1, 2, 100, -0.5, 2, 0.5]) == 0.5
    assert get_temperature_closest_to_zero([0, 1, 2, 100, -0.5, 2, 0.5]) == 0
    assert get_temperature_closest_to_zero([1, 2, 100, 0.5, 2, -0.5]) == 0.5
    assert get_temperature_closest_to_zero([1, 2, 100, -0.5, 2]) == -0.5
    assert get_temperature_closest_to_zero([]) == 0
