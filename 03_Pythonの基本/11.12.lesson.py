s = 'test'
print('hello')
print('hello')
# ↓シングルクォーテーションを混ぜる時ダブルクォーテーションを使いエラーが出ないようにする
print("I don't kow")
# ↓シングルクォーテーションのみの場合スラッシュ\を使って区別する
print('I don\'t kow')
# ↓シングルクォーテーションとダブルクォーテーションを使って文字列の違いを出せる
print('say "I don\t know"')
print("say \"I don't know\"")

print('hello.\nHow are you?')
# 下記のように\nで改行と認識されてしまう場合カッコ内の最初にｒを付けることでスラッシュを文字列と認識してくれる
print(r'C:\name\name')

# 下記のように　”　を三つ使うことで改行してくれる　また、＃＃＃を使い仕切りを付けた後一行開けたい場合に　\　を使うことで一行改行してくれる。
print("############")
print("""\
line1
line2
line3\
""")
print("############")

print('Hi.' * 3 + 'Mike.')

# 長い変数や文字列の場合見やすくするために改行出来るように使ったりする
s = ('py''thon')

print(s)


# 12.のレッスン開始

word = 'python'
# 下記のように変数を数字で指定することでその文字番の文字のみ表示されるようになる
print(word[0])
print(word[1])
print(word[-1])
print(word[0:1])
print(word[2:5])
print('############')
print(word[0:2])
print(word[:2])
print('############')
print(word[2:])
print('############')
# 下記のように変数の文字列の特定の物をを変えたい時番号と変更したい記述を　+　で変数宣言することで変更可能
word = 'j' + word[1:]
print(word[:])
n = len(word)
print(n)