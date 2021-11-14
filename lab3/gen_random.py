import random


def gen_random(num, start, stop):
    arr = []
    for i in range(num):
        arr.append(random.randint(start, stop))
    return arr


def main():
    arr = gen_random(5, 1, 30)
    [print(i) for i in arr]


if __name__ == '__main__':
    main()
