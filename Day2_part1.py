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

def conditions(check_item, color, limit, game_results):
    check_item = int(check_item[:-len(color)-1])
    if check_item > limit:
        game_results.append('not possible')
    return game_results

for x in results:
    game_results = [y.split(',') for y in results[x]]
    for roll in game_results:
        for color_num in roll:
            print(results[x])
            if 'red' in color_num:
                results[x] = conditions(color_num,'red',12,results[x])
            elif 'green' in color_num:
                results[x] = conditions(color_num,'green',13,results[x])
            else:
                results[x] = conditions(color_num,'blue',14,results[x])
            print(results[x])
sum_total = 0
for x in results:
    if 'not possible' not in results[x]:
        print(f'adding {x} to total of {sum_total}')
        sum_total += int(x)
print(f'final total of {sum_total}')