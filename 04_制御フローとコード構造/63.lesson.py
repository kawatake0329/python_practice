# ジェネレーター内包表記

def g():
    for i in range(10):
        yield i

g = g()

# タプルにならずにジェネレーターになるタプルにする場合は下記のように行う！
g = tuple(i for i in range(10))
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))