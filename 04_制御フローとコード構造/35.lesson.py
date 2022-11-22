# 比較演算子と論理演算子
a = 3
b = 3

# a が b と等しい
if a == b:
    print('epual')

# a が b と異なる
a != b

# a が b よりも小さい
a < b

# a が b よりも大きい
a > b

# a が b 以下である
a <= b

# a が b 以上である
a >= b

# a も b も真であれば真
if a < 0 and b > 0:
    print('a and b are positive')

# a または b が真であれば真
a = -1
a = 1
if a > 0 or b > 0:
    print('a or b is positive')