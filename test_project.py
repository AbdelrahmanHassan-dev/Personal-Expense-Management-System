import project
import pytest

def test_right_input():
    assert project.get_info("meal, 500, 2026-01-8") == True
def test_right_input1():
    assert project.get_info("meal, 500") == True
def test_right_input2():
    assert project.get_info("") == False
def test_false_input3():
    assert project.get_info("invalid input") == False

def test_average_price_month1():
    ...

def test_expenses_right1():
    with pytest.raises(ValueError):
        project.Expenses("meal", -5)


def test_average_price_month():
    mock_data = [{"price": "1000"}, {"price": "2000"}]
    days = 30
    assert project.average_price_month((mock_data, days)) == 100

