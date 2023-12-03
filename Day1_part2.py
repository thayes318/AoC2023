import pandas as pd

df = pd.read_csv(
    r'-----Day1_data.csv',
    header=None,
    names=['input'])
total = 0
lookups = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
           'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


for x in df['input']:
    a, b = [0]*2
    num_list = []
    print(f'full string - {x}')
    for i, y in enumerate(x):
        try:
            value = int(y)
            print(f'adding {int(y)}')
            num_list.append(value)
        except ValueError:
            for z in range(len(x)+1):
                if x[i:z] in lookups.keys():
                    print(f'adding {x[i:z]}')
                    num_list.append(lookups[x[i:z]])

    print(f'numbers found: {num_list}')
    c = str(num_list[0]) + str(num_list[len(num_list)-1])
    df.loc[df.index[df['input'] == x], 'value'] = int(c)

    total += int(c)
    print(f'{int(c)} added to total for new total of {total}')
