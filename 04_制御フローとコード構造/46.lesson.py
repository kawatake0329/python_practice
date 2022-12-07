# zip関数

# forloopを使って同じ順番で同時に出力する作業。
# 今回は月曜はバナナを食べ、コーヒーを飲むと言った形に作る。
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

# zip関数を使わない場合
for i in range(len(days)):
    print(days[i],fruits[i], drinks[i])


# zip関数を使った場合
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)