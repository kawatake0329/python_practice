# デフォルト引数で気を付ける事
def test_func(x, l=[]):
    l.append(x)
    return l

y = [1, 2, 3]
r = test_func(100, y)
print(r)

y = [1, 2, 3]
r = test_func(200, y)
print(r)



def test_func(x, l=[None]):
    if l is None:
        l = []
    l.append(x)
    return l

# 下記のように　二つ連続して行うと同じ所に値が入ってしまうのでバグに繋がってしまう。
# そのため上記のようにからのリスト等にはNoneを使うことで改善することが可能。
r = test_func(100)
print(r)

r = test_func(100)
print(r)