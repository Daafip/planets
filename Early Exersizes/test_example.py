from example import add 


def test_add():
    assert add(2,3) == 5
    assert add(1,0) == 1

def test_string_add():
    assert add("hello", "world") == "helloworld"

def helper():
    print('Hi, im a helper')
