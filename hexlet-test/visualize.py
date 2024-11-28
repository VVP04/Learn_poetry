from collections import Counter


def convert_to_line(roll: list, the_largest_bill: int) -> str:
    line = ''
    for symbol in roll[:-1]:
        if len(symbol) < len(str(the_largest_bill)):
            line += symbol
            line += ' ' * (len(str(the_largest_bill)) - (len(symbol) - 1))
        elif len(symbol) == len(str(the_largest_bill)):
            line += symbol
            line += ' '
    if len(roll[-1]) == len(str(the_largest_bill)):
        line += roll[-1]
    else:
        line += roll[-1] + (' ' * (len(str(the_largest_bill)) - len(roll[-1])))
    line += '\n'
    return line


def visualize(money: tuple, bar_char='₽') -> str:
    currency_symbol = bar_char * len(str(max(money)))
    result = ''
    coin_denominations = []

    for value in sorted(set(money)):
        coin_denominations.append(str(value))

    line_of_coin_denomination = convert_to_line(coin_denominations, max(money))
    line_of_coin_denomination = line_of_coin_denomination.replace('\n', '')
    divider = '-' * len(line_of_coin_denomination) + '\n'

    num_of_coins = []
    c = Counter(money)
    for face_value in sorted(set(money)):
        num_of_coins.append(c[face_value])

    for num_of_line in reversed(range(0, max(num_of_coins) + 1)):
        line = []

        for stack in num_of_coins:
            if stack > num_of_line:
                line.append(currency_symbol)

            elif stack == num_of_line:
                line.append(str(stack))

            else:
                line.append(' ')

        result += convert_to_line(line, max(money))

    return result + divider + line_of_coin_denomination


MONEY = [
    10, 10, 1, 1, 1, 1,
    20, 20, 20, 20, 20,
    2, 2, 2, 2, 2, 2, 3,
    3, 5, 5, 6, 100,
    1000, 100, 100, 1000
]
print(visualize(MONEY))
