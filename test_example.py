from example import add, subtract

def test_add():
    assert add(1,1) == 2

    
def test_add_str():
    """New test"""
    assert add("hello","world") == "helloworld"
    
    
def test_subtract():
    assert subtract(2,1) == 1
