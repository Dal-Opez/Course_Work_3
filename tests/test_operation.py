from course_work_3.operation import Operation
import pytest


@pytest.fixture
def fixture_class_example_1():
    return Operation('2019-08-26T10:50:58.294041', {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                     'Перевод организации', 'Maestro 1596837868705199', 'Счет 64686473678894779589')

@pytest.fixture
def fixture_class_example_2():
    return Operation('2019-08-26T10:50:58.294041', {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                     'Перевод организации', 'Счет 64686475698894771488', 'Maestro 1596837868705199')


def test_get_date(fixture_class_example_1):
    assert fixture_class_example_1.get_date() == '26.08.2019'

def test_get_description(fixture_class_example_1):
    assert fixture_class_example_1.get_description() == 'Перевод организации'

def test_convert_card(fixture_class_example_1):
    assert fixture_class_example_1.convert_card('Maestro 1596837868705199') == "Maestro 1596 83** **** 5199"

def test_convert_account(fixture_class_example_1):
    assert fixture_class_example_1.convert_account("Счет 64686473678894779589") == "Счет **9589"

def test_get_where_from(fixture_class_example_1, fixture_class_example_2):
    assert fixture_class_example_1.get_where_from() == 'Maestro 1596 83** **** 5199'
    assert fixture_class_example_2.get_where_from() == 'Счет **1488'

def test_get_to(fixture_class_example_1, fixture_class_example_2):
    assert fixture_class_example_1.get_to() == 'Счет **9589'
    assert fixture_class_example_2.get_to() == 'Maestro 1596 83** **** 5199'

def test_get_amount(fixture_class_example_1):
    assert fixture_class_example_1.get_amount() == '31957.58'

def test_get_amount_name(fixture_class_example_1):
    assert fixture_class_example_1.get_amount_name() == 'руб.'