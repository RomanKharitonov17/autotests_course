import pytest
import datetime
import time


@pytest.fixture(scope='class', autouse=True)
def start_stop_time():
    print(f'\n Запуск {datetime.datetime.now()}\n')
    yield
    print(f'\n Завершение {datetime.datetime.now()}')

@pytest.fixture()
def execution_time():
    start_time = time.perf_counter()
    yield
    print(f'\n Время выполнения {time.perf_counter()- start_time}\n')