import pytest

from leap_year import leapyear


# Parametrize known years divisible by 4 but not divisible by 100 in "year", every value "year" should return True.
@pytest.mark.parametrize("year", [2004, 1612, 2408, 2824, 3220, 1240, 2012])
def test_leapyear_is_divisible_by_4_but_not_100(year):
    assert leapyear(year) == True


# Parametrize known years divisible by 400 in "year", every value "year" should return True.
@pytest.mark.parametrize("year", [400, 800, 1200, 1600, 2000, 2400])
def test_leapyear_is_divisible_by_400(year):
    assert leapyear(year) == True


# Parametrize known years not divisible by 4. Every value "year" should return False
@pytest.mark.parametrize("year", [1019, 1267, 1895, 1993, 2003, 2023])
def test_leapyear_is_not_divisible_by_4(year):
    assert leapyear(year) == False


# Parametrize known years divisible by 100 but not divisible by 400. Every value "year" should return False
@pytest.mark.parametrize("year", [100, 600, 900, 1100, 1500, 1700, 1800, 2100])
def test_leapyear_is_divisible_by_100_but_not_400(year):
    assert leapyear(year) == False
