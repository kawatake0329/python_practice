# InとNotの使いどころ

y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

# a = 1
# b = 2

# if not a == b:
#     print('Not equal')

# if a < b:
#     print('Not equal')

is_ok = True

# もしも、is_ok の中がTrueでなければプリントする。
if is_ok != True:
    print('hello')
# 上記のようにするのではなくnot　を使用することで簡易的に書くことが出来る更に、見やすくなる。
if not is_ok:
    print('hello')

# このように反転を使う場合はnot
