# 集合の使いどころ
# フレンドの共通のフレンドを探す場合のように、共通のものを探すのに便利
my_friends = {'A','C','D'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_friends & A_friends)

f = {'apple', 'banana', 'apple', 'banana'}
kind = set(f)
print(kind)
