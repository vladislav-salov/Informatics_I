"""
Требуется <...> написать программу обработки данных в соответствии с выбранным и согласованным с преподавателем
вариантом (см. далее). При этом требуется контролировать типы и диапазоны вводимых данных, а также предусмотреть
обработку других исключительных ситуаций (если они есть), например, ситуацию деления на ноль.
При обнаружении ошибки ввода или ошибки вычислений программа должна информативно уведомлять пользователя о причине
ошибки. Если ошибка произошла на этапе ввода данных, то программа должна просить пользователя повторить ввод.

Создать квадратную матрицу размера M * M, где M является целым числом из диапазона [2,5].
Конкретный размер матрицы задается пользователем. Матрица должна содержать слова из чертырёх букв английского алфавита,
которые могут быть как случайными, так и вводиться пользователем. Полученную матрицу обработать следующим образом.
Из каждого слова удалить все гласные буквы. Результат удаления вывести на экран.
На основе изменённой матрицы сформировать массив, состоящий из размеров строк матрицы, который необходимо упорядочить
по убыванию. Результаты обработки вывести на экран.

Отчёт должен содержать:
...
– структурированный код программы с комментариями;
– примеры тестирования, доказывающие работоспособность;
...
"""


# Рекурсивная функция для получения кол-ва строк (столбцов) матрицы.
def size_input() -> int:
    m: str = input("Введите M: M ∈ [2, 5] ∈ ℤ для матрицы размера M * M. M = ")
    """
    # ord("0") = 48, ... , ord("2") = 50, ord("3") = 51, ord("4") = 52, ord("5") = 53, ... , ord("9") = 57.
    # try: m = int(m) — except ValueError — else.
    # m.isdecimal().
    """
    if m == "":
        print("[Ошибка]: На вход получена пустая строка.")
        print("Повторите ввод данных.")
        return size_input()
    counter: int = 0
    for symbol in m:
        counter += 1
        if counter > 1:
            print("[Ошибка]: Выход за границы диапазона.")
            print("Повторите ввод данных, учитывая, что M ∈ [2, 5].")
            return size_input()
        if ord(symbol) < 48 or ord(symbol) > 57:
            print("[Ошибка]: Неверный тип входных данных.")
            print("Повторите ввод данных, учитывая, что M ∈ ℤ.")
            return size_input()
        if ord(symbol) < 50 or ord(symbol) > 53:
            print("[Ошибка]: Выход за границы диапазона.")
            print("Повторите ввод данных, учитывая, что M ∈ [2, 5].")
            return size_input()
    return int(m)


# Рекурсивная функция для получения способа заполнения матрицы элементами.
def matrix_input_type() -> bool:
    print("Введите число для выбора способа ввода данных:")
    print("1 —  для автоматического заполнения матрицы случайным образом;")
    print("0 — для ввода элементов вручную.")
    choice: str = input("Ваш выбор (0 или 1): ")
    if choice == "":
        print("[Ошибка]: На вход получена пустая строка.")
        print("Повторите ввод данных.")
        return matrix_input_type()
    quantity: int = 0
    for symbol in choice:
        quantity += 1
        if quantity > 1:
            print("[Ошибка]: Неверный тип входных данных.")
            print("Повторите ввод данных, учитывая, что на вход подаётся только одно число.")
            return matrix_input_type()
        if ord(symbol) < 48 or ord(symbol) > 49:
            print("[Ошибка]: Выход за границы диапазона.")
            print("Повторите ввод данных, учитывая, что на вход подаётся либо 0, либо 1.")
            return matrix_input_type()
    return bool(int(choice))


# Рекурсивная функция для получения элемента матрицы с помощью интерактивного ввода.
def matrix_element_input(index: int, n_columns: int) -> str:
    coord_i: int
    coord_j: int
    element: str
    quantity: int
    coord_i = index // n_columns + 1
    coord_j = index % n_columns + 1
    element = input(f"Введите элемент {coord_i}-ой строки {coord_j}-ого столбца матрицы: ")
    if element == "":
        print("[Ошибка]: На вход получена пустая строка.")
        print("Повторите ввод данных.")
        return matrix_element_input(index, n_columns)
    quantity = 0
    for symbol in element:
        quantity += 1
        if quantity > 4:
            print("[Ошибка]: Выход за границы диапазона.")
            print("Повторите ввод данных, учитывая, что на вход подаётся строка, длиной 4.")
            return matrix_element_input(index, n_columns)
        if ord(symbol) < 65 or ord(symbol) > 122 or 90 < ord(symbol) < 97:
            print("[Ошибка]: Неверный тип входных данных.")
            print("Повторите ввод данных, учитывая, что на вход подаётся строка из 4 букв английского алфавита.")
            return matrix_element_input(index, n_columns)
    if quantity < 4:
        print("[Ошибка]: Выход за границы диапазона.")
        print("Повторите ввод данных, учитывая, что на вход подаётся строка, длиной 4.")
        return matrix_element_input(index, n_columns)
    return element


