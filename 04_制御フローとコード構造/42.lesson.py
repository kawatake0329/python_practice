# for文とbreak文とcontinue文
some_list = [1, 2, 3, 4, 5]

# i = 0
# while i < len(some_list):
#     print(some_list[i])
#     i += 1

# イテレーター反復処理を行ってくれるもので今回のは
# listの中のものがなくなったら終了してくるものとなる
for i in some_list:
    print(i)

# 文字列でも可能
for s in 'abcde':
    print(s)

# 下記のようにbreakやcontinueを使うことで途中でループを抜けることや飛ばすことも可能
for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        break
    print(word)