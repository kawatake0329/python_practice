r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3, 3))

print(r.count(3))

if 100 in r:
    print('exist')
    
r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s ='My name is Mike.'
# split　存在する文字を指定することでその場所で分けてlist化してくれる。
to_split = s.split(' ')
print(to_split)

# 逆に空白のところで文字列に戻してくれる(上の作業でlist化したのを元に戻した)
x = ' '.join(to_split)
print(x)