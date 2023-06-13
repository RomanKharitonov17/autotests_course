import pytest
import datetime
import time


@pytest.fixture(scope='class', autouse=False)
def start_stop_time():
    print(f'\n Запуск {datetime.datetime.now()}')
    yield
    print(f'\n Завершение {datetime.datetime.now()}')


@pytest.fixture()
def execution_time():
    start_time = time.perf_counter()
    yield
    print(f'\n Время выполнения {time.perf_counter() - start_time}\n')
