def field(dict, *args):
    assert len(args) > 0
    if len(args) > 1:
        dict1 = [{j: i[j] for j in args if j in i.keys()} for i in dict]
    else:
        dict1 = [i[j] for i in dict for j in args if j in i.keys()]
    return dict1


def main():
    goods = [
        {'title': 'Диван', 'price': 2500, 'color': 'green'},
        {'title': 'Ковер', 'price': 1000}
    ]
    field(goods, 'title')
    field(goods, 'title', 'price')
    field(goods, 'title', 'price', 'color')


if __name__ == '__main__':
    main()
