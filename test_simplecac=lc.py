from simplecalc import simpint 
def test_ratezero():
    assert simpint(1200,0,5) == 0.0 
def test_timezero():
    assert simpint(1200,3,0) == 0.0     
def test_largenumberamout ():
    assert simpint(10000000,3,3) == 900000.0