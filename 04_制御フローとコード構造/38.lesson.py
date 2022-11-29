# Noneを判定する場合
None
# ↑　何も入っていない状態のことを指す

is_empty = None
# print(help(is_empty))

# 下記のように is　を使うことで　is_empty　は None　であればprintという形にできる
if is_empty is None:
    print('None!!!')

# not　を使うことでNone　かどうかを判定することが出来る。
if is_empty is not None:
    print('None!!!')

# is は同じものの場合　 True
# 同じものではない場合  False
print(1 == True)
print(1 is True)
print(None is None)