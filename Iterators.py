class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.flatten_list = self.flatten(self.list_of_lists)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        '''
        Возвращает каждый вложенный элемент из списка списков list_of_list,
        когда элементы заканчиваются, вывзывает StopIteration
        '''
        if self.index < len(self.flatten_list):
            item = self.flatten_list[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

    def flatten(self, nested_list):
        '''
        Данный метод рекурсивно обходит вложенные списки, создавая плоский список.
        Для каждого элемента в nested_list проверяется, является ли он списком, если да, то метод
        рекурсивно вызывает сам себя для этого подсписка, если же элемент не является списком,
        он добавляется в result
        '''
        result = []
        for sublist in nested_list:
            if isinstance(sublist, list):
                result.extend(self.flatten(sublist))
            else:
                result.append(sublist)
        return result


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
