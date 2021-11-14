# Итератор для удаления дубликатов
class Unique:
    """Итератор, оставляющий только уникальные значения."""
    def __init__(self, data, **kwargs):
        self.used_elements = set()
        self.data = data
        self.index = 0
        self.ignore_case = False
        for v in kwargs.values():
            self.ignore_case = v

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            else:
                current = self.data[self.index]
                if self.ignore_case:
                    current = str(current).lower()
                self.index = self.index + 1
                if current not in self.used_elements:
                    # Добавление в множество производится
                    # с помощью метода add
                    self.used_elements.add(current)
                    return current


def main():
    abs = ['A', 'b', 'S', 'A', 'a', 'A', 'B', 'b', 's']
    for i in Unique(abs, ignore_case=True):
        print(i)


if __name__ == "__main__":
    main()
