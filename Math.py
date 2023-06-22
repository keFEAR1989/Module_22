def binary_search(lst, x):
    """Бинарный поиск"""
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left


def insertion_sort(lst):
    """Сортировка вставками"""
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key


def main():
    # Ввод последовательности чисел
    while True:
        try:
            lst = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
            break
        except ValueError:
            print("Некорректный ввод. Попробуйте еще раз.")

    # Сортировка
    insertion_sort(lst)

    # Ввод числа для поиска
    while True:
        try:
            x = int(input("Введите число для поиска: "))
            break
        except ValueError:
            print("Некорректный ввод. Попробуйте еще раз.")

    # Поиск позиции числа
    pos = binary_search(lst, x)

    # Проверка соответствия ввода
    if pos == len(lst):
        print(f"Число {x} больше всех элементов в последовательности.")
    elif lst[pos] == x:
        print(f"Число {x} находится на позиции {pos}.")
    else:
        print(f"Число {x} должно быть на позиции {pos}, но отсутствует в последовательности.")


if __name__ == '__main__':
    main()