# リスト内方表記

t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)

r = []
for i in t:
    if i % 2 == 0:
        r.append(i)

print(r)

# 上記のものを下の一行に簡易化(まとめ）させることが出来る(短いものに限る)
r = [i for i in t if i % 2 ==0]
print(r)

r = []
for i in t:
    for j in t2:
        r.append(i * j)

print(r)

r = [i * j for i in t for j in t2]
# こういったリスト内に行うことだが多用すると他の人が読みにくくなる可能性があるため
# for if の組み合わせの場合等の条件を絞る形のものなら使いやすい！