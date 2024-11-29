'''
Напишите скрипт, который считывает данные из CSV файла, содержащего
информацию о продажах (название продукта, количество, цена за единицу), и
подсчитывает общую выручку для каждого продукта. Итог должен быть сохранён в
новом CSV файле.
'''

import csv
from pathlib import Path

def calculate_csv(input_file: Path, output_file: Path) -> None:
    """

    """

    total_sales = {}

    with open(input_file, 'r', encoding='utf8', newline='') as f:
        reader = csv.DictReader(f)


        for row in reader:
            product = row['product']
            quantity = int(row['quantity'])
            price_per_unit = float(row['price'])
            total = quantity * price_per_unit

            if product in total_sales:
                total_sales[product] += total
            else:
                total_sales[product] = total


    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['название продукта', 'общая выручка'])
        writer.writeheader()

        for product, total in total_sales.items():
            writer.writerow({'название продукта': product, 'общая выручка': total})



if __name__ == '__main__':
    calculate_csv(Path('sales.csv'), Path('total.csv'))