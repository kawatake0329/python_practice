# tupleの使いどころ
# 例：　三つの選択肢の中から二つ選んでくださいといったアプリケーション
chose_from_two = ('A','B','C')
# chose_from_two = ['A','B','C']
#上記のコメントのtapleを使用しなかった場合、下記のように変数名を使った中に答えを入れると変数に追加されてしまい求めてる答えが帰ってこなくなる

answer = []

chose_from_two.append('A')
chose_from_two.append('C')

# answer.append('A')
# answer.append('C')

print(chose_from_two)
print(answer)


# 24.lesson開始
# 辞書型
# ターミナルでの作業

# d = {'x': 10, 'y'; 20}
# 下記のように [] の中に変えたい変数を指定して、書き込みたい内容を'xxxx'に入れる
# d['x'] = 'xxxx'

# 二つ目のやり方
# dict(a=10, b=20)
# 三つ目のやり方、あまり使わない可能性あり
# dict([('a', 10), ('b', 20)])


# 25.lesson
#辞書型のメソッドについて
# ターミナルでの作業

# keys()
# 変数名を表示する
# valuse()
# 変数内を表示する
# update(x)
# 指定した変数を追加、上書きする
# pop('x')
# 指定した変数を取り出す
# del
# 指定したものを削除
# 'x' in d
# 指定したものが入っているか　True or False