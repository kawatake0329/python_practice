# キーワード引数の辞書化


# def  menu(entree='beef', drink='wine'):
#     print(entree,drink)
# 上記のように最初作った後、どんどん項目を追加したい時
# パターン一つ目
def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

menu(entree='beef', drink='coffee')

# パターン二つ目
d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}
menu(**d)

# タプル化と辞書化同時に行う場合
# 下記の行のargsとkwargsを逆に書くとエラーが起こる順番に気を付ける
def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

# 下記のようにすることでfoodにbananaが入りargsにappleとorangeが入るその後は上と一緒
menu('banana', 'apple', 'orange', entree='beef', drink='coffee')
