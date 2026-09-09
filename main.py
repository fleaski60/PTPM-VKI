import logging
import sys
import os
from triangle_calcul import calculate_triangle

os.makedirs("logs", exist_ok=True)

log_format = "%(asctime)s | [%(levelname)-7s] | %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(
    level=logging.DEBUG,
    format=log_format,
    datefmt=date_format,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("logs/file_txt.log", encoding="utf-8")
    ]
)

logging.info("Логгер успешно сконфигурирован")
logging.info("Приложение запущено")

side_a = input("A: ")
side_b = input("B: ")
side_c = input("C: ")

t_type, coords = calculate_triangle(side_a, side_b, side_c)

print(f"тип треугольника : {t_type if t_type else '(пусто)'}")
print(f"координаты вершин : {coords}\n")

if coords == [(-2, -2), (-2, -2), (-2, -2)]:
    logging.error(f"ошибка ввода (не число): a='{side_a}', b='{side_b}', c='{side_c}'")
elif coords == [(-1, -1), (-1, -1), (-1, -1)]:
    logging.error(f"не треугольник: a='{side_a}', b='{side_b}', c='{side_c}'")
else:
    logging.info(f"тип='{t_type}', координаты={coords}")