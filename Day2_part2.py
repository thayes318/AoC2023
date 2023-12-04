results = {}

import csv
import time

with open(
        r'-----Day2_data.csv'
        ) as file:
    data = csv.reader(file)
    for row in file:
        game_num = row.lstrip('"Game ')
        index = game_num[:game_num.find(':')]
        results_raw = row[row.find(':')+2:]
        results_parsed = []
        print(f'game number {index}:')
        while results_raw:
            for idx,char in enumerate(results_raw):
                if char == ';':
                    results_parsed.append(results_raw[:idx])
                    results_raw = results_raw[idx+2:]
                    if not ';' in results_raw:
                        results_parsed.append(results_raw[:-2])
                        results_raw = None
                    break
        print(f'final results: {results_parsed}')
        results[index] = results_parsed

sum_total = 0

for x in results:
    max_red, max_green, max_blue = [0]*3
    game_results = [y.split(',') for y in results[x]]
    for roll in game_results:
        for color_num in roll:
            color_num = color_num.lstrip(' ')
            num = int(color_num[:color_num.find(' ')])
            if 'red' in color_num:
                max_red = max(max_red, num)
            elif 'green' in color_num:
                max_green = max(max_green, num)
            else:
                max_blue = max(max_blue, num)
    print(
        f'adding red {max_red}, blue {max_blue}, green {max_green}'
        f'for a power of {max_red * max_blue * max_green}'
        f'to total of {sum_total}')
    sum_total += (max_red * max_blue * max_green)
print(f'final total of {sum_total}')
