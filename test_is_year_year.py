from is_year_prime import is_year_prime

def test_is_year_div_4():
    assert is_year_prime(2024) == True
    
def test_is_year_div_100():
    
    assert is_year_prime(1900) == False
    
def test_is_year_div_400():
    assert is_year_prime(2000) == True
    
def test_is_year_not_prime():
    assert is_year_prime(2021) == False