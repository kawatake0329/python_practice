# enumerate関数

# インデックスのように果物の前に番号を入れる作業。
# enumerate関数を使わない場合
i = 0
for fruit in ['apple', 'banana', 'orange']:
    print(i, fruit)
    i += 1

# enumerate関数を使った場合
for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i,fruit)