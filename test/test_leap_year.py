import pytest

from leap_year import is_leap_year


# leap year tests
def test_leap_year_divisible_by_4_and_not_100():
    assert is_leap_year(2008)
    assert is_leap_year(2016)
    assert is_leap_year(2032)


def test_leap_year_divisible_by_400():
    assert is_leap_year(2000)
    assert is_leap_year(2400)
    assert is_leap_year(2800)
    assert is_leap_year(400)


# not leap year tests
def test_not_leap_year_not_divisible_by_4():
    assert not is_leap_year(1777)
    assert not is_leap_year(1989)
    assert not is_leap_year(2005)


@pytest.mark.parametrize("test_year", [
    1700,
    1800,
    1900,
    2100
])
def test_not_leap_year_divisible_by_100_not_400(test_year):
    assert not is_leap_year(test_year)
