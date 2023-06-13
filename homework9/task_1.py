# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
from pathlib import Path

with open(Path("test_file", "task1_data.txt"), 'r', encoding='utf-8') as file:
    file_content = file.read()
with open(Path("test_file", "task1_answer.txt"), 'w', encoding='utf-8') as file_text:
    for symbol in file_content:
        if not symbol.isdigit():
            file_text.write(symbol)
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
