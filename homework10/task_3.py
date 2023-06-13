# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("args, expected_result", [
    ((4, 2), 2),
    ((6, 3), 2),
    ((), IndexError),
    pytest.param((10, 0), ZeroDivisionError, marks=pytest.mark.skip(reason="division by zero")),
    pytest.param(('a', 'b'), TypeError, marks=pytest.mark.smoke)
])
def test_all_division(args, expected_result):
    try:
        assert all_division(*args) == expected_result
    except Exception as ex:
        assert type(ex) == expected_result

