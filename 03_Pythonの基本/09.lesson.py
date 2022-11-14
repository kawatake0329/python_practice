# 変数宣言では{1num = 1}のように最初に数字を入れることはできない
num = 1
name = '1'
is_ok = True

# 下記のように宣言することで型を変更することが出来る。（基本的に型宣言は使うことはない）
new_num = int(name)

print(new_num, type(new_num))

# 下記のようにtypeと書くことで何の型かわかる。
print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

num = name

print(num, type(num))