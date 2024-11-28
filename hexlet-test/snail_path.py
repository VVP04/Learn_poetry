def snail_path(matrix: list) -> list:
    result = []
    # Цикл улитки
    while matrix:
        if not matrix[0]:
            break
        # Добавить первую строку
        for element in matrix[0]:
            result.append(element)
        # Удалить первую строку
        matrix.remove(matrix[0])
        if matrix:
            # Добавить последний столбец
            for coll in matrix:
                result.append(coll[-1])
            # Удалить последний столбец
            for index in range(0, len(matrix)):
                matrix[index].remove(matrix[index][-1])
            # Добавить последнюю строку
            for element in matrix[-1][::-1]:
                result.append(element)
            # Удалить последнюю строку
            matrix.remove(matrix[-1])
            if matrix:
                # Добавить первый столбец
                for coll in matrix[::-1]:
                    if coll:
                        result.append(coll[0])
                # Удалить первый столбец
                for index in range(0, len(matrix)):
                    matrix[index].remove(matrix[index][0])
    if result:
        return result


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(snail_path(matrix))
