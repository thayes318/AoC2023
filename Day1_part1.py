import pandas as pd

df = pd.read_csv(
    r'-----Day1_data.csv',
    header=None,
    names=['input'])
total = 0

for x in df['input']:
    a, b = [0]*2
    num_list = []
    print(f'full string - {x}')
    for i, y in enumerate(x):
        try:
            if int(y) in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
                num_list.append(int(y))
                print(f'{int(y)} found at {i}')
                print(f'remaining string - {x[i+1:]}')
        except ValueError:
            pass
    print(f'numbers found: {num_list}')
    c = str(num_list[0]) + str(num_list[len(num_list)-1])
    df.loc[df.index[df['input'] == x], 'value'] = int(c)

    total += int(c)
    print(f'{int(c)} added to total for new total of {total}')
