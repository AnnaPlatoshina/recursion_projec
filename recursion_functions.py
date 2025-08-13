# 01. Рекурсивная функция для вычисления факториала
def factorial(n):
    """
    Вычисляет факториал числа n рекурсивно
    :param n: целое неотрицательное число
    :return: факториал числа n
    """
    if n == 0:  # базовый случай
        return 1
    else:
        return n * factorial(n - 1)  # рекурсивный случай


# 02. Рекурсивная функция для вычисления суммы элементов списка
def sum_list(lst):
    """
    Вычисляет сумму всех элементов в списке рекурсивно
    :param lst: список чисел
    :return: сумма элементов списка
    """
    if not lst:  # базовый случай - пустой список
        return 0
    else:
        return lst[0] + sum_list(lst[1:])  # рекурсивный случай


# 03. Рекурсивная функция бинарного поиска
def binary_search(arr, target, low=0, high=None):
    """
    Выполняет бинарный поиск элемента в отсортированном списке рекурсивно
    :param arr: отсортированный список
    :param target: искомый элемент
    :param low: нижняя граница поиска (по умолчанию 0)
    :param high: верхняя граница поиска (по умолчанию длина списка - 1)
    :return: индекс элемента или -1, если элемент не найден
    """
    if high is None:
        high = len(arr) - 1

    if low > high:  # базовый случай - элемент не найден
        return -1

    mid = (low + high) // 2
    if arr[mid] == target:  # базовый случай - элемент найден
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)  # рекурсивный случай - ищем в левой половине
    else:
        return binary_search(arr, target, mid + 1, high)  # рекурсивный случай - ищем в правой половине


# 04. Класс Stack
class Stack:
    """
    Реализация стека с основными операциями: push, pop, is_empty, peek
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        """Добавляет элемент на вершину стека"""
        self.items.append(item)

    def pop(self):
        """Удаляет и возвращает элемент с вершины стека"""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def is_empty(self):
        """Проверяет, пуст ли стек"""
        return len(self.items) == 0

    def peek(self):
        """Возвращает элемент с вершины стека без удаления"""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def size(self):
        """Возвращает количество элементов в стеке"""
        return len(self.items)


# Тестирование функций
if __name__ == "__main__":
    # Тест факториала
    print("Факториал 5:", factorial(5))  # Должно быть 120

    # Тест суммы списка
    print("Сумма [1, 2, 3, 4]:", sum_list([1, 2, 3, 4]))  # Должно быть 10

    # Тест бинарного поиска
    sorted_list = [1, 3, 5, 7, 9, 11, 13]
    print("Индекс 7 в списке:", binary_search(sorted_list, 7))  # Должно быть 3
    print("Индекс 8 в списке:", binary_search(sorted_list, 8))  # Должно быть -1

    # Тест стека
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Вершина стека:", stack.peek())  # Должно быть 3
    print("Удаленный элемент:", stack.pop())  # Должно быть 3
    print("Стек пуст?", stack.is_empty())  # Должно быть False
    print("Размер стека:", stack.size())  # Должно быть 2