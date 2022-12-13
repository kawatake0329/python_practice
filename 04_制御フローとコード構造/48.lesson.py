# 関数定義

def say_something():
    print('hi')

# 下記のように関数定義を行った物を呼び出す際、後ろに（）を付けるようにしなければならない。
say_something()

# タイプを見ることもできる
print(type(say_something))

f = say_something
f()

def say_something():
    s = 'hi'
    return s

result = say_something
print(result)

def what_is_this(color):
    print(color)
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"
    

result = what_is_this('red')
result = what_is_this('green')
result = what_is_this('yellow')
print(result)

# 関数を使う場合というのは、
# 何回も呼び出さなければならないものを簡単に呼び出せるようにすることが出来る。