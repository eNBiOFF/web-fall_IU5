import json
import sys
from print_result import print_result
from lab3 import field
from cm_timer import cm_timer
from unique import Unique
from gen_random import gen_random
# Сделаем другие необходимые импорты

path = 'C:/Users/nikik/web-fall_IU5/lab3/data_light.json'

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path, 'r', encoding='utf8') as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк


@print_result
def f1(arg):
    return sorted(Unique(field(arg, 'job-name'), ignore_case=True))


@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' c опытом Python', arg))


@print_result
def f4(arg):
    salary_dict = gen_random(len(arg), 100000, 200000)
    return list(map(lambda x, y: x + ' c запрлатой ' + str(y), arg, salary_dict))


if __name__ == '__main__':
    with cm_timer():
        f4(f3(f2(f1(data))))