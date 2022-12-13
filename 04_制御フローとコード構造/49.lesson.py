# 関数の引数と返り値の宣言

# 下記のようにすることでタイプ固定されてしまい表示されるが、
# pythonはエラーとして受け取ってくれないので注意
# 基本的にはこのように記述されることはまれである
def add_num(a: int, b: int) -> int:
    return a + b

r = add_num(10, 20)
print(r)