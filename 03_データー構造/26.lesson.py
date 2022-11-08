# 辞書のコピーについて

# リストと同様に参照渡しになる
x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y)

# リストと同様に copy を使うことで防ぐことが出来る
x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)