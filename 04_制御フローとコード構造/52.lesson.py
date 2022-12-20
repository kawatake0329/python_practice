# 位置引数のタプル化
def say_something(word, word2, word3):
    print(word)
    print(word2)
    
say_something('Hi', 'Mike', 'Nance')


def say_something (word,*args):
    print('word =', word)
    for arg in args:
        print(arg)

# 下記のように引数を何個入れても上記のargsでまとめてタプル化してくれるようになる！
say_something('Hi!', 'Mike', 'Nancy')