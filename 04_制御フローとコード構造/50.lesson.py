# 位置引数とキーワード引数とデフォルト引数

def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)
    
# 位置引数
# 上記の順番で変数内に出力されるので下記に入れる順番を間違わないように気を付ける。
menu('beef', 'beer', 'ice')

# キーワード引数
# 下記のようにキーワードを入れることで順番関係なく入力することが出来る。
# 位置引数と両用することもできるが位置がずれると不可
menu(entree='beef', dessert='beer', drink='ice')

# デフォルト引数
def menu(entree='beef', drink='wine', dessert='ice'):
    print(entree)
    print(drink)
    print(dessert)

# デフォルトが指定されているので何も入力しなくても表示される。
# 追加で入力すると変更することが出来る
menu('chicken', drink='beer')