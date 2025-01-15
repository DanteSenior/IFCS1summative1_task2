from leap_year_calc import is_leap_year

def test_is_year_div_by_4():
    assert is_leap_year(2020) == True

def test_is_year_div_by_100():
    assert is_leap_year(1900) == False

def test_is_year_div_by_400():
    assert is_leap_year(2000) == True

def test_non_leap_year():
    assert is_leap_year(2021) == False