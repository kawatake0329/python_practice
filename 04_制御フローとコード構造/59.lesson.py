# ジェネレーター
l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)


print('#################')

def counter(num=10):
    for _ in range(num):
        yield 'run'


# ジェネレーターは小分けして使う場合に使用される

# 下記のようにyieldの間に重たい処理などが入る場合や
def greeting():
    yield 'Good morning'
    for i in range(100000):
        print(i)
    yield 'Good agternoon'
    yield 'Good night'

for g in greeting():
    print(g)


# 今日何をしたか等を表示される場合に使用される！
g = greeting()
print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print("@@@@@@")

print(next(g))

print("@@@@@@")

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))
    