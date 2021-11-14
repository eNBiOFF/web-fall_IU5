from operator import itemgetter


class Mus:
    """Музыкант"""

    def __init__(self, id, fio, age, ork_id):
        self.id = id
        self.fio = fio
        self.age = age
        self.ork_id = ork_id


class Ork:
    """Оркестр"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class MusOrk:
    """
    'Сотрудники отдела' для реализации
    связи многие-ко-многим
    """

    def __init__(self, ork_id, mus_id):
        self.ork_id = ork_id
        self.mus_id = mus_id


# Отделы
Orks = [
    Ork(1, 'Чайковского'),
    Ork(2, 'Бетховена'),
    Ork(3, 'По кайфу'),
]

# Сотрудники
mus_d = [
    Mus(1, 'Артамонов', 25, 1),
    Mus(2, 'Петров', 23, 1),
    Mus(3, 'Иваненко', 40, 2),
    Mus(4, 'Иванов', 35, 2),
    Mus(5, 'Иванин', 25, 3),
]

musokr_link = [
    MusOrk(1, 1),
    MusOrk(2, 2),
    MusOrk(3, 3),
    MusOrk(3, 4),
    MusOrk(3, 5),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(e.fio, e.age, d.name)
                   for d in Orks
                   for e in mus_d
                   if e.ork_id == d.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, ed.ork_id, ed.mus_id)
                         for d in Orks
                         for ed in musokr_link
                         if d.id == ed.ork_id]

    many_to_many = [(e.fio, e.age, ork_name)
                    for ork_name, ork_id, mus_id in many_to_many_temp
                    for e in mus_d if e.id == mus_id]

    print('Задание В1')
    res_11 = {}
    for d in Orks:
        d_mus = list(filter(lambda i: i[2] == d.name, one_to_many))
        if len(d_mus) > 0:
            d_mus_names = [x for x, _, _ in d_mus]
            d_mus_names_a = []
            for el in d_mus_names:
                if el[0] == 'А':
                    d_mus_names_a.append(el)
            res_11[d.name] = d_mus_names_a
    print(res_11)

    print('\nЗадание В2')
    res_12_unsorted = []
    for d in Orks:
        d_mus = list(filter(lambda i: i[2] == d.name, one_to_many))
        if len(d_mus) > 0:
            d_mus_age = [age for _, age, _ in d_mus]
            d_mus_age_min = min(d_mus_age)
            res_12_unsorted.append((d.name, d_mus_age_min))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание В3')
    res_13 = sorted(many_to_many, key=itemgetter(2))
    print(res_13)


if __name__ == '__main__':
    main()