# Функция для получения матрицы, заполненной элементами.
def matrix_input(m_rows: int, n_columns: int, input_type: bool) -> [str]:
    matrix: [str] = [""] * m_rows * n_columns
    if input_type == 1:
        import random
        s: str
        upper_case: bool
        ch: str = ""
        element: str
        for index in range(m_rows * n_columns):
            s = ""
            for ch_i in range(4):
                upper_case = random.randint(0, 1)
                if upper_case == 1:
                    # chr("65") = 'A', ... , chr("90") = 'Z'
                    ch = chr(random.randint(65, 90))
                    s += ch
                else:
                    # chr("97") = 'a', ... , chr("122") = 'z'.
                    ch = chr(random.randint(97, 122))
                    s += ch
            matrix[index] = s
    else:
        print("Заполняйте матрицу поэлементно.")
        for index in range(m_rows * n_columns):
            element = matrix_element_input(index, n_columns)
            matrix[index] = element
    return matrix


# Процедура вывода матрицы matrix размером m * n.
def matrix_output(matrix: [str], m_rows: int, n_columns: int):
    for i in range(m_rows):
        print("(", end=" ")
        for j in range(n_columns):
            if j == n_columns - 1:
                print(matrix[i * n_columns + j], ")")
            else:
                print(matrix[i * n_columns + j], end=" ")


# Процедура для удаления гласных букв в элементах матрицы.
def remove_vowels(matrix: [str], m_rows: int, n_columns: int):
    element: str
    consonants: str
    for index in range(m_rows * n_columns):
        consonants = ""
        for ch_i in range(4):
            element = matrix[index][ch_i]
            if (element != "a" and element != "e" and element != "i" and
               element != "o" and element != "u" and element != "y" and
               element != "A" and element != "E" and element != "I" and
               element != "O" and element != "U" and element != "Y"):
                consonants += matrix[index][ch_i]
        matrix[index] = consonants


# Процедура вывода массива, состоящего из размеров строк матрицы, упорядоченного по убыванию.
def rows_sizes(matrix: [str], m_rows: int, n_columns: int):
    arr_of_sizes: [int] = [0] * m_rows
    size: int = 0
    for index in range(m_rows * n_columns):
        if index % n_columns == 0:
            size = 0
        size += len(matrix[index])
        if index % n_columns == n_columns - 1:
            arr_of_sizes[index // n_columns] += size
    print("Массив из размеров строк матрицы:")
    print("[", end=" ")
    for i in range(m_rows):
        if i == m_rows - 1:
            print(arr_of_sizes[i], "]")
        else:
            print(arr_of_sizes[i], end=", ")
    # Сортировка массива по невозрастанию.
    t: int
    for i in range(m_rows - 1):
        for j in range(m_rows - i - 1):
            if arr_of_sizes[j] <= arr_of_sizes[j + 1]:
                # swap(arr_of_sizes[j], arr_of_sizes[j + 1])
                t = arr_of_sizes[j]
                arr_of_sizes[j] = arr_of_sizes[j + 1]
                arr_of_sizes[j + 1] = t
    print("Массив из размеров строк матрицы, отсортированных по невозрастанию:")
    print("[", end=" ")
    for i in range(m_rows):
        if i == m_rows - 1:
            print(arr_of_sizes[i], "]")
        else:
            print(arr_of_sizes[i], end=", ")


# Главная функция.
def main():
    m: int = size_input()
    input_type: bool = matrix_input_type()
    matrix: [str] = matrix_input(m, m, input_type)
    print("Созданная матрица:")
    matrix_output(matrix, m, m)
    remove_vowels(matrix, m, m)
    print("Матрица с удалёнными гласными буквами в элементах:")
    matrix_output(matrix, m, m)
    rows_sizes(matrix, m, m)


if __name__ == "__main__":
    main()
