def summary_ranges(interval: list) -> list:
    result = []
    sequence = []
    for index in range(0, len(interval) - 1):
        num1 = interval[index]
        num2 = interval[index + 1]
        if num1 + 1 == num2:
            if not sequence:
                sequence.append(num1)
                sequence.append(num2)
            else:
                sequence.append(num2)
        else:
            if sequence:
                result.append(f'{sequence[0]}->{sequence[-1]}')
                sequence = []
    return result


print(summary_ranges([110, 111, 112, 111, -5, -4, -2, -3, -4, -5]))
