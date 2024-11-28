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
        line += roll[-1] + (' '  *  (len(str(the_largest_bill)) - len(roll[-1])))
    
    line += '\n'
    
    return line
    
def visualize(money: tuple, bar_char='₽') -> str:
    currency_symbol = bar_char * len(str(max(money)))
    result = ''
    
    coin_denominations = []
    for value in sorted(set(money)):
        coin_denominations.append(str(value))
    
    
    line_of_coin_denominations = convert_to_line(coin_denominations, max(money)).replace('\n', '')
    
    divider = '-' * len(line_of_coin_denominations) + '\n'
    
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
    #print(list(result + divider + line_of_coin_denominations))
    return result + divider + line_of_coin_denominations
    
        
            

MONEY = [10,10,1,1,1,1,20,20,20,20,20,2,2,2,2,2,2,3,3,5,5,6,100,1000,100,100,1000]

coins = (10,10,1,1,1,1,20,20,20,20,20,2,2,2,2,2,2,3,3,5,5)

def visualizes(coins, bar_char='₽'):

    unic_coin = sorted(set(coins))

    k = []
    for j in range(len(unic_coin)):
        k.append([unic_coin[j], 0])

    #print(k)

    for a in range(len(unic_coin)):
       for i in coins:
            if unic_coin[a] == i:
                k[a][1] += 1

    counter = []
    for b in range(len(unic_coin)):
        counter.append(k[b][1])

    counter_2 = []
    for b in range(len(unic_coin)):
        counter_2.append(k[b][1])

    string = []

    stroka_0 = ([bar_char*2 + ' ']*len(unic_coin) + ['\n']) # stroka_0 = ([bar_char*2 + ' ']*len(unic_coin) + ['\n'])
    stroka_1 = (['--']*len(unic_coin) + ['-']*(len(unic_coin)-1) + ['\n']) # stroka_1 = (['--']*len(unic_coin) + ['-']*(len(unic_coin)-1) + ['\n'])
    stroka_2 = list(unic_coin)
    
    stroka_22 = []
    for z in stroka_2:
        if len(str(z)) == 1: 
            stroka_22 = stroka_22 + [str(z) + '  ']
        else:
            stroka_22 = stroka_22 + [str(z) + ' ']
    stroka_22[-1] = stroka_22[-1][0:2]

    #print(stroka_22[-1])

    string_osn = []
    for r in range(len(unic_coin)):
        string_osn.append(['   ']*(len(unic_coin)-1) + ['  '] + ['\n']) # string_osn.append(['   ']*(len(unic_coin)-1) + ['  '] + ['\n'])

    h = 0
    maximum = []

    max_z = 0

    for j in range(len(unic_coin)):
        if counter == []:
            break
        maximum = [i for i, v in enumerate(counter_2) if v == max(counter)]
        if max(counter) + 1 < max_z:
            h +=1
        for p in maximum:
            if len(str(counter_2[p])) == 1:
                string_osn[h][p] = str(counter_2[p]) + '  '
            elif len(str(counter_2[p])) == 2:
                string_osn[h][p] = str(counter_2[p]) + ' '
            for y in range(h+1, len(unic_coin)):
                string_osn[y][p] = bar_char*2 + ' '
            max_z = max(counter)
            counter.remove(counter_2[p])

        h +=1


    #print(string_osn)

    for u in string_osn:
        u[5] = u[5][0]+u[5][1]
        string += list(u)

    stroka_0[5] = bar_char*2

    Ss = ''.join(string) + ''.join(stroka_0) + ''.join(stroka_1) + ''.join(stroka_22)
    #print(list(Ss))
    #print(''.join(string))

    #print(list(Ss))

    #print(list(stroka_0))

    return Ss


def visualizess(coins, bar_char='₽'):
    """Visualize money in a money box."""
    # BEGIN
    counts = Counter(coins) #Counter({2: 6, 20: 5, 1: 4, 10: 2, 3: 2, 5: 2})
    #print(counts)
    nominals = sorted(counts.keys()) #[1, 2, 3, 5, 10, 20]
    #print(nominals)
    highest_stack = max(counts.values()) #6
    # print(highest_stack)
    rows = []
    delimiter = ''
    #print(sorted(counts.items()))
    for level in range(highest_stack, -1, -1):
        row = ''
        for _, bar in sorted(counts.items()): #[(1, 4), (2, 6), (3, 2), (5, 2), (10, 2), (20, 5)]
            if bar > level:
                row += f'{bar_char * 2} '
            elif bar == level and bar != 0:
                row += f'{bar:<2d} '
                #print(list(f'{bar:<2b} '))
                
                delimiter += '---'
            else:
                row += '   '
        rows.append(row[:-1])

    rows.append(delimiter[:-1])
    row = ''
    for nominal in nominals:
        row += f'{nominal:<2d} '
    rows.append(row[:-1])

    return '\n'.join(rows)

print(visualize(MONEY))