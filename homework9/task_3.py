# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
with open("test_file/task_3.txt") as file:
    total_prices = []
    purchases = []
    for line in file:
        try:
            price = int(line.strip())
            purchases.append(price)
        except ValueError:
            if purchases:
                total_prices.append(sum(purchases))
                purchases = []
    if purchases:
        total_prices.append(sum(purchases))
    three_most_expensive_purchases = sum(sorted(total_prices)[-3:])

assert three_most_expensive_purchases == 202346
