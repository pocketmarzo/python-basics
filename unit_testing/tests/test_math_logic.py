import pytest
from hello import add, divide



def test_add():
    assert add(2, 2) == 4
    assert add(5, -3) == 2

def test_add_errors():
    with pytest.raises(TypeError):
        add("1", 2)
    with pytest.raises(TypeError):
        add(1, "2")

def test_divide():
    assert divide(10, 2) == 5

def test_divide_errors():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


