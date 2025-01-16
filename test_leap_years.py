from leap_year_calc import is_leap_year

def test_leap_year_div_4():
    assert is_leap_year(2020) == True
    
def test_leap_year_div_100():
    assert is_leap_year(1900) == False
    
def test_leap_year_div_400():
    assert is_leap_year(2000) == True
    
def test_odd_year():
    assert is_leap_year(2019) == False